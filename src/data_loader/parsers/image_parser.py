# src/data_loader/image_parser.py
import cv2
import numpy as np
from .base_loader import BaseLoader

class ImageParser(BaseLoader):
    """
    影像文件解析器，支持JPEG、PNG等格式。
    """

    def load_data(self, file_path: str) -> np.ndarray:
        """
        從影像文件加載圖像數據。

        參數:
        - file_path: str, 影像文件的路徑。

        返回:
        - np.ndarray, 加載的圖像數據。
        """
        image = cv2.imread(file_path)
        if image is None:
            raise FileNotFoundError(f"無法加載文件: {file_path}")
        return image

    def validate_data(self, data: np.ndarray) -> bool:
        """
        驗證加載的圖像數據是否有效。

        參數:
        - data: np.ndarray, 需要被驗證的圖像數據。

        返回:
        - bool, 圖像數據是否有效。
        """
        # 驗證數據維度和類型
        if data.ndim not in [2, 3]:  # 允許灰階圖像和彩色圖像
            return False
        return True

# 示範用法
if __name__ == "__main__":
    parser = ImageParser()
    file_path = "path/to/your/image.png"
    try:
        data = parser.load_data(file_path)
        if parser.validate_data(data):
            print("圖像加載並驗證成功")
        else:
            print("加載的圖像數據無效")
    except FileNotFoundError as e:
        print(e)
