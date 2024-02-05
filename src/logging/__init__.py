# src/logging/__init__.py

# 導入日誌系統配置和實現的類和函數
from .logger import setup_logger

# 配置預設的日誌記錄器
default_log_file = 'application.log'
default_logger = setup_logger('default_logger', default_log_file)

# 可以在這裡加入模組級別的初始化代碼，比如全局日誌配置

# 對外暴露模組接口
__all__ = ['setup_logger', 'default_logger']

#