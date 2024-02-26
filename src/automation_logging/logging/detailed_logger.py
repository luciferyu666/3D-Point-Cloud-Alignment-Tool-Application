import logging
import time

# 初始化日誌記錄器
def setup_detailed_logger(log_file_name):
    logger = logging.getLogger('DetailedLogger')
    logger.setLevel(logging.DEBUG)  # 設置日誌級別

    # 創建文件處理器，寫入指定文件
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.DEBUG)

    # 創建控制台處理器，輸出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 定義日誌格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加處理器到日誌記錄器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# 使用日誌記錄器
def demo_process(logger):
    logger.info("開始執行處理流程")
    try:
        # 模擬一些處理過程
        logger.debug("處理細節：執行某個步驟")
        time.sleep(1)  # 模擬耗時操作
        logger.debug("處理細節：執行另一個步驟")
        # 模擬一個錯誤
        raise ValueError("模擬一個錯誤發生")
    except Exception as e:
        logger.error(f"錯誤發生：{e}")
    finally:
        logger.info("處理流程結束")

if __name__ == '__main__':
    detailed_logger = setup_detailed_logger('detailed_processing.log')
    demo_process(detailed_logger)
