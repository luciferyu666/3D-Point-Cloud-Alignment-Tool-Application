import logging
import time

# 設置日誌記錄器
def setup_logger(log_file):
    logger = logging.getLogger('PointCloudLog')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

# 示例函數，模擬點雲處理步驟
def process_point_cloud(logger):
    logger.info("開始處理點雲數據")
    
    # 模擬處理步驟
    try:
        logger.info("進行點雲下採樣")
        time.sleep(1)  # 模擬處理時間
        logger.info("點雲下採樣完成")
        
        logger.info("進行特徵提取")
        time.sleep(2)  # 模擬處理時間
        logger.info("特徵提取完成")

        # 模擬一個錯誤
        raise ValueError("特徵匹配過程中出現錯誤")

        logger.info("進行點雲對齊")
        time.sleep(1)  # 模擬處理時間
        logger.info("點雲對齊完成")
        
    except Exception as e:
        logger.error(f"處理過程中發生錯誤: {e}")

    logger.info("點雲處理流程結束")

# 使用示例
if __name__ == "__main__":
    logger = setup_logger("point_cloud_processing.log")
    process_point_cloud(logger)
