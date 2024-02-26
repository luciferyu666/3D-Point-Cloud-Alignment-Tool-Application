import cv2
import numpy as np

def estimate_camera_pose(image_points, object_points, camera_matrix, dist_coeffs):
    """
    使用PnP算法估計相機的姿態。

    參數:
    - image_points: 圖像上的點，形狀為(N, 2)。
    - object_points: 對應的3D物體點，形狀為(N, 3)。
    - camera_matrix: 相機內參矩陣。
    - dist_coeffs: 相機的畸變係數。

    返回:
    - success: 布林值，表示是否成功估計姿態。
    - rotation_vector: 旋轉向量。
    - translation_vector: 平移向量。
    """
    success, rotation_vector, translation_vector = cv2.solvePnP(
        object_points, image_points, camera_matrix, dist_coeffs)
    
    return success, rotation_vector, translation_vector

# 使用示例
if __name__ == "__main__":
    # 假設的圖像點和物體點
    image_points = np.array([[x, y] for x, y in zip(range(100, 600, 100), range(100, 600, 100))], dtype="double")
    object_points = np.array([[x, y, z] for x, y, z in zip(range(0, 500, 100), range(0, 500, 100), range(500, 0, -100))], dtype="double")
    
    # 假設的相機內參矩陣和畸變係數
    camera_matrix = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]], dtype="double")
    dist_coeffs = np.zeros((4, 1))  # 假設無畸變
    
    # 估計相機姿態
    success, rotation_vector, translation_vector = estimate_camera_pose(
        image_points, object_points, camera_matrix, dist_coeffs)
    
    if success:
        print("相機姿態估計成功。")
        print("旋轉向量:", rotation_vector)
        print("平移向量:", translation_vector)
    else:
        print("相機姿態估計失敗。")
