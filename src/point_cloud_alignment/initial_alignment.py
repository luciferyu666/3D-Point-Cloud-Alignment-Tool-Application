import numpy as np
import open3d as o3d

def initial_alignment(source_point_cloud, target_point_cloud, transformation_matrix):
    source_point_cloud.transform(transformation_matrix)
    return source_point_cloud

def compute_initial_transformation(rvec, tvec):
    # Convert rotation vector to rotation matrix
    R, _ = cv2.Rodrigues(rvec)
    T = np.array(tvec).reshape(3, 1)
    # Create a 4x4 transformation matrix
    transformation_matrix = np.hstack((R, T))
    transformation_matrix = np.vstack((transformation_matrix, [0, 0, 0, 1]))
    return transformation_matrix
