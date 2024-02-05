# src/file_operations.py
import tkinter as tk
from tkinter import filedialog

class FileOperationsUI:
    def __init__(self, root):
        self.root = root
        self.create_ui()

    def create_ui(self):
        """
        創建用戶界面元素。
        """
        self.root.title("文件操作界面")
        
        # 打開文件按鈕
        self.open_button = tk.Button(self.root, text="打開文件", command=self.open_file)
        self.open_button.pack(pady=5)
        
        # 保存文件按鈕
        self.save_button = tk.Button(self.root, text="保存文件", command=self.save_file)
        self.save_button.pack(pady=5)

    def open_file(self):
        """
        打開文件對話框並讀取文件。
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            print(f"選擇的文件: {file_path}")
            # 在這裡添加讀取和處理文件的代碼

    def save_file(self):
        """
        打開保存文件對話框並保存文件。
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            print(f"文件將被保存在: {file_path}")
            # 在這裡添加保存文件到指定路徑的代碼

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOperationsUI(root)
    root.mainloop()
