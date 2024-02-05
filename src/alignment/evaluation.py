# src/alignment/evaluation.py
import numpy as np

def calculate_rmse(source_points: np.ndarray, target_points: np.ndarray, transformation_matrix: np.ndarray) -> float:
    """
    計算對齊後源點雲到目標點雲的均方根誤差(RMSE)。

    參數:
    - source_points: np.ndarray, 源點雲的點坐標。
    - target_points: np.ndarray, 目標點雲的點坐標。
    - transformation_matrix: np.ndarray, 對齊變換矩陣。

    返回:
    - float, 均方根誤差值。
    """
    if source_points.shape[0] != target_points.shape[0]:
        raise ValueError("源點雲和目標點雲的點數必須相等。")

    # 將源點雲通過變換矩陣轉換到目標點雲的坐標系
    ones = np.ones((source_points.shape[0], 1))
    homogeneous_source_points = np.hstack((source_points, ones))
    transformed_points = (transformation_matrix @ homogeneous_source_points.T).T[:, :3]

    # 計算每個點之間的歐氏距離
    distances = np.linalg.norm(transformed_points - target_points, axis=1)
    
    # 計算均方根誤差
    rmse = np.sqrt(np.mean(distances**2))
    return rmse

# 示範用法
if __name__ == "__main__":
    # 模擬數據
    source_points = np.random.rand(100, 3)
    target_points = source_points + np.random.normal(0, 0.01, source_points.shape)
    transformation_matrix = np.eye(4)  # 假設是一個單位矩陣，即無變換

    rmse = calculate_rmse(source_points, target_points, transformation_matrix)
    print(f"均方根誤差(RMSE): {rmse}")
