import open3d as o3d

def precise_alignment(source_point_cloud, target_point_cloud, threshold=0.02, max_iteration=2000):
    # Convert numpy arrays to Open3D point clouds
    source = o3d.geometry.PointCloud()
    target = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(source_point_cloud)
    target.points = o3d.utility.Vector3dVector(target_point_cloud)

    # Apply ICP alignment
    icp_result = o3d.registration.registration_icp(
        source, target, threshold, np.eye(4),
        o3d.registration.TransformationEstimationPointToPoint(),
        o3d.registration.ICPConvergenceCriteria(max_iteration=max_iteration))

    return icp_result.transformation
