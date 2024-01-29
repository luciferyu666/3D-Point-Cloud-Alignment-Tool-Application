import pytest
from modules.initial_alignment import InitialAlignment

def test_align():
    # 測試初步對齊功能
    initial_alignment = InitialAlignment()
    aligned = initial_alignment.align([], [])
    assert aligned is not None
