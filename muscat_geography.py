import numpy as np
import matplotlib.pyplot as plt

def generate_muscat_locations(n_customers=10, seed=42):
    """
    Generate delivery locations that mimic Muscat's geography
    """
    np.random.seed(seed)
    
    # REAL Muscat geography (simplified to [0,1] square):
    # Depot: Seeb Airport/ASYAD warehouse area (approx 23.5937°N, 58.2842°E)
    # Converted to our normalized coordinates: (0.5, 0.5)
    depot = np.array([[0.5, 0.5]])
    
    customers = []
    for i in range(n_customers - 1):
        # Muscat districts probability (based on population density)
        district_roll = np.random.random()
        
        if district_roll < 0.3:  # 30% - Al Seeb (around depot)
            x = np.random.normal(0.5, 0.1)
            y = np.random.normal(0.5, 0.1)
            
        elif district_roll < 0.6:  # 30% - Coastal strip (Bausher, Muscat)
            x = np.random.uniform(0.65, 0.95)  # Right side = coast
            y = np.random.uniform(0.3, 0.7)
            
        elif district_roll < 0.85:  # 25% - Inland (Al Amrat, Mabela)
            x = np.random.uniform(0.2, 0.45)  # Left side = inland
            y = np.random.uniform(0.4, 0.6)
            
        else:  # 15% - Mountain areas (Al Hajar mountains)
            x = np.random.uniform(0.1, 0.3)
            y = np.random.uniform(0.7, 0.9)  # Top = mountains
        
        # Add some noise
        x = np.clip(x + np.random.normal(0, 0.02), 0.05, 0.95)
        y = np.clip(y + np.random.normal(0, 0.02), 0.05, 0.95)
        
        customers.append([x, y])
    
    locations = np.vstack([depot, np.array(customers)])
    return locations

# Test it
locations = generate_muscat_locations(10)
print("Generated Muscat-like locations:")
print(locations)