import open3d as o3d
import numpy as np

def feature_based_alignment(source_pcd, target_pcd, voxel_size):
    """
    基於特徵的點雲對齊。

    參數:
    - source_pcd: 源點雲對象。
    - target_pcd: 目標點雲對象。
    - voxel_size: 用於下採樣的體素大小。

    返回:
    - 對齊後的源點雲對象。
    """
    # 下採樣和估計法線
    source_down = source_pcd.voxel_down_sample(voxel_size)
    target_down = target_pcd.voxel_down_sample(voxel_size)
    source_down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 2, max_nn=30))
    target_down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 2, max_nn=30))

    # 計算特徵
    source_fpfh = o3d.pipelines.registration.compute_fpfh_feature(source_down, o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 5, max_nn=100))
    target_fpfh = o3d.pipelines.registration.compute_fpfh_feature(target_down, o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 5, max_nn=100))
    
    # 特徵匹配和對齊
    result = o3d.pipelines.registration.registration_ransac_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh, True,
        distance_threshold=voxel_size * 1.5,
        ransac_n=4,
        checkers=[o3d.pipelines.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
                  o3d.pipelines.registration.CorrespondenceCheckerBasedOnDistance(voxel_size * 1.5)],
        criteria=o3d.pipelines.registration.RANSACConvergenceCriteria(4000000, 500)
    )
    
    # 應用變換到源點雲
    source_pcd.transform(result.transformation)
    return source_pcd

# 使用示例
if __name__ == "__main__":
    source_pcd = o3d.io.read_point_cloud("path_to_your_source_point_cloud.ply")
    target_pcd = o3d.io.read_point_cloud("path_to_your_target_point_cloud.ply")
    voxel_size = 0.05  # 定義一個合適的體素大小

    aligned_source_pcd = feature_based_alignment(source_pcd, target_pcd, voxel_size)
    o3d.visualization.draw_geometries([aligned_source_pcd, target_pcd], window_name="Feature Based Alignment Result")
