import random
import math

# Sample data as one-dimensional list
data_points = [2, 3, 4,10,11,12,20,25,30]

# Number of clusters (K)
K = 3

# Number of iterations
max_iterations = 100

# Initialize cluster centers randomly
cluster_centers = random.sample(data_points, K)
print("Random mean")
print(cluster_centers)
for _ in range(max_iterations):
    # Initialize empty clusters
    clusters = [[] for _ in range(K)]
    
    # Assign each data point to the nearest cluster
    for point in data_points:
        distances = [abs(point - center) for center in cluster_centers]
        closest_cluster = distances.index(min(distances))
        clusters[closest_cluster].append(point)
    
    # Calculate new cluster centers
    new_centers = []
    for cluster in clusters:
        if cluster:
            new_center = sum(cluster) / len(cluster)
            new_centers.append(new_center)
        else:
            # If a cluster is empty, keep the old center
            new_centers.append(cluster_centers[clusters.index(cluster)])
    
    # Check for convergence
    if new_centers == cluster_centers:
        break
   
    # Update cluster centers
    cluster_centers = new_centers
print("Mean")
print(cluster_centers)	
    	
# Print the final clusters
print("final cluster")
for i, cluster in enumerate(clusters):  		
    print(f'Cluster {i + 1}: {cluster}')
