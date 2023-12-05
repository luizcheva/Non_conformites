import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindows

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()

    window.show()
    app.exec()
