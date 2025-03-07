from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QApplication
import sys

from praktika.Medical_records.app.adminWin import AdminWin
from praktika.Medical_records.app.userWin import UserWin


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вход в систему')
        self.resize(300, 400)
        self.setStyleSheet("background-color: #057D9F;")

        self.setWindowIcon(QIcon('resources/logo99'))
        wid = QWidget()
        self.setCentralWidget(wid)
        self.admin_win_btn = QPushButton('Войти как администратор')
        self.admin_win_btn.setStyleSheet("background-color: white; color: black;")

        self.user_win_btn = QPushButton('Войти как гость')
        self.user_win_btn.setStyleSheet("background-color: white; color: black;")

        main_vl = QVBoxLayout()
        main_vl.addStretch()
        main_vl.addWidget(self.admin_win_btn)
        main_vl.addWidget(self.user_win_btn)
        main_vl.addStretch()
        wid.setLayout(main_vl)
        self.admin_win_btn.clicked.connect(self.show_admin_win)
        self.user_win_btn.clicked.connect(self.show_user_win)

    def show_admin_win(self):
        self.win_v = AdminWin()
        self.win_v.show()

    def show_user_win(self):
        self.win_a = UserWin()
        self.win_a.show()

    def closeEvent(self, event):
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())
