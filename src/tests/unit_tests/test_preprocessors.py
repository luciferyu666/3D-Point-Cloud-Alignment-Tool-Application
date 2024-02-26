import unittest
from preprocessors import DataCleaner, DataFormatter

class TestDataPreprocessors(unittest.TestCase):
    def setUp(self):
        # 初始化預處理器實例
        self.cleaner = DataCleaner()
        self.formatter = DataFormatter()

    def test_data_cleaning(self):
        # 測試數據清洗功能
        dirty_data = ["NaN", "inf", "-inf", None, "正常數據"]
        expected_result = ["正常數據"]
        cleaned_data = self.cleaner.clean(dirty_data)
        self.assertEqual(cleaned_data, expected_result)

    def test_data_formatting(self):
        # 測試數據格式化功能
        raw_data = ["1", "2", "3"]
        expected_result = [1, 2, 3]
        formatted_data = self.formatter.format(raw_data)
        self.assertEqual(formatted_data, expected_result)

    def test_performance(self):
        # 測試預處理步驟的運行效率
        import time
        start_time = time.time()
        self.formatter.format(["1", "2", "3"] * 1000)  # 假設大量數據的處理
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 1)  # 假設1秒內完成為合格

    def test_noise_data_handling(self):
        # 測試異常值和噪聲數據處理
        noisy_data = [999, 1, 2, 3, 999]
        expected_result = [1, 2, 3]
        cleaned_data = self.cleaner.remove_noise(noisy_data)
        self.assertEqual(cleaned_data, expected_result)

if __name__ == '__main__':
    unittest.main()
