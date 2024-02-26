import unittest
import time
from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
from point_cloud_aligner import PointCloudAligner
from result_exporter import ResultExporter

class TestDataPipeline(unittest.TestCase):
    def setUp(self):
        # 初始化所需的組件
        self.loader = DataLoader()
        self.preprocessor = DataPreprocessor()
        self.aligner = PointCloudAligner()
        self.exporter = ResultExporter()
    
    def test_data_pipeline(self):
        start_time = time.time()
        # 步驟1: 加載數據
        data = self.loader.load_data("path/to/data")
        # 步驟2: 數據預處理
        preprocessed_data = self.preprocessor.preprocess(data)
        # 步驟3: 點雲對齊
        aligned_data = self.aligner.align(preprocessed_data)
        # 步驟4: 結果輸出
        self.exporter.export(aligned_data, "path/to/exported_data")
        end_time = time.time()
        
        # 效能評估
        processing_time = end_time - start_time
        print(f"數據處理總耗時: {processing_time} 秒")
        
        # 結果驗證（這裡需要根據實際情況來實現具體的驗證邏輯）
        self.assertTrue(self.validate_results(aligned_data), "對齊結果不符合預期")
        
    def validate_results(self, results):
        # 實現對齊結果的驗證邏輯
        # 這裡僅為示例，具體實現需根據應用需求定制
        return True

if __name__ == "__main__":
    unittest.main()
