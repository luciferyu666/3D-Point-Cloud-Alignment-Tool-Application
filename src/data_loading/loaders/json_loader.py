import json

def load_json(filename):
    """從文件中讀取JSON數據並轉換成Python對象。"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"文件 {filename} 不存在。")
        return None
    except json.JSONDecodeError:
        print(f"解析JSON文件 {filename} 時發生錯誤。")
        return None

# 使用示例
if __name__ == "__main__":
    filename = 'your_json_file.json'
    data = load_json(filename)
    print(data)
