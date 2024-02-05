# src/test_data_output.py
import numpy as np
import open3d as o3d
from data_output.format_converters import convert_numpy_to_point_cloud, convert_numpy_to_image

def test_save_point_cloud():
    """
    測試保存點雲數據功能。
    """
    # 生成模擬點雲數據
    points = np.random.rand(100, 3) * 100
    point_cloud = convert_numpy_to_point_cloud(points)
    
    # 保存點雲到PLY文件
    o3d.io.write_point_cloud("output/test_point_cloud.ply", point_cloud)
    print("點雲數據已保存到 'output/test_point_cloud.ply'。")

def test_save_image():
    """
    測試保存圖像數據功能。
    """
    # 生成模擬圖像數據
    image_data = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
    image_path = "output/test_image.png"
    
    # 保存圖像數據到PNG文件
    convert_numpy_to_image(image_data, image_path)
    print(f"圖像數據已保存到 '{image_path}'。")

if __name__ == "__main__":
    test_save_point_cloud()
    test_save_image()
