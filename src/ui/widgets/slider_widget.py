import tkinter as tk
from tkinter import ttk

class SliderWidget(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('滑桿小組件示例')
        self.geometry('400x200')

        # 創建一個滑桿
        self.slider = ttk.Scale(self, from_=0, to=100, orient='horizontal', command=self.on_slide)
        self.slider.pack(pady=20)

        # 顯示滑桿數值的標籤
        self.value_label = ttk.Label(self, text='滑桿數值: 0')
        self.value_label.pack()

    def on_slide(self, value):
        # 更新標籤以顯示當前滑桿數值
        self.value_label.config(text=f'滑桿數值: {int(float(value))}')

if __name__ == '__main__':
    app = SliderWidget()
    app.mainloop()
