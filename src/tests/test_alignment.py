# src/test_alignment.py
import numpy as np
import open3d as o3d
from preprocess.preprocess_module import preprocess_point_cloud
from alignment.initial_alignment import perform_initial_alignment
from alignment.icp_alignment import perform_icp
from alignment.utils import apply_transformation

def create_simulated_point_cloud():
    """
    創建模擬的點雲數據用於測試。
    """
    mesh = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)
    mesh.compute_vertex_normals()
    point_cloud = mesh.sample_points_poisson_disk(number_of_points=1000)
    return point_cloud

def test_point_cloud_alignment():
    """
    測試點雲對齊功能。
    """
    # 創建模擬的源點雲和目標點雲
    source = create_simulated_point_cloud()
    target = source.translate((0.1, 0.2, 0.3), relative=False)
    
    # 預處理點雲
    source_processed = preprocess_point_cloud(source, voxel_size=0.05)
    target_processed = preprocess_point_cloud(target, voxel_size=0.05)
    
    # 初步對齊（這裡省略了特徵提取和匹配的步驟，直接使用模擬數據）
    # 假設初步對齊結果
    initial_transformation = np.eye(4)
    
    # ICP精確對齊
    icp_result = perform_icp(source_processed, target_processed, initial_transformation, threshold=0.02)
    print("ICP對齊變換矩陣:\n", icp_result["transformation"])
    
    # 應用變換，並可視化對齊結果
    source_aligned = apply_transformation(np.asarray(source_processed.points), icp_result["transformation"])
    source_aligned_pc = o3d.geometry.PointCloud()
    source_aligned_pc.points = o3d.utility.Vector3dVector(source_aligned)
    
    o3d.visualization.draw_geometries([source_aligned_pc, target_processed], window_name="Alignment Result")

if __name__ == "__main__":
    test_point_cloud_alignment()

#