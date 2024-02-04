import pytest
from modules.data_loader import DataLoader

def test_load_data():
    # 測試數據加載功能
    data_loader = DataLoader()
    images, point_clouds = data_loader.load_data()
    assert images is not None
    assert point_clouds is not None
