# src/pose_estimation/camera_pose_estimator.py

import numpy as np
from .feature_extraction import extract_features
from .point_cloud_matching import match_point_clouds
from .pose_calculation import calculate_pose

class CameraPoseEstimator:
    """
    相機姿態估計類，負責從2D圖像和對應的3D點雲中估計相機的位置和朝向。
    """

    def __init__(self):
        """
        初始化相機姿態估計器。
        """
        pass  # 初始化代碼，如加載預訓練模型等

    def estimate_pose(self, image, point_cloud, method='PnP', **kwargs):
        """
        根據給定的2D圖像和3D點雲數據估計相機姿態。

        參數:
            image (np.ndarray): 輸入的2D圖像。
            point_cloud (np.ndarray): 對應的3D點雲數據。
            method (str): 使用的姿態估計算法。
            **kwargs: 算法特定的額外參數。

        返回:
            pose (np.ndarray): 估計的相機姿態，包括位置和旋轉。
        """
        # 特徵提取
        features_2d = extract_features(image, **kwargs)

        # 點雲匹配
        matched_points_3d, matched_features_2d = match_point_clouds(point_cloud, features_2d, **kwargs)

        # 姿態計算
        pose = calculate_pose(matched_features_2d, matched_points_3d, method=method, **kwargs)

        return pose

# 這裡可以添加相機姿態估計的其他輔助函數或類
