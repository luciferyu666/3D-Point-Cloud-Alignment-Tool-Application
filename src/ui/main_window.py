import tkinter as tk
from tkinter import filedialog, messagebox

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("3D點雲對齊工具")
        self.root.geometry("600x400")
        
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="加載數據", command=self.load_data)
        self.file_menu.add_command(label="保存結果", command=self.save_results)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=self.root.quit)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        
        self.root.config(menu=self.menu_bar)
        
        self.status_label = tk.Label(self.root, text="就緒", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        
    def load_data(self):
        filename = filedialog.askopenfilename(title="選擇點雲數據文件", filetypes=(("PLY files", "*.ply"), ("All files", "*.*")))
        if filename:
            # 在這裡加載和處理點雲數據
            self.update_status(f"加載數據：{filename}")
        
    def save_results(self):
        # 在這裡實現保存結果的功能
        self.update_status("結果已保存")
        
    def update_status(self, message):
        self.status_label.config(text=message)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
