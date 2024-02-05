# src/visualization/display.py
import open3d as o3d

def display_point_cloud(point_cloud_path):
    """
    從文件讀取並顯示3D點雲。

    參數:
    - point_cloud_path: str, 點雲文件的路徑。
    """
    # 讀取點雲
    pcd = o3d.io.read_point_cloud(point_cloud_path)

    # 設置窗口標題
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="3D 點雲顯示")

    # 添加點雲到視覺化工具並顯示
    vis.add_geometry(pcd)
    vis.run()
    vis.destroy_window()

# 示範用法
if __name__ == "__main__":
    display_point_cloud("path/to/your/pointcloud.ply")
