# src/utils.py
import os
import json

def ensure_dir(directory):
    """
    確保指定的目錄存在，如果不存在則創建它。
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_json(data, file_path):
    """
    將字典數據保存到JSON文件。
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(file_path):
    """
    從JSON文件加載數據。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def format_size(bytes):
    """
    格式化文件大小。
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}"
        bytes /= 1024
    return f"{bytes:.2f}PB"

# 示範用法
if __name__ == "__main__":
    # 確保目錄存在
    ensure_dir("output")

    # 保存和加載JSON數據
    data = {"name": "Alice", "age": 30}
    save_json(data, "output/data.json")
    loaded_data = load_json("output/data.json")
    print(loaded_data)

    # 格式化文件大小
    print(format_size(1024))  # 1.00KB
    print(format_size(123456789))  # 117.74MB
