import os
import open3d as o3d
from feature_extraction import extract_features
from alignment import align_point_clouds
from outlier_removal import remove_outliers
from global_optimization import global_optimization
from evaluation import evaluate_alignment

def load_point_clouds(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.ply')]
    point_clouds = [o3d.io.read_point_cloud(file) for file in files]
    return point_clouds

def preprocess_point_clouds(point_clouds):
    processed = []
    for pc in point_clouds:
        pc_downsampled = pc.voxel_down_sample(voxel_size=0.05)
        pc_clean = remove_outliers(pc_downsampled)
        processed.append(pc_clean)
    return processed

def perform_feature_based_alignment(point_clouds):
    features = [extract_features(pc) for pc in point_clouds]
    # Assume extract_features returns a tuple of (feature_points, descriptors)
    aligned_point_clouds = align_point_clouds(point_clouds, features)
    return aligned_point_clouds

def main():
    directory = "path_to_your_point_clouds"
    point_clouds = load_point_clouds(directory)
    processed_point_clouds = preprocess_point_clouds(point_clouds)
    aligned_point_clouds = perform_feature_based_alignment(processed_point_clouds)
    optimized_point_clouds = global_optimization(aligned_point_clouds)
    for pc in optimized_point_clouds:
        evaluate_alignment(pc)
        o3d.io.write_point_cloud("path_to_output/" + os.path.basename(pc.filename), pc)

if __name__ == "__main__":
    main()
