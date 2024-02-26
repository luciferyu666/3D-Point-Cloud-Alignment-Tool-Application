import open3d as o3d
import numpy as np

def transform_point_cloud(pcd, rotation_matrix, translation_vector, scale_factor=1.0):
    """
    對3D點雲進行幾何變換，包括旋轉、平移和縮放。

    參數:
    - pcd: Open3D點雲對象。
    - rotation_matrix: 旋轉矩陣，形狀為(3, 3)。
    - translation_vector: 平移向量，形狀為(3,)。
    - scale_factor: 縮放因子。

    返回:
    - 變換後的點雲對象。
    """
    # 對點雲進行縮放
    pcd.scale(scale_factor, center=(0, 0, 0))
    
    # 對點雲進行旋轉
    pcd.rotate(rotation_matrix, center=(0, 0, 0))
    
    # 對點雲進行平移
    pcd.translate(translation_vector)
    
    return pcd

# 使用示例
if __name__ == "__main__":
    # 讀取點雲文件
    pcd = o3d.io.read_point_cloud("path_to_your_point_cloud.ply")
    
    # 定義旋轉矩陣和平移向量
    rotation_matrix = o3d.geometry.get_rotation_matrix_from_xyz((np.pi / 4, 0, np.pi / 4))  # 以X軸和Z軸為軸旋轉45度
    translation_vector = np.array([0.5, 0, 0.5])  # 沿X軸和Z軸平移0.5單位
    scale_factor = 1.5  # 縮放因子
    
    # 對點雲進行幾何變換
    transformed_pcd = transform_point_cloud(pcd, rotation_matrix, translation_vector, scale_factor)
    
    # 可選：保存變換後的點雲
    o3d.io.write_point_cloud("transformed_point_cloud.ply", transformed_pcd)
    
    print("點雲幾何變換處理完成。")
