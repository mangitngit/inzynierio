from gui.main_window import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    sys.exit(app.exec_())
