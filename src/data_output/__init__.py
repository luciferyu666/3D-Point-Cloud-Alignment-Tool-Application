# src/data_output/__init__.py

# 導入數據輸出模組內部的類和函數
from .data_saver import save_point_cloud, save_image

# 可以在這裡加入模組級別的初始化代碼，比如全局配置或預加載數據

# 對外暴露模組接口
__all__ = ['save_point_cloud', 'save_image']
