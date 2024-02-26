import cv2
import numpy as np

def undistort_image(image, camera_matrix, distortion_coeffs):
    """
    對給定的圖像進行畸變矯正。

    參數:
    - image: 要矯正的圖像。
    - camera_matrix: 相機內參矩陣。
    - distortion_coeffs: 畸變係數。

    返回:
    - 矯正後的圖像。
    """
    h, w = image.shape[:2]
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coeffs, (w, h), 1, (w, h))

    # 矯正畸變
    undistorted_img = cv2.undistort(image, camera_matrix, distortion_coeffs, None, new_camera_matrix)

    # 裁剪圖像
    x, y, w, h = roi
    undistorted_img = undistorted_img[y:y+h, x:x+w]
    
    return undistorted_img

# 使用示例
if __name__ == "__main__":
    # 讀取圖像
    img = cv2.imread('path_to_your_distorted_image.jpg')
    
    # 假設的相機內參矩陣和畸變係數
    camera_matrix = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]], dtype="double")
    distortion_coeffs = np.array([k1, k2, p1, p2, k3])  # 實際應用中需要替換為實際值
    
    # 進行畸變矯正
    undistorted_img = undistort_image(img, camera_matrix, distortion_coeffs)
    
    # 顯示或保存矯正後的圖像
    cv2.imshow('Undistorted Image', undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
