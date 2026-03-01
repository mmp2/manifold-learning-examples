import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn import manifold
import random

# This file contains helper functions to generate a cityscape with buildings and roads 
# to be used for manifold learning algorithms.

class Building:
    """Represents a rectangular building with given dimensions"""
    def __init__(self, x, y, z, width, depth, height):
        self.x = x  # x coordinate of bottom-left corner
        self.y = y  # y coordinate of bottom-left corner  
        self.z = z  # z coordinate of bottom
        self.width = width
        self.depth = depth
        self.height = height
        self.volume = width * depth * height
        
    def contains_point(self, point):
        """Check if a point is inside this building"""
        px, py, pz = point
        return (self.x <= px <= self.x + self.width and
                self.y <= py <= self.y + self.depth and
                self.z <= pz <= self.z + self.height)
    
    def sample_point(self):
        """Sample a random point uniformly from this building"""
        px = self.x + random.uniform(0, self.width)
        py = self.y + random.uniform(0, self.depth)
        pz = self.z + random.uniform(0, self.height)
        return np.array([px, py, pz])

class Road:
    """Represents a straight road connecting two buildings"""
    def __init__(self, start_building, end_building, width=1, height=1):
        self.start = start_building
        self.end = end_building
        self.width = width
        self.height = height
        
        # Calculate road dimensions
        self.start_x = start_building.x + start_building.width/2
        self.start_y = start_building.y + start_building.depth/2
        self.start_z = start_building.z + start_building.height
        
        self.end_x = end_building.x + end_building.width/2
        self.end_y = end_building.y + end_building.depth/2
        self.end_z = end_building.z + end_building.height
        
        # Calculate road length and volume
        self.length = np.sqrt((self.end_x - self.start_x)**2 + 
                             (self.end_y - self.start_y)**2 + 
                             (self.end_z - self.start_z)**2)
        self.volume = self.length * self.width * self.height
        
    def contains_point(self, point):
        """Check if a point is on this road"""
        px, py, pz = point
        
        # Check if point is within the road's bounding box
        min_x = min(self.start_x, self.end_x) - self.width/2
        max_x = max(self.start_x, self.end_x) + self.width/2
        min_y = min(self.start_y, self.end_y) - self.width/2
        max_y = max(self.start_y, self.end_y) + self.width/2
        min_z = min(self.start_z, self.end_z)
        max_z = max(self.start_z, self.end_z) + self.height
        
        return (min_x <= px <= max_x and
                min_y <= py <= max_y and
                min_z <= pz <= max_z)
    
    def sample_point(self):
        """Sample a random point uniformly from this road"""
        # Sample a random position along the road
        t = random.uniform(0, 1)
        
        # Interpolate position
        px = self.start_x + t * (self.end_x - self.start_x)
        py = self.start_y + t * (self.end_y - self.start_y)
        pz = self.start_z + t * (self.end_z - self.start_z)
        
        # Add random offset within road width
        offset_x = random.uniform(-self.width/2, self.width/2)
        offset_y = random.uniform(-self.width/2, self.width/2)
        offset_z = random.uniform(0, self.height)
        
        return np.array([px + offset_x, py + offset_y, pz + offset_z])

def generate_cityscape():
    """Generate a cityscape with buildings and roads"""
    buildings = []
    roads = []
    
    # Create some buildings with different sizes
    buildings.append(Building(0, 0, 0, 3, 5, 10))      # 3x5x10 building
    buildings.append(Building(8, 0, 0, 2, 2, 15))      # 2x2x15 building  
    buildings.append(Building(0, 8, 0, 4, 3, 8))       # 4x3x8 building
    buildings.append(Building(8, 8, 0, 2, 4, 12))      # 2x4x12 building
    buildings.append(Building(4, 4, 0, 1, 1, 20))      # 1x1x20 building (tower)
    
    # Create roads connecting buildings
    roads.append(Road(buildings[0], buildings[1]))     # Connect building 0 to 1
    roads.append(Road(buildings[0], buildings[2]))     # Connect building 0 to 2
    roads.append(Road(buildings[1], buildings[3]))     # Connect building 1 to 3
    roads.append(Road(buildings[2], buildings[3]))     # Connect building 2 to 3
    roads.append(Road(buildings[4], buildings[0]))     # Connect tower to building 0
    roads.append(Road(buildings[4], buildings[1]))     # Connect tower to building 1
    
    return buildings, roads

def sample_points_mixture_uniform(buildings, roads, n_samples=5000):
    """
    Sample points proportionally to volume using mixture uniform sampling.
    
    This means:
    - Calculate total volume of all buildings + roads
    - For each building/road, calculate its probability = volume/total_volume
    - Sample n_samples points, where each point has probability of coming from
      each building/road proportional to its volume
    """
    # Calculate total volume
    total_volume = sum(building.volume for building in buildings) + sum(road.volume for road in roads)
    
    # Calculate probabilities for each building and road
    building_probs = [building.volume / total_volume for building in buildings]
    road_probs = [road.volume / total_volume for road in roads]
    
    # Sample points
    sampled_points = []
    sampled_labels = []  # Track which building/road each point came from
    
    for _ in range(n_samples):
        # Choose which building or road to sample from
        rand = random.random()
        cumulative_prob = 0
        
        # Check buildings first
        for i, prob in enumerate(building_probs):
            cumulative_prob += prob
            if rand <= cumulative_prob:
                point = buildings[i].sample_point()
                sampled_points.append(point)
                sampled_labels.append(f"Building_{i}")
                break
        else:
            # If not from buildings, sample from roads
            cumulative_prob = sum(building_probs)
            for i, prob in enumerate(road_probs):
                cumulative_prob += prob
                if rand <= cumulative_prob:
                    point = roads[i].sample_point()
                    sampled_points.append(point)
                    sampled_labels.append(f"Road_{i}")
                    break
    
    return np.array(sampled_points), sampled_labels

def visualize_cityscape(buildings, roads, sampled_points=None):
    """Visualize the cityscape and optionally the sampled points"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot buildings
    for i, building in enumerate(buildings):
        # Create building outline
        x = [building.x, building.x + building.width, building.x + building.width, building.x, building.x]
        y = [building.y, building.y, building.y + building.depth, building.y + building.depth, building.y]
        z = [building.z, building.z, building.z, building.z, building.z]
        
        # Plot building base
        ax.plot(x, y, z, 'b-', linewidth=2, label=f'Building {i}' if i == 0 else "")
        
        # Plot building top
        z_top = [building.z + building.height] * 5
        ax.plot(x, y, z_top, 'b-', linewidth=2)
        
        # Plot vertical edges
        for j in range(4):
            ax.plot([x[j], x[j]], [y[j], y[j]], [building.z, building.z + building.height], 'b-', linewidth=2)
    
    # Plot roads
    for i, road in enumerate(roads):
        ax.plot([road.start_x, road.end_x], 
                [road.start_y, road.end_y], 
                [road.start_z, road.end_z], 
                'r-', linewidth=3, label=f'Road {i}' if i == 0 else "")
    
    # Plot sampled points if provided
    if sampled_points is not None:
        ax.scatter(sampled_points[:, 0], sampled_points[:, 1], sampled_points[:, 2], 
                  c='green', s=1, alpha=0.6, label='Sampled Points')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Cityscape with Buildings and Roads')
    ax.legend()
    
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    # Generate cityscape
    buildings, roads = generate_cityscape()
    
    # Sample points
    sampled_points, labels = sample_points_mixture_uniform(buildings, roads, n_samples=5000)
    
    # Count points from each source
    from collections import Counter
    label_counts = Counter(labels)
    for label, count in label_counts.items():
        print(f"  {label}: {count} points")
    
    visualize_cityscape(buildings, roads, sampled_points)
