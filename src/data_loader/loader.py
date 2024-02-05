# src/data_loader/loader.py
import numpy as np
import open3d as o3d
from .base_loader import BaseLoader

class PLYLoader(BaseLoader):
    """
    PLY格式的點雲數據加載器。
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
        np_points = np.asarray(ply.points)  # 轉換為NumPy數組
        return np_points

    def validate_data(self, data: np.ndarray) -> bool:
        """
        驗證加載的數據是否為有效的點雲數據。

        參數:
        - data: np.ndarray, 需要被驗證的數據。

        返回:
        - bool, 點雲數據是否有效。
        """
        # 驗證數據維度和類型
        if data.ndim != 2 or data.shape[1] != 3:
            return False
        return True

# 示範用法
if __name__ == "__main__":
    loader = PLYLoader()
    file_path = "path/to/your/pointcloud.ply"
    data = loader.load_data(file_path)
    if loader.validate_data(data):
        print("數據加載並驗證成功")
    else:
        print("加載的數據無效")
