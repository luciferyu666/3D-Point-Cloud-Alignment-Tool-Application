import tkinter as tk
from tkinter import filedialog, messagebox
# 假設已經有這些模組完成了相應的功能
from data_preprocessing.read_image import read_image
from data_preprocessing.read_point_cloud import read_point_cloud_ply
from point_cloud_alignment.icp_alignment import precise_alignment
# 其他必要的導入...

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 設定用戶介面元件
        self.load_image_btn = tk.Button(self, text="讀取影像", command=self.load_image)
        self.load_image_btn.pack(side="top")

        self.load_pcd_btn = tk.Button(self, text="讀取3D點雲數據", command=self.load_point_cloud)
        self.load_pcd_btn.pack(side="top")

        self.align_pcd_btn = tk.Button(self, text="執行對齊", command=self.align_point_cloud)
        self.align_pcd_btn.pack(side="top")

        self.quit_btn = tk.Button(self, text="退出", command=self.master.destroy)
        self.quit_btn.pack(side="bottom")

    def load_image(self):
        # 讀取影像
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            # 在這裡調用讀取影像的函數
            image_data = read_image(file_path)
            messagebox.showinfo("信息", "影像讀取成功!")

    def load_point_cloud(self):
        # 讀取3D點雲數據
        file_path = filedialog.askopenfilename(filetypes=[("PLY files", "*.ply")])
        if file_path:
            # 在這裡調用讀取點雲的函數
            pcd_data = read_point_cloud_ply(file_path)
            messagebox.showinfo("信息", "3D點雲數據讀取成功!")

    def align_point_cloud(self):
        # 執行點雲對齊
        # 假設已經有點雲數據載入和準備好了對齊的相關數據
        # 在這裡調用點雲對齊的核心處理函數
        result = precise_alignment()
        messagebox.showinfo("信息", "點雲對齊完成!")

# 用於啟動應用程式的函數
def run_app():
    root = tk.Tk()
    app = MainApplication(master=root)
    app.mainloop()

if __name__ == "__main__":
    run_app()
