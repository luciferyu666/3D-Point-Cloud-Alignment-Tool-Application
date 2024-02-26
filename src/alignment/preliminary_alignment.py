import open3d as o3d

def preliminary_alignment(source_pcd, target_pcd, voxel_size=0.05):
    """
    對兩個點雲進行初步對齊。

    參數:
    - source_pcd: 源點雲對象。
    - target_pcd: 目標點雲對象。
    - voxel_size: 體素大小，用於點雲下採樣。

    返回:
    - 對齊後的源點雲對象。
    """
    # 下採樣點雲
    source_down = source_pcd.voxel_down_sample(voxel_size)
    target_down = target_pcd.voxel_down_sample(voxel_size)
    
    # 估計法線
    source_down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size*2, max_nn=30))
    target_down.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size*2, max_nn=30))
    
    # 使用ICP進行初步對齊
    result = o3d.pipelines.registration.registration_icp(
        source_down, target_down, voxel_size * 1.5, np.eye(4),
        o3d.pipelines.registration.TransformationEstimationPointToPlane())
    
    # 應用變換到源點雲
    source_pcd.transform(result.transformation)
    
    return source_pcd

# 使用示例
if __name__ == "__main__":
    source_pcd = o3d.io.read_point_cloud("path_to_your_source_point_cloud.ply")
    target_pcd = o3d.io.read_point_cloud("path_to_your_target_point_cloud.ply")
    
    aligned_source_pcd = preliminary_alignment(source_pcd, target_pcd)
    o3d.visualization.draw_geometries([aligned_source_pcd, target_pcd], window_name="Preliminary Alignment")
