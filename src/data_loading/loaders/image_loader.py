from PIL import Image
import numpy as np

def load_image(image_path):
    """從文件中讀取圖像，並將其轉換為NumPy數組。"""
    with Image.open(image_path) as img:
        img_array = np.array(img)
        return img_array

def resize_image(image_array, size=(224, 224)):
    """調整圖像尺寸。"""
    img = Image.fromarray(image_array)
    resized_img = img.resize(size)
    resized_img_array = np.array(resized_img)
    return resized_img_array

def convert_color_space(image_array, color_space="RGB"):
    """轉換圖像的顏色空間。"""
    img = Image.fromarray(image_array).convert(color_space)
    converted_img_array = np.array(img)
    return converted_img_array

# 使用示例
image_path = 'path_to_your_image.jpg'  # 圖像文件路徑
image_array = load_image(image_path)   # 載入圖像
resized_image_array = resize_image(image_array)  # 調整圖像尺寸
converted_image_array = convert_color_space(resized_image_array)  # 轉換顏色空間

