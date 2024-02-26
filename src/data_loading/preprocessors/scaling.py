import open3d as o3d

def scale_point_cloud(pcd, scale_factor):
    """
    對3D點雲進行縮放處理。

    參數:
    - pcd: Open3D點雲對象。
    - scale_factor: 縮放因子。

    返回:
    - 縮放後的點雲對象。
    """
    # 計算點雲的重心
    centroid = pcd.get_center()
    
    # 將點雲移至原點
    pcd.translate(-centroid)
    
    # 根據縮放因子對點雲進行縮放
    pcd.scale(scale_factor, center=(0, 0, 0))
    
    # 將點雲移回原來的中心位置
    pcd.translate(centroid)
    
    return pcd

# 使用示例
if __name__ == "__main__":
    # 讀取點雲文件
    pcd = o3d.io.read_point_cloud("path_to_your_point_cloud.ply")
    
    # 定義縮放因子
    scale_factor = 0.5  # 例如，將點雲縮小到原來的一半
    
    # 對點雲進行縮放處理
    scaled_pcd = scale_point_cloud(pcd, scale_factor)
    
    # 可選：保存縮放後的點雲
    o3d.io.write_point_cloud("scaled_point_cloud.ply", scaled_pcd)
    
    print("點雲縮放處理完成。")
