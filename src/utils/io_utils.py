import json
import os

class IOUtils:
    @staticmethod
    def read_text_file(file_path):
        """讀取文本文件內容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"文件未找到: {file_path}")
            return None

    @staticmethod
    def write_text_file(file_path, content):
        """將內容寫入文本文件"""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def read_json_file(file_path):
        """讀取JSON格式的配置文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"文件未找到: {file_path}")
            return None

    @staticmethod
    def write_json_file(file_path, data):
        """將數據以JSON格式寫入文件"""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

# 示例使用
if __name__ == "__main__":
    # 讀取和寫入文本文件示例
    text_content = IOUtils.read_text_file('example.txt')
    print(text_content)
    IOUtils.write_text_file('example_new.txt', '這是一段新的文本內容。')

    # 讀取和寫入JSON文件示例
    config = IOUtils.read_json_file('config.json')
    print(config)
    IOUtils.write_json_file('config_new.json', {'key': 'value'})
