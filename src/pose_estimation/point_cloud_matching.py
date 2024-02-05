# src/pose_estimation/point_cloud_matching.py
import numpy as np
import cv2

def match_features_2d_to_3d(image_keypoints, image_descriptors, point_cloud, camera_matrix, dist_coeffs=None):
    """
    匹配2D圖像特徵點到3D點雲。

    參數:
    - image_keypoints (list): 2D圖像中檢測到的特徵點。
    - image_descriptors (np.ndarray): 對應於image_keypoints的特徵描述子。
    - point_cloud (np.ndarray): 3D點雲數據，形狀為(N, 3)。
    - camera_matrix (np.ndarray): 相機內參矩陣。
    - dist_coeffs (np.ndarray): 相機的畸變係數，可選。

    返回:
    - matched_points_3d (np.ndarray): 匹配到的3D點。
    - matched_keypoints_2d (list): 匹配到的2D特徵點列表。
    """
    # 這裡僅為示例框架，實際匹配邏輯需根據具體情況實現
    # 假設每個2D特徵點都能在點雲中找到一個匹配點
    matched_points_3d = np.random.rand(len(image_keypoints), 3)  # 隨機生成匹配的3D點，僅作為示例
    matched_keypoints_2d = image_keypoints  # 假設所有2D點都匹配成功

    return matched_points_3d, matched_keypoints_2d

# 示範用法
if __name__ == "__main__":
    # 模擬數據
    image_keypoints = [cv2.KeyPoint(x=np.random.randint(0, 500), y=np.random.randint(0, 500), _size=1) for _ in range(100)]
    image_descriptors = np.random.rand(100, 64)  # 假設使用SIFT，描述子維度為64
    point_cloud = np.random.rand(1000, 3)  # 模擬的3D點雲數據
    camera_matrix = np.eye(3)  # 假設的相機內參矩陣

    matched_points_3d, matched_keypoints_2d = match_features_2d_to_3d(image_keypoints, image_descriptors, point_cloud, camera_matrix)

    print("匹配到的3D點數量:", len(matched_points_3d))
