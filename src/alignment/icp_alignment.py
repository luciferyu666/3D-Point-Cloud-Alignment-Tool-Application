import open3d as o3d
import numpy as np

def icp_alignment(source_pcd, target_pcd, threshold, trans_init=np.eye(4)):
    """
    使用ICP算法進行點雲之間的精確對齊。

    參數:
    - source_pcd: 源點雲對象。
    - target_pcd: 目標點雲對象。
    - threshold: 對齊時考慮的最大距離閾值。
    - trans_init: 初始變換矩陣。

    返回:
    - icp_result: ICP算法的結果，包含變換矩陣等信息。
    """
    icp_result = o3d.pipelines.registration.registration_icp(
        source_pcd, target_pcd, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint())
    return icp_result

# 使用示例
if __name__ == "__main__":
    source_pcd = o3d.io.read_point_cloud("path_to_your_source_point_cloud.ply")  # 讀取源點雲
    target_pcd = o3d.io.read_point_cloud("path_to_your_target_point_cloud.ply")  # 讀取目標點雲
    
    # 定義ICP算法的參數
    threshold = 0.02  # 最大距離閾值
    trans_init = np.eye(4)  # 初始變換矩陣
    
    # 執行ICP對齊
    icp_result = icp_alignment(source_pcd, target_pcd, threshold, trans_init)
    
    print("ICP對齊完成")
    print("變換矩陣:")
    print(icp_result.transformation)
    
    # 可視化對齊結果
    source_pcd.transform(icp_result.transformation)
    o3d.visualization.draw_geometries([source_pcd, target_pcd], window_name="ICP Alignment Result")
