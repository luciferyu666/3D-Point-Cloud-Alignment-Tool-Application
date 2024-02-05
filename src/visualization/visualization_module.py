# src/visualization/visualization_module.py
import open3d as o3d
from .display import display_point_cloud
from .error_heatmap import calculate_point_distances, plot_error_heatmap

class VisualizationModule:
    def __init__(self):
        pass

    def visualize_point_cloud(self, point_cloud_path):
        """
        從文件路徑讀取並顯示3D點雲。
        """
        display_point_cloud(point_cloud_path)

    def visualize_alignment_error(self, source_points, target_points):
        """
        計算並顯示對齊誤差的視圖。
        """
        distances = calculate_point_distances(source_points, target_points)
        plot_error_heatmap(distances, title="點雲對齊誤差分析")

# 示範用法
if __name__ == "__main__":
    vis_module = VisualizationModule()
    
    # 示範顯示3D點雲
    vis_module.visualize_point_cloud("path/to/your/pointcloud.ply")

    # 隨機生成模擬點雲數據進行測試對齊誤差的可視化
    source = np.random.rand(100, 3)
    target = source + np.random.normal(0, 0.01, source.shape)  # 添加噪聲模擬對齊後的點雲
    vis_module.visualize_alignment_error(source, target)
