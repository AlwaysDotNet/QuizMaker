from widgets.signwindow import SignInWindow
from sys import exit,argv
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(argv)
    sg = SignInWindow()
    sg.show()
    exit(app.exec())
