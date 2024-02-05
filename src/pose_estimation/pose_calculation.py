# src/pose_estimation/pose_calculation.py
import cv2
import numpy as np

def calculate_camera_pose(matched_points_2d, matched_points_3d, camera_matrix, dist_coeffs=None):
    """
    根據匹配的2D和3D點計算相機姿態。

    參數:
    - matched_points_2d (np.ndarray): 圖像平面上匹配的2D點，形狀為(N, 2)。
    - matched_points_3d (np.ndarray): 對應的3D世界點，形狀為(N, 3)。
    - camera_matrix (np.ndarray): 相機內參矩陣。
    - dist_coeffs (np.ndarray): 相機畸變係數，可選，默認為None表示無畸變。

    返回:
    - success (bool): 姿態估計是否成功。
    - rotation_vector (np.ndarray): 旋轉向量，描述相機旋轉。
    - translation_vector (np.ndarray): 平移向量，描述相機平移。
    """
    if dist_coeffs is None:
        dist_coeffs = np.zeros((4, 1))  # 假設無畸變

    success, rotation_vector, translation_vector = cv2.solvePnP(
        objectPoints=matched_points_3d,
        imagePoints=matched_points_2d,
        cameraMatrix=camera_matrix,
        distCoeffs=dist_coeffs,
        flags=cv2.SOLVEPNP_ITERATIVE
    )
    return success, rotation_vector, translation_vector

# 示範用法
if __name__ == "__main__":
    # 模擬數據
    matched_points_2d = np.random.rand(4, 2) * 100  # 假設有4個匹配點
    matched_points_3d = np.random.rand(4, 3) * 10
    camera_matrix = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]])
    dist_coeffs = np.zeros((4, 1))  # 假設無畸變

    success, rotation_vector, translation_vector = calculate_camera_pose(
        matched_points_2d, matched_points_3d, camera_matrix, dist_coeffs
    )

    if success:
        print("旋轉向量:", rotation_vector.ravel())
        print("平移向量:", translation_vector.ravel())
    else:
        print("姿態估計失敗")
