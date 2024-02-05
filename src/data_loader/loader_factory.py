# src/data_loader/loader_factory.py

class LoaderFactory:
    """
    工廠類，用於根據文件格式動態創建對應的讀取器實例。
    """
    _loaders = {}

    @classmethod
    def register_loader(cls, file_format, loader_class):
        """
        註冊一個新的讀取器類到工廠。
        
        :param file_format: 文件格式 (如 'ply', 'las', 'jpg')
        :param loader_class: 該文件格式對應的讀取器類
        """
        cls._loaders[file_format] = loader_class

    @classmethod
    def get_loader(cls, file_format):
        """
        根據文件格式獲取對應的讀取器類的實例。
        
        :param file_format: 文件格式
        :return: 對應文件格式的讀取器類的實例
        :raises KeyError: 如果沒有找到對應的讀取器類
        """
        if file_format not in cls._loaders:
            raise KeyError(f"No loader registered for format: {file_format}")
        loader_class = cls._loaders[file_format]
        return loader_class

    @classmethod
    def reset_registry(cls):
        """
        重置註冊表，用於初始化或測試。
        """
        cls._loaders.clear()
