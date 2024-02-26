import tkinter as tk
from tkinter import ttk

class ProgressBarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('進度條示例')
        self.geometry('400x150')

        # 任務信息
        self.task_label = tk.Label(self, text='當前任務：處理中...')
        self.task_label.pack(pady=10)

        # 進度條
        self.progress = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=10)
        
        # 錯誤和警告提示
        self.message_label = tk.Label(self, text='')
        self.message_label.pack(pady=5)

        # 更新進度條的按鈕
        self.update_button = tk.Button(self, text='更新進度', command=self.update_progress)
        self.update_button.pack(pady=10)

        # 中斷操作的按鈕
        self.cancel_button = tk.Button(self, text='中斷操作', command=self.cancel_operation)
        self.cancel_button.pack(pady=10)

        self.progress['value'] = 0

    def update_progress(self):
        if self.progress['value'] < 100:
            self.progress['value'] += 10
            self.message_label.config(text='')
        else:
            self.task_label.config(text='任務完成！')
            self.message_label.config(text='操作成功完成。')

    def cancel_operation(self):
        self.progress['value'] = 0
        self.task_label.config(text='當前任務：已中斷')
        self.message_label.config(text='操作已被用戶中斷。')

if __name__ == '__main__':
    app = ProgressBarApp()
    app.mainloop()
