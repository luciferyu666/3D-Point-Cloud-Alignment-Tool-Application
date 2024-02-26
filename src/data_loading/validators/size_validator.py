# path/filename: size_validator.py
import numpy as np

def validate_data_size(point_cloud, max_points):
    """
    驗證點雲數據大小。
    :param point_cloud: 點雲數據，假設為 NumPy 陣列。
    :param max_points: 允許的最大點數量。
    :return: 布林值，表示是否通過驗證。
    """
    return point_cloud.shape[0] <= max_points

def validate_resolution(point_cloud, min_resolution):
    """
    確認數據分辨率。
    :param point_cloud: 點雲數據，假設為 NumPy 陣列。
    :param min_resolution: 最小分辨率。
    :return: 布林值，表示是否通過驗證。
    """
    # 計算點與點之間的最小距離作為分辨率的近似值
    distances = np.sqrt(np.sum(np.diff(point_cloud, axis=0)**2, axis=1))
    return np.min(distances) >= min_resolution

def validate_range(point_cloud, min_range, max_range):
    """
    檢測數據區間和範圍。
    :param point_cloud: 點雲數據，假設為 NumPy 陣列。
    :param min_range: 最小範圍值。
    :param max_range: 最大範圍值。
    :return: 布林值，表示是否通過驗證。
    """
    return np.all(point_cloud >= min_range) and np.all(point_cloud <= max_range)

def validate_point_cloud(point_cloud, max_points, min_resolution, min_range, max_range):
    """
    綜合驗證點雲數據。
    :param point_cloud: 點雲數據，假設為 NumPy 陣列。
    :return: 驗證結果和錯誤消息。
    """
    if not validate_data_size(point_cloud, max_points):
        return False, "點雲數據大小超過上限。"
    if not validate_resolution(point_cloud, min_resolution):
        return False, "點雲數據分辨率不符合要求。"
    if not validate_range(point_cloud, min_range, max_range):
        return False, "點雲數據不在指定的範圍內。"
    return True, "點雲數據驗證成功。"

# 示例用法
if __name__ == '__main__':
    point_cloud_example = np.random.rand(1000, 3)  # 假設的點雲數據
    max_points = 5000
    min_resolution = 0.01
    min_range, max_range = 0, 1
    result, message = validate_point_cloud(point_cloud_example, max_points, min_resolution, min_range, max_range)
    print(message)
