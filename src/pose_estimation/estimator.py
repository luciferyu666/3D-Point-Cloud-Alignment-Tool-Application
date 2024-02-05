# src/pose_estimation/estimator.py
import numpy as np
import cv2

def estimate_pose_2d_3d(matches_2d, matches_3d, camera_matrix, dist_coeffs=None):
    """
    使用2D-3D點匹配和PnP算法估計相機姿態。

    參數:
    - matches_2d (np.ndarray): 圖像上的2D點，形狀為(N, 2)。
    - matches_3d (np.ndarray): 對應的3D世界點，形狀為(N, 3)。
    - camera_matrix (np.ndarray): 相機內參矩陣。
    - dist_coeffs (np.ndarray): 相機的畸變係數，可選。

    返回:
    - success (bool): 姿態估計是否成功。
    - rotation_vector (np.ndarray): 旋轉向量，描述相機旋轉。
    - translation_vector (np.ndarray): 平移向量，描述相機平移。
    """
    if dist_coeffs is None:
        dist_coeffs = np.zeros((4, 1))  # 假設無畸變
    success, rotation_vector, translation_vector = cv2.solvePnP(
        objectPoints=matches_3d,
        imagePoints=matches_2d,
        cameraMatrix=camera_matrix,
        distCoeffs=dist_coeffs,
        flags=cv2.SOLVEPNP_ITERATIVE
    )
    return success, rotation_vector, translation_vector
