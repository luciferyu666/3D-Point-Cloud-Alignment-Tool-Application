# src/pose_estimation/__init__.py

# 導入相機姿態估計模組內部的所有必要類和函數
from .camera_pose_estimator import CameraPoseEstimator
from .feature_extraction import extract_features
from .point_cloud_matching import match_point_clouds
from .pose_calculation import calculate_pose

# 這裡可以加入任何需要在模組加載時執行的初始化代碼
# 例如，設置全局變量、加載模型、初始化資源等

# 可以選擇性地對外界暴露模組接口
__all__ = ['CameraPoseEstimator', 'extract_features', 'match_point_clouds', 'calculate_pose']
