import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def plot_route(locations, tour, title="VRP Solution", save_path=None):
    """
    Plot a VRP route
    locations: (N, 2) array of coordinates
    tour: list of indices showing visit order
    """
    plt.figure(figsize=(10, 10))
    
    # Plot all locations
    plt.scatter(locations[1:, 0], locations[1:, 1], 
                c='blue', s=200, alpha=0.6, label='Customers')
    
    # Plot depot
    plt.scatter(locations[0, 0], locations[0, 1], 
                c='red', s=400, marker='s', label='Depot', zorder=5)
    
    # Plot route
    for i in range(len(tour) - 1):
        start = locations[tour[i]]
        end = locations[tour[i+1]]
        
        arrow = FancyArrowPatch(start, end,
                                arrowstyle='->', 
                                color='green',
                                linewidth=2,
                                mutation_scale=20,
                                alpha=0.7)
        plt.gca().add_patch(arrow)
    
    # Add labels
    for i, loc in enumerate(locations):
        label = 'D' if i == 0 else str(i)
        plt.annotate(label, (loc[0], loc[1]), 
                    fontsize=12, ha='center', va='center')
    
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    plt.legend()
    plt.title(title)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
    plt.close()

def calculate_tour_length(locations, tour):
    """Calculate total distance of tour"""
    total = 0
    for i in range(len(tour) - 1):
        start = locations[tour[i]]
        end = locations[tour[i+1]]
        total += np.linalg.norm(end - start)
    return total

if __name__ == "__main__":
    # Test with random data
    test_locations = np.random.rand(10, 2)
    test_locations[0] = [0.5, 0.5]  # depot
    test_tour = [0, 1, 3, 5, 2, 7, 9, 4, 6, 8, 0]
    
    length = calculate_tour_length(test_locations, test_tour)
    plot_route(test_locations, test_tour, 
              title=f"VRP Solution - Length: {length:.3f}",
              save_path="demo_route.png") 
