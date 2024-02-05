# src/visualization/error_heatmap.py
import numpy as np
import matplotlib.pyplot as plt

def calculate_point_distances(source_points, target_points):
    """
    計算源點雲和目標點雲之間點對點的距離。
    
    參數:
    - source_points: np.ndarray, 源點雲的點座標。
    - target_points: np.ndarray, 目標點雲的點座標。
    
    返回:
    - distances: np.ndarray, 點對點距離的數組。
    """
    if source_points.shape != target_points.shape:
        raise ValueError("源點雲和目標點雲的形狀必須相同。")
    
    distances = np.sqrt(np.sum((source_points - target_points) ** 2, axis=1))
    return distances

def plot_error_heatmap(distances, title="誤差熱圖"):
    """
    根據點對點距離繪製誤差熱圖。
    
    參數:
    - distances: np.ndarray, 點對點距離的數組。
    - title: str, 熱圖的標題。
    """
    plt.figure(figsize=(10, 8))
    plt.hist(distances, bins=50, cmap='hot', density=True)
    plt.colorbar(label='密度')
    plt.title(title)
    plt.xlabel('點對點距離')
    plt.ylabel('頻率')
    plt.show()

# 示範用法
if __name__ == "__main__":
    # 隨機生成模擬點雲數據進行測試
    source = np.random.rand(100, 3)
    target = source + np.random.normal(0, 0.01, source.shape)  # 添加噪聲模擬誤差
    
    distances = calculate_point_distances(source, target)
    plot_error_heatmap(distances)
