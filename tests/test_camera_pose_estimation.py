import pytest
from modules.camera_pose_estimation import CameraPoseEstimation

def test_estimate_poses():
    # 測試相機姿態反推功能
    camera_pose_estimation = CameraPoseEstimation()
    poses = camera_pose_estimation.estimate_poses([])
    assert poses is not None
