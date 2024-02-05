# src/test_preprocess.py
import numpy as np
import open3d as o3d
from preprocess.preprocess_module import preprocess_point_cloud

def create_simulated_point_cloud():
    """
    生成模擬的點雲數據。
    """
    # 使用Open3D生成一個球形點雲作為模擬數據
    mesh = o3d.geometry.TriangleMesh.create_sphere(radius=1.0, resolution=20)
    pcd = mesh.sample_points_uniformly(number_of_points=1000)
    
    # 添加一些隨機噪聲
    noise = np.random.normal(0, 0.02, size=np.asarray(pcd.points).shape)
    pcd.points = o3d.utility.Vector3dVector(np.asarray(pcd.points) + noise)
    
    return pcd

def test_preprocess_point_cloud():
    """
    測試點雲預處理功能。
    """
    pcd = create_simulated_point_cloud()
    
    # 視覺化原始點雲
    print("顯示原始點雲")
    o3d.visualization.draw_geometries([pcd], window_name="Original Point Cloud")
    
    # 進行預處理
    voxel_size = 0.05  # 定義體素大小
    processed_pcd = preprocess_point_cloud(pcd, voxel_size)
    
    # 視覺化預處理後的點雲
    print("顯示預處理後的點雲")
    o3d.visualization.draw_geometries([processed_pcd], window_name="Processed Point Cloud")

if __name__ == "__main__":
    test_preprocess_point_cloud()
