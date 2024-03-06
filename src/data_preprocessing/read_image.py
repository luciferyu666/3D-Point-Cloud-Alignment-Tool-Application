from PIL import Image
import numpy as np

def read_image(image_path):
    """
    讀取JPEG或PNG格式的RGB影像。

    參數:
        image_path (str): 影像文件的路徑。

    返回:
        numpy.ndarray: 影像數據，格式為(height, width, channels)。
    """
    image = Image.open(image_path)
    image_np = np.array(image)
    return image_np
