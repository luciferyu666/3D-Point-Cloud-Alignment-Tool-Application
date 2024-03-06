import tkinter as tk
from user_interface.ui_module import MainApplication

def main():
    """
    主應用程式入口。
    初始化並運行用戶介面。
    """
    root = tk.Tk()
    root.geometry("800x600")  # 設定窗口大小
    root.title("3D點雲對齊工具應用程式")  # 設定窗口標題

    # 初始化應用程式並將其與根窗口關聯
    app = MainApplication(master=root)

    # 進入事件循環
    app.mainloop()

if __name__ == "__main__":
    main()
