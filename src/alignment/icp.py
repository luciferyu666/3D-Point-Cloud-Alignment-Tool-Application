# src/alignment/icp.py
import open3d as o3d
import numpy as np

def perform_icp(source_points: np.ndarray, target_points: np.ndarray, threshold: float = 0.02, init_transformation: np.ndarray = np.eye(4)) -> dict:
    """
    執行ICP算法來對齊點雲。

    參數:
    - source_points: np.ndarray, 源點雲數據。
    - target_points: np.ndarray, 目標點雲數據。
    - threshold: float, 對齊過程中考慮的最大點對距離。
    - init_transformation: np.ndarray, 對齊的初始估計變換矩陣。

    返回:
    - dict, 包含對齊結果的詳細信息。
    """
    # 將NumPy數組轉換為Open3D點雲對象
    source = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(source_points)
    target = o3d.geometry.PointCloud()
    target.points = o3d.utility.Vector3dVector(target_points)

    # 執行ICP對齊
    result = o3d.pipelines.registration.registration_icp(
        source, target, threshold, init_transformation,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000)
    )

    # 返回對齊結果
    return {
        "transformation": result.transformation,
        "fitness": result.fitness,
        "inlier_rmse": result.inlier_rmse
    }

# 示範用法
if __name__ == "__main__":
    # 模擬點雲數據
    source_points = np.random.rand(100, 3)
    target_points = source_points + np.array([0.05, 0, 0])  # 簡單平移以模擬對齊需求
    result = perform_icp(source_points, target_points, threshold=0.02)
    print("變換矩陣:\n", result["transformation"])
    print("對齊評分:", result["fitness"])
    print("內點RMSE:", result["inlier_rmse"])
