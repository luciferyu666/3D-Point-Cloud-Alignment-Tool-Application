# src/test_ui.py
import tkinter as tk
from tkinter import messagebox

def create_simple_ui():
    """
    創建一個包含一個按鈕的簡單用戶界面，點擊按鈕時顯示一個消息框。
    """
    root = tk.Tk()
    root.title("UI 測試")
    
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    greet_button = tk.Button(frame, text="點擊我", command=lambda: messagebox.showinfo("測試", "你好，這是一個測試消息！"))
    greet_button.pack()

    return root

def test_ui():
    """
    啟動用戶界面並等待用戶操作。
    """
    ui = create_simple_ui()
    ui.mainloop()

if __name__ == "__main__":
    test_ui()
