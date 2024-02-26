import open3d as o3d

def load_and_view_point_cloud(file_path):
    """
    加載並視覺化點雲數據。
    """
    # 加載點雲文件
    pcd = o3d.io.read_point_cloud(file_path)

    # 計算並輸出點雲的一些基本屬性
    print(f"點雲包含 {len(pcd.points)} 個點.")
    print(f"點雲的範圍是:\n{pcd.get_axis_aligned_bounding_box()}")

    # 使用Open3D視覺化工具查看點雲
    o3d.visualization.draw_geometries([pcd], window_name="點雲查看器", width=800, height=600)

if __name__ == "__main__":
    file_path = 'path_to_your_point_cloud.ply'  # 更換為你的點雲文件路徑
    load_and_view_point_cloud(file_path)
