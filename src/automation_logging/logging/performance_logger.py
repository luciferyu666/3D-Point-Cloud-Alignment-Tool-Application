import time
import psutil
import logging

# 初始化日誌記錄器
logging.basicConfig(filename='performance.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_performance(func):
    """
    裝飾器，用於記錄函數的性能數據。
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 開始時間
        result = func(*args, **kwargs)
        end_time = time.time()  # 結束時間
        duration = end_time - start_time
        memory_usage = psutil.Process().memory_info().rss / (1024 * 1024)  # MB
        cpu_percentage = psutil.cpu_percent()
        logging.info(f"函數 {func.__name__} 執行時間: {duration:.2f} 秒, 記憶體使用: {memory_usage:.2f} MB, CPU使用率: {cpu_percentage}%")
        return result
    return wrapper

@log_performance
def demo_function():
    """
    示範函數，模擬一個耗時操作。
    """
    time.sleep(2)  # 模擬耗時操作

if __name__ == '__main__':
    demo_function()
