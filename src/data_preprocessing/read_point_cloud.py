import open3d as o3d

def read_point_cloud_ply(ply_path):
    """
    讀取.PLY格式的3D點雲數據。

    參數:
        ply_path (str): 點雲文件的路徑。

    返回:
        open3d.geometry.PointCloud: 點雲對象。
    """
    pcd = o3d.io.read_point_cloud(ply_path)
    return pcd
