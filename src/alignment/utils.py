# src/alignment/utils.py
import numpy as np

def compute_transformation_matrix(rotation_vector: np.ndarray, translation_vector: np.ndarray) -> np.ndarray:
    """
    根據旋轉向量和平移向量計算4x4的變換矩陣。

    參數:
    - rotation_vector: np.ndarray, 旋轉向量。
    - translation_vector: np.ndarray, 平移向量。

    返回:
    - np.ndarray, 4x4的變換矩陣。
    """
    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
    transformation_matrix = np.eye(4)
    transformation_matrix[:3, :3] = rotation_matrix
    transformation_matrix[:3, 3] = translation_vector.ravel()
    return transformation_matrix

def apply_transformation(points: np.ndarray, transformation_matrix: np.ndarray) -> np.ndarray:
    """
    將變換矩陣應用於點雲數據。

    參數:
    - points: np.ndarray, 點雲數據，形狀為(N, 3)。
    - transformation_matrix: np.ndarray, 4x4的變換矩陣。

    返回:
    - np.ndarray, 變換後的點雲數據。
    """
    ones = np.ones((points.shape[0], 1))
    homogeneous_points = np.hstack((points, ones))
    transformed_points = (transformation_matrix @ homogeneous_points.T).T
    return transformed_points[:, :3]

# 需要導入cv2模組進行旋轉向量到旋轉矩陣的轉換
import cv2

# 示範用法
if __name__ == "__main__":
    rotation_vector = np.array([0.1, 0.2, 0.3])
    translation_vector = np.array([1, 2, 3])
    transformation_matrix = compute_transformation_matrix(rotation_vector, translation_vector)
    print("變換矩陣:\n", transformation_matrix)

    points = np.random.rand(100, 3)  # 模擬點雲數據
    transformed_points = apply_transformation(points, transformation_matrix)
    print("變換後的點雲數據示例:\n", transformed_points[:5])
