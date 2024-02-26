from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QCheckBox

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("設置")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # 算法選擇
        self.algorithm_label = QLabel("選擇算法:")
        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItems(["算法A", "算法B", "算法C"])
        layout.addWidget(self.algorithm_label)
        layout.addWidget(self.algorithm_combo)

        # 性能優化
        self.performance_optimization_label = QLabel("性能優化選項:")
        self.multi_threading_checkbox = QCheckBox("啟用多線程")
        layout.addWidget(self.performance_optimization_label)
        layout.addWidget(self.multi_threading_checkbox)

        # 視覺化選項
        self.visualization_options_label = QLabel("視覺化選項:")
        self.color_scheme_combo = QComboBox()
        self.color_scheme_combo.addItems(["方案A", "方案B", "方案C"])
        layout.addWidget(self.visualization_options_label)
        layout.addWidget(self.color_scheme_combo)

        # 確認按鈕
        self.confirm_button = QPushButton("確認")
        self.confirm_button.clicked.connect(self.confirm_settings)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def confirm_settings(self):
        # 處理設置確認的邏輯
        algorithm = self.algorithm_combo.currentText()
        multi_threading = self.multi_threading_checkbox.isChecked()
        color_scheme = self.color_scheme_combo.currentText()
        print(f"選擇的算法: {algorithm}, 多線程: {multi_threading}, 視覺化方案: {color_scheme}")
        self.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dialog = SettingsDialog()
    if dialog.exec_():
        print("設置已確認")
    sys.exit(app.exec_())
