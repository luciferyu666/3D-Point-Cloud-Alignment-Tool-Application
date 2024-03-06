import cv2
import numpy as np

def match_features(descriptor1, descriptor2, method='FLANN', crossCheck=True):
    if method == 'FLANN':
        index_params = dict(algorithm=1, trees=5)
        search_params = dict(checks=50)

        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(descriptor1, descriptor2, k=2)
        # Apply ratio test
        good_matches = []
        for m, n in matches:
            if m.distance < 0.7*n.distance:
                good_matches.append(m)
    elif method == 'BF':
        if descriptor1.dtype != np.float32:
            descriptor1 = descriptor1.astype(np.float32)
        if descriptor2.dtype != np.float32:
            descriptor2 = descriptor2.astype(np.float32)
        
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=crossCheck)
        matches = bf.match(descriptor1, descriptor2)
        good_matches = sorted(matches, key=lambda x: x.distance)
    else:
        raise ValueError("Unsupported matching method.")

    return good_matches
