import numpy as np
import matplotlib.pyplot as plt
from visualize_routes import calculate_tour_length

def run_oman_demo():
    print("=" * 60)
    print("ASYAD OMAN DELIVERY OPTIMIZATION DEMO")
    print("=" * 60)
    
    # 1. Generate Muscat-like locations
    print("\n1. Generating delivery locations in Muscat...")
    locations = generate_muscat_locations(10)
    print(f"   Depot: {locations[0]} (Al Seeb area)")
    print(f"   9 delivery stops generated")
    
    # 2. For demo, use greedy tour (replace with your model later)
    print("\n2. Finding optimal delivery sequence...")
    # Simple greedy for now
    tour = greedy_tour(locations)
    length = calculate_tour_length(locations, tour)
    print(f"   Route length: {length:.3f} units")
    print(f"   Route: {tour}")
    
    # 3. Show visualization
    print("\n3. Creating route visualization...")
    plot_muscat_route(locations, tour, 
                     title=f"ASYAD Muscat Delivery Route\nLength: {length:.3f}")
    
    # 4. Show Oman-specific info
    print("\n4. Oman-Specific Constraints Applied:")
    constraints = add_muscat_constraints()
    print(f"   - Avoid deliveries during prayer times")
    print(f"   - Business deliveries: {constraints['time_windows']['preferred']['business'][0]}-{constraints['time_windows']['preferred']['business'][1]}")
    print(f"   - Residential deliveries: {constraints['time_windows']['preferred']['residential'][0]}-{constraints['time_windows']['preferred']['residential'][1]}")
    
    return locations, tour

# Helper function (greedy algorithm)
def greedy_tour(locations):
    n = len(locations)
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    while unvisited:
        nearest = min(unvisited, key=lambda x: np.linalg.norm(locations[x] - locations[current]))
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    tour.append(0)
    return tour

if __name__ == "__main__":
    run_oman_demo()