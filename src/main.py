import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from PyQt5.QtCore import QCoreApplication
import logging
import json

def load_app_config():
    """加載應用配置文件"""
    with open('app_config.json', 'r') as config_file:
        return json.load(config_file)

def setup_logging():
    """設定日誌配置"""
    with open('logging_config.json', 'r') as config_file:
        logging.config.dictConfig(json.load(config_file))
    logging.info('應用程式啟動')

def main():
    """應用程式入口函數"""
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    # 加載應用配置
    app_config = load_app_config()
    setup_logging()

    # 初始化主窗口
    main_window = MainWindow()
    main_window.show()

    # 設定應用程式退出時的清理動作
    app.aboutToQuit.connect(app_cleanup)

    sys.exit(app.exec_())

def app_cleanup():
    """應用程式清理函數"""
    logging.info('應用程式結束')

if __name__ == '__main__':
    main()
