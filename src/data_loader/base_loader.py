# src/data_loader/base_loader.py

from abc import ABC, abstractmethod
import numpy as np

class BaseLoader(ABC):
    """
    所有讀取器類的基礎接口。
    定義了讀取數據的基本方法和屬性。
    """

    @abstractmethod
    def load_data(self, file_path: str) -> np.ndarray:
        """
        從給定的文件路徑加載數據。

        參數:
        - file_path: str, 數據文件的路徑。

        返回:
        - np.ndarray, 加載的數據。
        
        此方法必須被所有子類實現。
        """
        pass

    @abstractmethod
    def validate_data(self, data: np.ndarray) -> bool:
        """
        驗證加載的數據是否有效。

        參數:
        - data: np.ndarray, 需要被驗證的數據。

        返回:
        - bool, 數據是否有效。

        此方法必須被所有子類實現。
        """
        pass
