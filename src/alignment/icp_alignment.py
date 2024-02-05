# src/alignment/icp_alignment.py
import open3d as o3d
import numpy as np

def perform_icp(source_points: np.ndarray, target_points: np.ndarray, threshold: float = 1.0, init_transformation: np.ndarray = np.eye(4)) -> dict:
    """
    使用ICP算法對齊兩個點雲。

    參數:
    - source_points: np.ndarray, 源點雲的點坐標。
    - target_points: np.ndarray, 目標點雲的點坐標。
    - threshold: float, 尋找對應點的最大距離閾值。
    - init_transformation: np.ndarray, 初始變換矩陣。

    返回:
    - dict, 包含對齊後的點雲、變換矩陣和對齊評分等信息。
    """
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
    
    return {
        "transformed_source_points": np.asarray(result.transformation @ np.hstack((source_points, np.ones((source_points.shape[0], 1)))).T).T[:, :3],
        "transformation_matrix": result.transformation,
        "fitness": result.fitness
    }

# 示範用法
if __name__ == "__main__":
    # 模擬數據
    source_points = np.random.rand(100, 3)
    target_points = source_points + np.array([0.5, 0, 0])  # 簡單平移變換作為目標點雲
    result = perform_icp(source_points, target_points, threshold=1.0)
    print("變換矩陣:", result["transformation_matrix"])
    print("對齊評分:", result["fitness"])
