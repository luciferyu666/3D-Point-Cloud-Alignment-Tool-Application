# src/alignment/__init__.py

# 導入點雲對齊模組內部的類和函數
from .initial_alignment import InitialAlignment
from .icp_alignment import ICPAlignment
from .utils import compute_transformation_matrix, apply_transformation

# 可以在這裡加入模組級別的初始化代碼，比如全局配置或預加載數據

# 對外暴露模組接口
__all__ = ['InitialAlignment', 'ICPAlignment', 'compute_transformation_matrix', 'apply_transformation']

#