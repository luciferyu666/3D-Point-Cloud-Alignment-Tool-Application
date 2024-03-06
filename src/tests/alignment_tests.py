import open3d as o3d
import numpy as np

def calculate_point_cloud_distance(source_point_cloud, target_point_cloud):
    source = o3d.geometry.PointCloud()
    target = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(source_point_cloud)
    target.points = o3d.utility.Vector3dVector(target_point_cloud)
    
    # Compute the distance from the source to target point cloud
    distance = source.compute_point_cloud_distance(target)
    return np.mean(distance)

def evaluate_alignment_performance(source_point_cloud, target_point_cloud, transformation_matrix):
    source_aligned = source_point_cloud.transform(transformation_matrix)
    distance = calculate_point_cloud_distance(source_aligned, target_point_cloud)
    print(f"Average distance between aligned point clouds: {distance}")

    return distance
