# src/ui/main_window.py
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('就緒')
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('3D點雲對齊工具')

        # 菜單欄設置
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        
        # 添加打開文件動作
        openAction = QAction('打開', self)
        openAction.triggered.connect(self.openFileDialog)
        fileMenu.addAction(openAction)

        # 狀態欄
        self.statusLabel = QLabel('就緒')
        self.statusBar().addPermanentWidget(self.statusLabel)

    def openFileDialog(self):
        # 打開文件選擇對話框
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "選擇點雲文件", "",
                                                  "點雲文件 (*.ply *.pcd *.las);;所有文件 (*)", options=options)
        if fileName:
            self.statusLabel.setText(f'選擇的文件：{fileName}')
            # 處理文件...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
