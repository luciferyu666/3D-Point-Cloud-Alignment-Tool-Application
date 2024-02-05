# src/parameter_configuration.py
import tkinter as tk
from tkinter import ttk

class ParameterConfigurationUI:
    def __init__(self, root):
        self.root = root
        self.create_ui()

    def create_ui(self):
        """
        創建用戶界面元素。
        """
        self.root.title("參數配置界面")

        # 配置參數標籤和輸入框
        ttk.Label(self.root, text="參數1:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.param1_entry = ttk.Entry(self.root)
        self.param1_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(self.root, text="參數2:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.param2_entry = ttk.Entry(self.root)
        self.param2_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        # 保存按鈕
        self.save_button = ttk.Button(self.root, text="保存設定", command=self.save_settings)
        self.save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_settings(self):
        """
        保存設定到文件或處理設定。
        """
        param1 = self.param1_entry.get()
        param2 = self.param2_entry.get()
        print(f"保存的參數設定: 參數1={param1}, 參數2={param2}")
        # 在這裡實現保存設定的邏輯，比如寫入到文件或更新應用設定

if __name__ == "__main__":
    root = tk.Tk()
    app = ParameterConfigurationUI(root)
    root.mainloop()
