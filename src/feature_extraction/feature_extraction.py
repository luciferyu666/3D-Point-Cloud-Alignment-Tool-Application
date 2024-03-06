import cv2
import numpy as np

def extract_features(image, method='SIFT'):
    if method == 'SIFT':
        detector = cv2.SIFT_create()
    elif method == 'SURF':
        detector = cv2.xfeatures2d.SURF_create()
    elif method == 'ORB':
        detector = cv2.ORB_create(nfeatures=1500)
    else:
        raise ValueError("Unsupported feature extraction method.")

    keypoints, descriptors = detector.detectAndCompute(image, None)
    return keypoints, descriptors
