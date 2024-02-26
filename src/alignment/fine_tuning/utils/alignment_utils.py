import open3d as o3d
import numpy as np

def extract_features(point_cloud, voxel_size):
    """
    特徵提取和描述
    """
    radius_normal = voxel_size * 2
    point_cloud.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

    radius_feature = voxel_size * 5
    fpfh = o3d.pipelines.registration.compute_fpfh_feature(
        point_cloud,
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    return fpfh

def match_features(fpfh_source, fpfh_target, source, target, distance_threshold=0.025):
    """
    特徵點匹配策略
    """
    result = o3d.pipelines.registration.registration_ransac_based_on_feature_matching(
        source, target, fpfh_source, fpfh_target, True,
        distance_threshold,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(False),
        4,
        [o3d.pipelines.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
         o3d.pipelines.registration.CorrespondenceCheckerBasedOnDistance(distance_threshold)],
        o3d.pipelines.registration.RANSACConvergenceCriteria(5000, 400))
    return result

def remove_outliers(point_cloud, nb_neighbors=20, std_ratio=2.0):
    """
    異常點去除
    """
    _, ind = point_cloud.remove_statistical_outlier(nb_neighbors, std_ratio)
    return point_cloud.select_by_index(ind)

def evaluate_alignment(source, target, transformation):
    """
    對齊結果評估
    """
    evaluation = o3d.pipelines.registration.evaluate_registration(
        source, target, 0.03, transformation)
    return evaluation

# 使用示例
if __name__ == "__main__":
    # 讀取點雲
    source = o3d.io.read_point_cloud("path_to_your_source_point_cloud.ply")
    target = o3d.io.read_point_cloud("path_to_your_target_point_cloud.ply")
    
    # 特徵提取和描述
    voxel_size = 0.05  # 定義一個合適的體素大小
    fpfh_source = extract_features(source, voxel_size)
    fpfh_target = extract_features(target, voxel_size)
    
    # 特徵匹配
    result = match_features(fpfh_source, fpfh_target, source, target)
    
    # 異常點去除
    source_clean = remove_outliers(source)
    target_clean = remove_outliers(target)
    
    # 對齊結果評估
    evaluation = evaluate_alignment(source_clean, target_clean, result.transformation)
    print("對齊結果評估:", evaluation)
