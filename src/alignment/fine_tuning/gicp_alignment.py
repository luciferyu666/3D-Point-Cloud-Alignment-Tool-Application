import open3d as o3d
import numpy as np

def gicp_alignment(source_pcd, target_pcd, max_correspondence_distance, init_transformation=np.eye(4)):
    """
    使用GICP算法進行點雲之間的對齊。

    參數:
    - source_pcd: 源點雲對象。
    - target_pcd: 目標點雲對象。
    - max_correspondence_distance: 最大對應點距離。
    - init_transformation: 初始變換矩陣。

    返回:
    - 對齊結果，包括變換矩陣等信息。
    """
    # 估計法線
    source_pcd.estimate_normals()
    target_pcd.estimate_normals()
    
    # 執行GICP對齊
    result = o3d.pipelines.registration.registration_generalized_icp(
        source_pcd, target_pcd, max_correspondence_distance, init_transformation,
        o3d.pipelines.registration.TransformationEstimationForGeneralizedICP(),
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000))
    
    return result

# 使用示例
if __name__ == "__main__":
    source_pcd = o3d.io.read_point_cloud("path_to_source_point_cloud.ply")  # 讀取源點雲
    target_pcd = o3d.io.read_point_cloud("path_to_target_point_cloud.ply")  # 讀取目標點雲
    
    # 定義GICP算法的參數
    max_correspondence_distance = 0.05  # 最大對應點距離
    init_transformation = np.eye(4)  # 初始變換矩陣
    
    # 執行GICP對齊
    gicp_result = gicp_alignment(source_pcd, target_pcd, max_correspondence_distance, init_transformation)
    
    print("GICP對齊完成")
    print("變換矩陣:")
    print(gicp_result.transformation)
    
    # 可視化對齊結果
    source_pcd.transform(gicp_result.transformation)
    o3d.visualization.draw_geometries([source_pcd, target_pcd], window_name="GICP Alignment Result")
