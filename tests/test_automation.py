import pytest
from modules.automation import Automation

def test_process():
    # 測試自動化處理功能
    automation = Automation()
    result = automation.process([])
    assert result is None or isinstance(result, list)
