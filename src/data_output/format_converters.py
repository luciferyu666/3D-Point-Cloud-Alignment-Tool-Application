# src/data_output/format_converters.py
import numpy as np
import open3d as o3d
from PIL import Image

def convert_numpy_to_point_cloud(points: np.ndarray) -> o3d.geometry.PointCloud:
    """
    將NumPy數組轉換為Open3D的點雲對象。

    參數:
    - points: np.ndarray, 點坐標數據，形狀為(N, 3)。

    返回:
    - o3d.geometry.PointCloud, Open3D點雲對象。
    """
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    return point_cloud

def convert_point_cloud_to_numpy(point_cloud: o3d.geometry.PointCloud) -> np.ndarray:
    """
    將Open3D的點雲對象轉換為NumPy數組。

    參數:
    - point_cloud: o3d.geometry.PointCloud, Open3D點雲對象。

    返回:
    - np.ndarray, 點坐標數據。
    """
    return np.asarray(point_cloud.points)

def convert_image_to_numpy(image_path: str) -> np.ndarray:
    """
    從文件讀取圖像並轉換為NumPy數組。

    參數:
    - image_path: str, 圖像文件的路徑。

    返回:
    - np.ndarray, 圖像數據。
    """
    image = Image.open(image_path)
    return np.array(image)

def convert_numpy_to_image(image_data: np.ndarray, image_path: str) -> None:
    """
    將NumPy數組保存為圖像文件。

    參數:
    - image_data: np.ndarray, 圖像數據。
    - image_path: str, 保存圖像的路徑。
    """
    image = Image.fromarray(image_data)
    image.save(image_path)

# 示範用法
if __name__ == "__main__":
    # NumPy數組轉點雲對象
    points = np.random.rand(100, 3)
    point_cloud = convert_numpy_to_point_cloud(points)
    print("NumPy數組轉Open3D點雲對象成功")

    # 點雲對象轉NumPy數組
    points_converted_back = convert_point_cloud_to_numpy(point_cloud)
    print("Open3D點雲對象轉NumPy數組成功")

    # 讀取圖像為NumPy數組
    image_data = convert_image_to_numpy('path/to/your/image.png')
    print("圖像讀取為NumPy數組成功")

    # 將NumPy數組保存為圖像
    convert_numpy_to_image(image_data, 'path/to/save/new_image.png')
    print("NumPy數組保存為圖像成功")
