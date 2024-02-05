# src/logger.py
import logging
import os
from datetime import datetime

def setup_logger(name, log_file, level=logging.INFO):
    """
    配置和創建一個日誌記錄器。

    參數:
    - name: str, 記錄器名稱。
    - log_file: str, 日誌文件保存的路徑。
    - level: logging.Level, 日誌級別。

    返回:
    - logging.Logger, 配置好的記錄器實例。
    """
    # 創建記錄器，設置級別
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 創建一個文件處理器，寫入指定文件
    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = logging.FileHandler(log_file)
    
    # 創建一個控制台處理器，輸出到標準輸出
    console_handler = logging.StreamHandler()

    # 設置日誌格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 為記錄器添加處理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# 示範用法
if __name__ == "__main__":
    log_file_name = datetime.now().strftime('%Y-%m-%d') + '.log'
    logger = setup_logger('example_logger', os.path.join('logs', log_file_name))
    logger.info('這是一條INFO級別的日誌訊息')
    logger.error('這是一條ERROR級別的日誌訊息')
