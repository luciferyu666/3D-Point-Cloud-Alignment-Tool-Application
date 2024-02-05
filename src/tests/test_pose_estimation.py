# src/test_pose_estimation.py
import numpy as np
from pose_estimation.camera_pose_estimator import CameraPoseEstimator

def simulate_data():
    """
    生成模擬的2D圖像特徵點和對應的3D世界坐標點。
    """
    image_points = np.array([
        [100, 200],
        [150, 250],
        [200, 300],
        [250, 350],
        [300, 400]
    ])
    
    world_points = np.array([
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
        [4, 5, 6],
        [5, 6, 7]
    ])
    
    return image_points, world_points

def test_camera_pose_estimation():
    """
    測試相機姿態估計功能。
    """
    image_points, world_points = simulate_data()
    estimator = CameraPoseEstimator()
    
    pose_estimation_result = estimator.estimate_pose(image_points, world_points)
    
    print("估計的相機姿態:\n", pose_estimation_result)

if __name__ == "__main__":
    test_camera_pose_estimation()
