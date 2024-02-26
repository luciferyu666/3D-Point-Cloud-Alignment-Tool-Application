import tkinter as tk
from tkinter import ttk

class DropdownWidget(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('下拉選單小組件示例')
        self.geometry('300x200')

        # 定義下拉選單的選項
        options = ['選項1', '選項2', '選項3', '選項4']

        # 創建一個變量來存儲當前選擇的選項
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(options[0])  # 設置初始選擇的選項

        # 創建下拉選單
        self.dropdown = ttk.Combobox(self, textvariable=self.selected_option, values=options)
        self.dropdown.pack(pady=20)

        # 創建一個按鈕來展示當前選擇的選項
        self.show_selection_button = ttk.Button(self, text='顯示選擇', command=self.show_selection)
        self.show_selection_button.pack(pady=10)

    def show_selection(self):
        # 顯示當前選擇的選項
        tk.messagebox.showinfo('選擇的選項', f'您選擇了: {self.selected_option.get()}')

if __name__ == '__main__':
    app = DropdownWidget()
    app.mainloop()
