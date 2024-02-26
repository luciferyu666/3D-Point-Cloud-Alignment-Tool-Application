import open3d as o3d

def remove_outliers_statistical(point_cloud, nb_neighbors=20, std_ratio=2.0):
    """
    使用統計分析方法去除外點。

    參數:
    - point_cloud: 點雲對象。
    - nb_neighbors: 考慮的鄰居數量。
    - std_ratio: 標準差倍數，用於判斷外點。

    返回:
    - 處理後的點雲對象。
    """
    cl, ind = point_cloud.remove_statistical_outlier(nb_neighbors, std_ratio)
    return point_cloud.select_by_index(ind)

def remove_outliers_radius(point_cloud, nb_points=16, radius=0.05):
    """
    使用半徑異常值移除方法去除外點。

    參數:
    - point_cloud: 點雲對象。
    - nb_points: 最小點數，低於此數量的點將被視為外點。
    - radius: 搜索半徑。

    返回:
    - 處理後的點雲對象。
    """
    cl, ind = point_cloud.remove_radius_outlier(nb_points, radius)
    return point_cloud.select_by_index(ind)

# 使用示例
if __name__ == "__main__":
    # 讀取點雲數據
    pcd = o3d.io.read_point_cloud("path_to_your_point_cloud.ply")

    # 統計分析去除外點
    pcd_statistical = remove_outliers_statistical(pcd)
    # 半徑去除外點
    pcd_radius = remove_outliers_radius(pcd)

    # 可視化結果
    o3d.visualization.draw_geometries([pcd_statistical], window_name="After Statistical Outlier Removal")
    o3d.visualization.draw_geometries([pcd_radius], window_name="After Radius Outlier Removal")
