import os

class FormatValidator:
    def __init__(self, filepath):
        self.filepath = filepath
        self.allowed_3d_formats = ['.ply', '.las']
        self.allowed_image_formats = ['.jpeg', '.jpg', '.png']
    
    def validate(self):
        file_extension = os.path.splitext(self.filepath)[1].lower()
        
        if file_extension in self.allowed_3d_formats:
            return self._validate_3d_format()
        elif file_extension in self.allowed_image_formats:
            return self._validate_image_format()
        else:
            print(f"不支持的文件格式: {file_extension}")
            return False
    
    def _validate_3d_format(self):
        # 在這裡添加針對3D點雲數據格式的驗證邏輯
        print("進行3D點雲格式驗證...")
        return True
    
    def _validate_image_format(self):
        # 在這裡添加針對圖像文件的驗證邏輯
        print("進行圖像格式驗證...")
        return True

# 使用示例
if __name__ == "__main__":
    validator = FormatValidator('example.ply')
    if validator.validate():
        print("文件格式驗證通過。")
    else:
        print("文件格式驗證失敗。")
