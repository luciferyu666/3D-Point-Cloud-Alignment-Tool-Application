# src/result_display.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ResultDisplayUI:
    def __init__(self, root):
        self.root = root
        self.create_ui()

    def create_ui(self):
        """
        創建用戶界面元素。
        """
        self.root.title("結果展示界面")

        # 結果文本展示
        self.result_text = tk.StringVar()
        self.result_text.set("處理結果將顯示在這裡。")
        ttk.Label(self.root, textvariable=self.result_text).pack(padx=10, pady=10)

        # 圖像展示區域
        self.image_panel = ttk.Label(self.root)
        self.image_panel.pack(padx=10, pady=10)

    def update_result_text(self, text):
        """
        更新結果文本。
        """
        self.result_text.set(text)

    def display_image(self, image_path):
        """
        在界面上展示圖像。
        """
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_panel.config(image=photo)
        self.image_panel.image = photo  # 保持對photo的引用

if __name__ == "__main__":
    root = tk.Tk()
    app = ResultDisplayUI(root)
    
    # 更新結果文本和展示圖像作為示例
    app.update_result_text("這是一個示例文本。")
    app.display_image("path/to/your/image.png")
    
    root.mainloop()
