import open3d as o3d
import numpy as np

def apply_global_optimization(pose_graph, max_correspondence_distance, preference_loop_closure):
    """
    進行全局優化以精細調整點雲間的對齊。

    參數:
    - pose_graph: 姿態圖，包含所有點雲的初始對齊信息。
    - max_correspondence_distance: 對齊中考慮的最大對應點距離。
    - preference_loop_closure: 關閉迴路的偏好設置，值越高表示對迴路閉合的偏好越高。

    返回:
    - 優化後的姿態圖。
    """
    option = o3d.pipelines.registration.GlobalOptimizationOption(
        max_correspondence_distance=max_correspondence_distance,
        edge_prune_threshold=0.25,
        reference_node=0)
    o3d.pipelines.registration.global_optimization(
        pose_graph,
        o3d.pipelines.registration.GlobalOptimizationLevenbergMarquardt(),
        o3d.pipelines.registration.GlobalOptimizationConvergenceCriteria(),
        option)
    return pose_graph

# 使用示例
if __name__ == "__main__":
    # 加載姿態圖，這裡假設已經創建了姿態圖並填充了所有初始對齊信息
    pose_graph = o3d.io.read_pose_graph("path_to_your_pose_graph.json")

    # 進行全局優化
    optimized_pose_graph = apply_global_optimization(pose_graph, 0.03, 2.0)

    # 優化後的姿態圖可以用於進一步的點雲融合或分析
    print("全局優化完成。")
