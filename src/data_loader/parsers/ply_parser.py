# src/data_loader/ply_parser.py
import numpy as np
import open3d as o3d
from .base_loader import BaseLoader

class PLYParser(BaseLoader):
    """
    PLY文件解析器，用於加載PLY格式的點雲數據。
    """

    def load_data(self, file_path: str) -> np.ndarray:
        """
        從PLY文件加載點雲數據。

        參數:
        - file_path: str, PLY文件的路徑。

        返回:
        - np.ndarray, 加載的點雲數據。
        """
        ply = o3d.io.read_point_cloud(file_path)  # 使用Open3D讀取PLY文件
        points = np.asarray(ply.points)  # 轉換點雲到NumPy數組
        return points

    def validate_data(self, data: np.ndarray) -> bool:
        """
        驗證加載的點雲數據是否有效。

        參數:
        - data: np.ndarray, 需要被驗證的點雲數據。

        返回:
        - bool, 點雲數據是否有效。
        """
        if data.ndim != 2 or data.shape[1] != 3:
            return False
        return True

# 示範用法
if __name__ == "__main__":
    parser = PLYParser()
    file_path = "path/to/your/pointcloud.ply"
    data = parser.load_data(file_path)
    if parser.validate_data(data):
        print("點雲數據加載並驗證成功")
    else:
        print("加載的點雲數據無效")
