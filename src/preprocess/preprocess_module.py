# src/preprocess_module.py
import open3d as o3d
import numpy as np

def preprocess_point_cloud(point_cloud: o3d.geometry.PointCloud, voxel_size: float) -> o3d.geometry.PointCloud:
    """
    預處理點雲數據：降采樣、估計法線和去噪。

    參數:
    - point_cloud: o3d.geometry.PointCloud, 原始點雲對象。
    - voxel_size: float, 體素大小，用於降采樣。

    返回:
    - o3d.geometry.PointCloud, 預處理後的點雲對象。
    """
    print("原始點數:", len(point_cloud.points))

    # 降采樣使用體素下採樣
    downsampled = point_cloud.voxel_down_sample(voxel_size)
    print("降采樣後點數:", len(downsampled.points))

    # 估計法線
    radius_normal = voxel_size * 2
    downsampled.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

    # 點雲去噪
    radius_outlier = voxel_size * 2
    processed = downsampled.remove_radius_outlier(nb_points=16, radius=radius_outlier)[0]

    return processed

# 示範用法
if __name__ == "__main__":
    # 讀取點雲數據
    point_cloud = o3d.io.read_point_cloud("path/to/your/pointcloud.ply")
    voxel_size = 0.02  # 定義體素大小

    # 預處理點雲
    processed_point_cloud = preprocess_point_cloud(point_cloud, voxel_size)

    # 可視化預處理後的點雲
    o3d.visualization.draw_geometries([processed_point_cloud], window_name="Processed Point Cloud")
