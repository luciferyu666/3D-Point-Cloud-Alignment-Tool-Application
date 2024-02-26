import open3d as o3d
import numpy as np

def normalize_point_cloud(pcd):
    """
    對3D點雲進行標準化處理，包括中心化和縮放。

    參數:
    - pcd: Open3D點雲對象。

    返回:
    - 標準化後的點雲對象。
    """
    # 計算點雲的重心
    centroid = pcd.get_center()
    
    # 將點雲移至原點
    pcd.translate(-centroid)
    
    # 獲取點雲最遠點與原點之間的最大距離
    distances = np.asarray(pcd.points) - centroid
    max_distance = np.max(np.linalg.norm(distances, axis=1))
    
    # 縮放點雲，使其最大半徑為1
    pcd.scale(1 / max_distance, center=(0, 0, 0))
    
    return pcd

# 使用示例
if __name__ == "__main__":
    # 讀取點雲文件
    pcd = o3d.io.read_point_cloud("path_to_your_point_cloud.ply")
    
    # 對點雲進行標準化處理
    normalized_pcd = normalize_point_cloud(pcd)
    
    # 可選：保存標準化後的點雲
    o3d.io.write_point_cloud("normalized_point_cloud.ply", normalized_pcd)
    
    print("點雲標準化處理完成。")
