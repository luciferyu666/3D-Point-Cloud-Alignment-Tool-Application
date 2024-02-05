# src/alignment/initial_alignment.py
import numpy as np
import open3d as o3d

def perform_initial_alignment(source_points: np.ndarray, target_points: np.ndarray, source_features: np.ndarray, target_features: np.ndarray, distance_threshold: float = 0.02) -> dict:
    """
    使用基於特徵的RANSAC進行初步點雲對齊。

    參數:
    - source_points: np.ndarray, 源點雲的點坐標。
    - target_points: np.ndarray, 目標點雲的點坐標。
    - source_features: np.ndarray, 源點雲的特徵描述子。
    - target_features: np.ndarray, 目標點雲的特徵描述子。
    - distance_threshold: float, RANSAC的距離閾值。

    返回:
    - dict, 包含初步對齊結果的變換矩陣等信息。
    """
    source = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(source_points)
    
    target = o3d.geometry.PointCloud()
    target.points = o3d.utility.Vector3dVector(target_points)
    
    # 創建特徵對象
    source_feature = o3d.pipelines.registration.Feature()
    source_feature.data = source_features.T
    target_feature = o3d.pipelines.registration.Feature()
    target_feature.data = target_features.T
    
    # 執行RANSAC初步對齊
    result = o3d.pipelines.registration.registration_ransac_based_on_feature_matching(
        source, target, source_feature, target_feature,
        distance_threshold,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(False),
        4,  # 每次迭代中考慮的點對數
        [o3d.pipelines.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
         o3d.pipelines.registration.CorrespondenceCheckerBasedOnDistance(distance_threshold)],
        o3d.pipelines.registration.RANSACConvergenceCriteria(4000000, 500)
    )
    
    return {
        "transformation": result.transformation,
        "inliers": result.correspondence_set
    }

# 示範用法
if __name__ == "__main__":
    # 模擬數據和特徵（需要實際提取特徵）
    source_points = np.random.rand(100, 3)
    target_points = np.random.rand(100, 3)
    source_features = np.random.rand(33, 100)
    target_features = np.random.rand(33, 100)
    
    result = perform_initial_alignment(source_points, target_points, source_features, target_features)
    print("變換矩陣:\n", result["transformation"])
    print("內點數量:", len(result["inliers"]))
