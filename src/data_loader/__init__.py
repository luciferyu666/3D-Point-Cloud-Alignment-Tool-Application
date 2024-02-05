# src/data_loader/__init__.py

from .loader_factory import LoaderFactory
from .config.loader_config import LOADER_MAPPING
from .base_loader import BaseLoader
from .parsers.ply_parser import PLYParser
from .parsers.las_parser import LASParser
from .parsers.image_parser import ImageParser

def initialize_loaders():
    """
    初始化並註冊所有支持的讀取器類。
    """
    # 確保LoaderFactory清空先前的註冊
    LoaderFactory.reset_registry()

    # 從配置中讀取並註冊所有讀取器
    for file_format, loader_class in LOADER_MAPPING.items():
        LoaderFactory.register_loader(file_format, loader_class)

def get_loader(file_format):
    """
    根據文件格式獲取對應的讀取器實例。
    :param file_format: 文件格式 (如 'ply', 'las', 'jpg')
    :return: 對應文件格式的讀取器實例
    """
    try:
        loader = LoaderFactory.get_loader(file_format)
        return loader()
    except KeyError:
        raise ValueError(f"Unsupported file format: {file_format}")

# 在模組加載時初始化讀取器
initialize_loaders()

#