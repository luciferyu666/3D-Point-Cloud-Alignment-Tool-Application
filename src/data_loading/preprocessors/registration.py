import open3d as o3d
import numpy as np

def preprocess_point_cloud(pcd, voxel_size):
    """
    預處理點雲：下採樣並估計法線。
    """
    pcd_down = pcd.voxel_down_sample(voxel_size)
    radius_normal = voxel_size * 2
    pcd_down.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))
    return pcd_down

def execute_global_registration(source_down, target_down, source_fpfh, target_fpfh, voxel_size):
    """
    執行點雲之間的全局初步對齊。
    """
    distance_threshold = voxel_size * 1.5
    result = o3d.pipelines.registration.registration_ransac_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh, distance_threshold,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(False),
        4, 
        [o3d.pipelines.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
         o3d.pipelines.registration.CorrespondenceCheckerBasedOnDistance(distance_threshold)],
        o3d.pipelines.registration.RANSACConvergenceCriteria(4000000, 500))
    return result

# 使用示例
if __name__ == "__main__":
    voxel_size = 0.05  # 設定體素大小
    source = o3d.io.read_point_cloud("source.ply")  # 讀取源點雲
    target = o3d.io.read_point_cloud("target.ply")  # 讀取目標點雲
    
    source_down = preprocess_point_cloud(source, voxel_size)  # 預處理源點雲
    target_down = preprocess_point_cloud(target, voxel_size)  # 預處理目標點雲
    
    # 計算FPFH特徵
    radius_feature = voxel_size * 5
    source_fpfh = o3d.pipelines.registration.compute_fpfh_feature(
        source_down, o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    target_fpfh = o3d.pipelines.registration.compute_fpfh_feature(
        target_down, o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    
    # 執行全局初步對齊
    result = execute_global_registration(source_down, target_down, source_fpfh, target_fpfh, voxel_size)
    print("初步對齊結果：", result)
    print("變換矩陣：\n", result.transformation)
    
    # 可選：將對齊後的點雲保存或進行進一步處理
