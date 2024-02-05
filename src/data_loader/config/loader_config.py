# src/data_loader/loader_config.py

# 導入不同格式的解析器類
from .ply_parser import PLYParser
from .las_parser import LASParser
from .image_parser import ImageParser

# 定義支持的文件格式和對應的讀取器類
LOADER_MAPPING = {
    'ply': PLYParser,
    'las': LASParser,
    'jpg': ImageParser,
    'jpeg': ImageParser,
    'png': ImageParser
}

def get_loader_for_format(file_format: str):
    """
    根據文件格式獲取對應的讀取器類。

    參數:
    - file_format: str, 文件格式。

    返回:
    - 對應的讀取器類，如果不支持給定的格式則返回None。
    """
    loader_class = LOADER_MAPPING.get(file_format.lower())
    return loader_class
