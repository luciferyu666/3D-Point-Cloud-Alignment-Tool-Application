import tkinter as tk
from tkinter import ttk

def set_dark_theme(root):
    """
    為 Tkinter 應用程式設置暗色主題。
    """
    # 定義暗色主題的顏色
    background_color = "#333333"
    text_color = "#FFFFFF"
    button_color = "#555555"
    entry_bg_color = "#555555"
    entry_fg_color = "white"

    # 應用背景顏色和文字顏色
    root.configure(bg=background_color)
    style = ttk.Style(root)
    style.configure('.', background=background_color, foreground=text_color)
    style.configure('TButton', background=button_color, foreground=text_color)
    style.configure('TEntry', fieldbackground=entry_bg_color, foreground=entry_fg_color)
    style.configure('TLabel', background=background_color, foreground=text_color)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('暗色主題示例')
    root.geometry('300x200')

    set_dark_theme(root)

    # 創建標籤、按鈕和輸入框作為示例元素
    label = ttk.Label(root, text="這是一個標籤")
    label.pack(pady=10)

    entry = ttk.Entry(root)
    entry.pack(pady=10)

    button = ttk.Button(root, text="點擊我")
    button.pack(pady=10)

    root.mainloop()
