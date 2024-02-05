# src/data_loader/las_parser.py
import numpy as np
import laspy
from .base_loader import BaseLoader

class LASParser(BaseLoader):
    """
    LAS文件解析器，用於加載LAS格式的點雲數據。
    """

    def load_data(self, file_path: str) -> np.ndarray:
        """
        從LAS文件加載點雲數據。

        參數:
        - file_path: str, LAS文件的路徑。

        返回:
        - np.ndarray, 加載的點雲數據。
        """
        with laspy.open(file_path) as file:
            las = file.read()
            points = np.vstack((las.x, las.y, las.z)).transpose()
        return points

    def validate_data(self, data: np.ndarray) -> bool:
        """
        驗證加載的點雲數據是否有效。

        參數:
        - data: np.ndarray, 需要被驗證的點雲數據。

        返回:
        - bool, 點雲數據是否有效。
        """
        # 驗證數據維度和類型
        if data.ndim != 2 or data.shape[1] != 3:
            return False
        return True

# 示範用法
if __name__ == "__main__":
    parser = LASParser()
    file_path = "path/to/your/pointcloud.las"
    data = parser.load_data(file_path)
    if parser.validate_data(data):
        print("點雲數據加載並驗證成功")
    else:
        print("加載的點雲數據無效")
