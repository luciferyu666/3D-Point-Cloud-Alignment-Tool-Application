import tkinter as tk
from tkinter import ttk

def set_light_theme(root):
    """
    為 Tkinter 應用程式設置亮色主題。
    """
    # 定義亮色主題的顏色
    background_color = "#FFFFFF"
    text_color = "#000000"
    button_color = "#F0F0F0"
    entry_bg_color = "#FFFFFF"
    entry_fg_color = "black"

    # 應用背景顏色和文字顏色
    root.configure(bg=background_color)
    style = ttk.Style(root)
    style.configure('.', background=background_color, foreground=text_color)
    style.configure('TButton', background=button_color, foreground=text_color)
    style.configure('TEntry', fieldbackground=entry_bg_color, foreground=entry_fg_color)
    style.configure('TLabel', background=background_color, foreground=text_color)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('亮色主題示例')
    root.geometry('300x200')

    set_light_theme(root)

    # 創建標籤、按鈕和輸入框作為示例元素
    label = ttk.Label(root, text="這是一個標籤")
    label.pack(pady=10)

    entry = ttk.Entry(root)
    entry.pack(pady=10)

    button = ttk.Button(root, text="點擊我")
    button.pack(pady=10)

    root.mainloop()
