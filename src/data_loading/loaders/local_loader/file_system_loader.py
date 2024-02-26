def load_text_file(filepath):
    """從指定的文件路徑加載文本內容。"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件 {filepath} 未找到。")
        return None
    except Exception as e:
        print(f"讀取文件時發生錯誤: {e}")
        return None

def load_binary_file(filepath):
    """從指定的文件路徑加載二進制數據。"""
    try:
        with open(filepath, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件 {filepath} 未找到。")
        return None
    except Exception as e:
        print(f"讀取文件時發生錯誤: {e}")
        return None

# 使用示例
if __name__ == "__main__":
    text_data = load_text_file('path/to/your/textfile.txt')
    print(text_data)
    
    binary_data = load_binary_file('path/to/your/binaryfile.bin')
    print(binary_data)
