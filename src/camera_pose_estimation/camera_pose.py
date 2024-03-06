import cv2
import numpy as np

def estimate_camera_pose(keypoints1, keypoints2, matches, camera_matrix, dist_coeffs=np.zeros((4, 1))):
    # Convert keypoints to the format required by cv2.solvePnPRansac
    points1 = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    points2 = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Find the 3D points of the keypoints in the world coordinate system
    _, rvec, tvec, inliers = cv2.solvePnPRansac(points1, points2, camera_matrix, dist_coeffs)

    return rvec, tvec, inliers

def draw_camera_pose(image, camera_matrix, rvec, tvec):
    # Draw the projected axis on the image
    axis = np.float32([[4,0,0], [0,4,0], [0,0,-4]]).reshape(-1,3)
    imgpts, jac = cv2.projectPoints(axis, rvec, tvec, camera_matrix, np.zeros((4, 1)))

    corner = tuple(imgpts[0].ravel())
    image = cv2.line(image, corner, tuple(imgpts[1].ravel()), (255,0,0), 5)
    image = cv2.line(image, corner, tuple(imgpts[2].ravel()), (0,255,0), 5)
    image = cv2.line(image, corner, tuple(imgpts[3].ravel()), (0,0,255), 5)

    return image
