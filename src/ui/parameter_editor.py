import tkinter as tk
from tkinter import ttk

class ParameterEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('參數編輯器')
        self.geometry('400x300')

        # 創建Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # 基本設置Tab
        self.basic_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.basic_frame, text='基本設置')
        self.create_basic_settings(self.basic_frame)

        # 進階設置Tab
        self.advanced_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.advanced_frame, text='進階設置')
        self.create_advanced_settings(self.advanced_frame)

    def create_basic_settings(self, frame):
        # 算法選擇
        ttk.Label(frame, text='選擇算法:').pack()
        self.algorithm_var = tk.StringVar()
        algorithms = ttk.Combobox(frame, textvariable=self.algorithm_var, values=['ICP', 'GICP', '其他'])
        algorithms.pack()

        # 性能優化
        ttk.Label(frame, text='啟用多線程:').pack()
        self.multithreading_var = tk.BooleanVar()
        multithreading_check = ttk.Checkbutton(frame, text='是', variable=self.multithreading_var, onvalue=True, offvalue=False)
        multithreading_check.pack()

    def create_advanced_settings(self, frame):
        # 視覺化選項
        ttk.Label(frame, text='點大小:').pack()
        self.point_size_var = tk.DoubleVar()
        point_size_slider = ttk.Scale(frame, from_=1, to=10, variable=self.point_size_var)
        point_size_slider.pack()

        # 輸出格式
        ttk.Label(frame, text='輸出格式:').pack()
        self.output_format_var = tk.StringVar()
        output_format = ttk.Combobox(frame, textvariable=self.output_format_var, values=['PLY', 'LAS', '其他'])
        output_format.pack()

        # 保存按鈕
        save_button = ttk.Button(frame, text='保存設置', command=self.save_settings)
        save_button.pack()

    def save_settings(self):
        settings = {
            'algorithm': self.algorithm_var.get(),
            'multithreading': self.multithreading_var.get(),
            'point_size': self.point_size_var.get(),
            'output_format': self.output_format_var.get()
        }
        print("設置已保存:", settings)
        # 實際應用中，這裡可以將設置保存到文件或進行其他處理

if __name__ == "__main__":
    app = ParameterEditor()
    app.mainloop()
