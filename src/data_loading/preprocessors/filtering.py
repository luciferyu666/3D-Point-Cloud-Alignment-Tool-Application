import open3d as o3d

def voxel_grid_filtering(point_cloud, voxel_size=0.05):
    """
    使用體素格化過濾對點雲進行降采樣。

    參數:
    - point_cloud: 要過濾的原始點雲對象。
    - voxel_size: 體素的大小。

    返回:
    - 過濾後的點雲對象。
    """
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(point_cloud, voxel_size)
    filtered_point_cloud = o3d.geometry.PointCloud()
    for voxel in voxel_grid.get_voxels():
        filtered_point_cloud.points.append(voxel.grid_index)
    return filtered_point_cloud

def statistical_outlier_removal(point_cloud, nb_neighbors=20, std_ratio=2.0):
    """
    使用統計分析去噪法移除異常點。

    參數:
    - point_cloud: 要過濾的原始點雲對象。
    - nb_neighbors: 考慮的鄰域點數。
    - std_ratio: 標準差比例。

    返回:
    - 去噪後的點雲對象。
    """
    cl, ind = point_cloud.remove_statistical_outlier(nb_neighbors, std_ratio)
    return point_cloud.select_by_index(ind)

# 使用示例
if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud("path_to_your_point_cloud.ply")
    voxel_filtered_pcd = voxel_grid_filtering(pcd)
    noise_removed_pcd = statistical_outlier_removal(voxel_filtered_pcd)
    o3d.io.write_point_cloud("filtered_point_cloud.ply", noise_removed_pcd)
    print("點雲過濾處理完成。")
