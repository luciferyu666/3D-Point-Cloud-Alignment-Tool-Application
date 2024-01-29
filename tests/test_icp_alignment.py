import pytest
from modules.icp_alignment import ICPAlignment

def test_refine_alignment():
    # 測試ICP精確對齊功能
    icp_alignment = ICPAlignment()
    refined = icp_alignment.refine_alignment([])
    assert refined is not None
