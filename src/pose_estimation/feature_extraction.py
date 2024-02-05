# src/pose_estimation/feature_extraction.py
import cv2
import numpy as np

def extract_features(image, method='SIFT', nfeatures=500):
    """
    從圖像中提取特徵點和描述子。

    參數:
    - image (np.ndarray): 待處理的圖像。
    - method (str): 特徵提取算法，默認為'SIFT'。
    - nfeatures (int): 要提取的特徵點數量上限。

    返回:
    - keypoints (list): 特徵點列表。
    - descriptors (np.ndarray): 對應特徵點的描述子。
    """
    if method == 'SIFT':
        sift = cv2.SIFT_create(nfeatures=nfeatures)
        keypoints, descriptors = sift.detectAndCompute(image, None)
    elif method == 'ORB':
        orb = cv2.ORB_create(nfeatures=nfeatures)
        keypoints, descriptors = orb.detectAndCompute(image, None)
    else:
        raise ValueError(f"不支持的特徵提取方法: {method}")

    return keypoints, descriptors

# 示範用法
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    keypoints, descriptors = extract_features(image, method='SIFT', nfeatures=500)
    
    # 可視化特徵點
    image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Feature Points", image_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
