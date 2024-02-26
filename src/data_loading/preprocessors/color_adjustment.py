import open3d as o3d
import numpy as np

def adjust_colors(pcd, brightness_factor=1.0, contrast_factor=1.0):
    """
    對3D點雲的顏色進行調整。

    參數:
    - pcd: Open3D點雲對象，包含RGB顏色信息。
    - brightness_factor: 亮度調整因子。
    - contrast_factor: 對比度調整因子。

    返回:
    - 調整顏色後的點雲對象。
    """
    colors = np.asarray(pcd.colors)
    
    # 調整亮度
    colors = colors * brightness_factor
    colors = np.clip(colors, 0, 1)  # 保證顏色值在合理範圍內
    
    # 簡單的對比度調整示例
    mean = np.mean(colors, axis=0)
    colors = (1 - contrast_factor) * mean + contrast_factor * colors
    colors = np.clip(colors, 0, 1)  # 保證顏色值在合理範圍內
    
    pcd.colors = o3d.utility.Vector3dVector(colors)
    return pcd

# 使用示例
if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud("path_to_your_colored_point_cloud.ply")
    adjusted_pcd = adjust_colors(pcd, brightness_factor=1.1, contrast_factor=1.2)
    o3d.visualization.draw_geometries([adjusted_pcd], "Adjusted Point Cloud")
