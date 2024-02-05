# src/alignment/point_cloud_aligner.py
import numpy as np
from .initial_alignment import perform_initial_alignment
from .icp_alignment import perform_icp

class PointCloudAligner:
    """
    點雲對齊類，結合初步對齊和ICP對齊實現點雲的精確匹配。
    """
    
    def __init__(self, threshold_icp=0.02):
        self.threshold_icp = threshold_icp  # ICP算法的距離閾值

    def align(self, source_points, target_points, source_features, target_features):
        """
        對齊兩個點雲。

        參數:
        - source_points: 源點雲的點坐標。
        - target_points: 目標點雲的點坐標。
        - source_features: 源點雲的特徵描述子。
        - target_features: 目標點雲的特徵描述子。

        返回:
        - 變換矩陣: 將源點雲對齊到目標點雲的變換矩陣。
        """
        # 初步對齊
        initial_alignment_result = perform_initial_alignment(
            source_points, target_points, source_features, target_features)
        initial_transformation = initial_alignment_result["transformation"]
        
        # ICP精確對齊
        icp_result = perform_icp(
            source_points, target_points,
            threshold=self.threshold_icp,
            init_transformation=initial_transformation)
        
        final_transformation = icp_result["transformation"]
        
        return final_transformation

# 示範用法
if __name__ == "__main__":
    # 假設已經有了源點雲和目標點雲的點坐標以及特徵描述子
    source_points = np.random.rand(100, 3)
    target_points = np.random.rand(100, 3)
    source_features = np.random.rand(33, 100)  # 假設特徵維度為33
    target_features = np.random.rand(33, 100)
    
    aligner = PointCloudAligner()
    transformation_matrix = aligner.align(source_points, target_points, source_features, target_features)
    print("變換矩陣:\n", transformation_matrix)
