import logging

# 配置日誌記錄器
logging.basicConfig(filename='process_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class ErrorHandler:
    def log_error(self, error):
        """
        將錯誤記錄到日誌文件。
        """
        logging.error(str(error))

    def notify_user(self, error):
        """
        向用戶提供錯誤通知。
        """
        print(f"發生錯誤: {error}")

    def handle_error(self, function, *args, **kwargs):
        """
        執行函數並處理可能的錯誤。
        """
        try:
            return function(*args, **kwargs)
        except Exception as e:
            self.log_error(e)
            self.notify_user(e)
            # 根據錯誤類型實施不同的處理策略
            # 這裡可以根據需要添加更複雜的錯誤處理邏輯

# 使用示例
def risky_function(x):
    if x < 0:
        raise ValueError("x 不能小於 0")
    return x * 2

if __name__ == "__main__":
    handler = ErrorHandler()
    result = handler.handle_error(risky_function, -1)
    print("處理結果:", result)
