# src/comparison.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_rmsd(source_points, target_points):
    """
    計算兩組點雲之間的RMSD（均方根差）。

    參數:
    - source_points: np.ndarray, 源點雲數據。
    - target_points: np.ndarray, 目標點雲數據。

    返回:
    - float, 兩組點雲之間的RMSD值。
    """
    if source_points.shape != target_points.shape:
        raise ValueError("源點雲和目標點雲的形狀必須相同。")

    diff = source_points - target_points
    rmsd = np.sqrt(np.mean(np.sum(diff ** 2, axis=1)))
    return rmsd

def plot_point_clouds(source_points, aligned_points, title="點雲對齊比較"):
    """
    繪製對齊前後的點雲散點圖進行比較。

    參數:
    - source_points: np.ndarray, 源點雲數據。
    - aligned_points: np.ndarray, 對齊後的點雲數據。
    - title: str, 圖表標題。
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(source_points[:, 0], source_points[:, 1], source_points[:, 2], c='r', marker='o', label='源點雲')
    ax.scatter(aligned_points[:, 0], aligned_points[:, 1], aligned_points[:, 2], c='g', marker='^', label='對齊後點雲')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.title(title)
    plt.legend()
    plt.show()

# 示範用法
if __name__ == "__main__":
    source = np.random.rand(100, 3)
    target = source + np.random.normal(0, 0.02, source.shape)  # 添加噪聲模擬對齊後的點雲

    rmsd = calculate_rmsd(source, target)
    print(f"RMSD: {rmsd:.3f}")

    plot_point_clouds(source, target)
