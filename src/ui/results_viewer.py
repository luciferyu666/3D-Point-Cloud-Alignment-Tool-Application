import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np

def visualize_point_cloud(pcd_file):
    """
    使用Open3D視覺化點雲文件。
    """
    pcd = o3d.io.read_point_cloud(pcd_file)
    o3d.visualization.draw_geometries([pcd])

def plot_alignment_quality(quality_metrics):
    """
    使用matplotlib展示對齊質量的指標。
    """
    fig, ax = plt.subplots()
    ax.bar(range(len(quality_metrics)), list(quality_metrics.values()), align='center')
    plt.xticks(range(len(quality_metrics)), list(quality_metrics.keys()))
    plt.ylabel('質量指標')
    plt.title('對齊質量評估')
    plt.show()

if __name__ == "__main__":
    # 示範使用
    visualize_point_cloud("path_to_your_point_cloud.ply")
    
    # 對齊質量指標示範數據
    quality_metrics = {"重疊度": 0.8, "平均距離差異": 0.05}
    plot_alignment_quality(quality_metrics)
