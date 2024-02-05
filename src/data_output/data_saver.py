# src/data_saver.py
import numpy as np
import open3d as o3d
from PIL import Image

def save_point_cloud(points: np.ndarray, file_path: str, format: str = 'ply') -> None:
    """
    將點雲數據保存到文件中。

    參數:
    - points: np.ndarray, 點雲的點坐標。
    - file_path: str, 保存文件的路徑。
    - format: str, 文件格式，默認為'ply'。
    """
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    if format.lower() == 'ply':
        o3d.io.write_point_cloud(file_path, point_cloud)
    else:
        raise ValueError(f"不支持的文件格式: {format}")

def save_image(image: np.ndarray, file_path: str) -> None:
    """
    將圖像數據保存到文件中。

    參數:
    - image: np.ndarray, 圖像數據。
    - file_path: str, 保存文件的路徑。
    """
    image = Image.fromarray(image)
    image.save(file_path)

# 示範用法
if __name__ == "__main__":
    # 保存點雲數據
    points = np.random.rand(100, 3)
    save_point_cloud(points, 'test_point_cloud.ply')

    # 保存圖像數據
    image_data = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
    save_image(image_data, 'test_image.png')
