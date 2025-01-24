import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt


class UserWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Городская больница №99')
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #057D9F;")

        layout = QVBoxLayout()

        self.priem_button = QPushButton("Запись на прием")
        self.priem_button.setStyleSheet("background-color: white; color: black;")
        self.priem_button.clicked.connect(self.open_priem_menu)
        layout.addWidget(self.priem_button)

        self.my_priem_button = QPushButton("Мои записи на прием")
        self.my_priem_button.setStyleSheet("background-color: white; color: black;")
        self.my_priem_button.clicked.connect(self.open_my_priem_menu)
        layout.addWidget(self.my_priem_button)

        self.setLayout(layout)

    def open_priem_menu(self):
        self.priem_window = QWidget()
        self.priem_window.setWindowTitle("Запись на прием")
        self.priem_window.setStyleSheet("background-color: #057D9F;")
        self.priem_window.resize(800, 600)

        layout = QVBoxLayout()

        self.terapevt_button = QPushButton("Терапевт")
        self.terapevt_button.setStyleSheet("background-color: white; color: black;")
        self.terapevt_button.clicked.connect(self.open_terapevt_menu)
        layout.addWidget(self.terapevt_button)

        self.oftalmolog_button = QPushButton("Хирург")
        self.oftalmolog_button.setStyleSheet("background-color: white; color: black;")
        self.oftalmolog_button.clicked.connect(self.open_hirurg_menu)
        layout.addWidget(self.oftalmolog_button)

        self.oftalmolog_button = QPushButton("Офтальмолог")
        self.oftalmolog_button.setStyleSheet("background-color: white; color: black;")
        self.oftalmolog_button.clicked.connect(self.open_oftalmolog_menu)
        layout.addWidget(self.oftalmolog_button)

        self.priem_window.setLayout(layout)
        self.priem_window.show()

    def open_terapevt_menu(self):
        pass

    def open_hirurg_menu(self):
        pass

    def open_oftalmolog_menu(self):
        pass

    def open_my_priem_menu(self):
        self.my_priem_window = QWidget()
        self.my_priem_window.setWindowTitle("Мои записи на прием")
        self.my_priem_window.setStyleSheet("background-color: #057D9F;")
        self.my_priem_window.resize(800, 600)

        my_zapis_table = QTableWidget()
        my_zapis_table.setColumnCount(3)
        my_zapis_table.setHorizontalHeaderLabels(
            ["Врач", "Время", "Номер талона"]
        )

        layout = QVBoxLayout()
        layout.addWidget(my_zapis_table)
        self.my_priem_window.setLayout(layout)
        self.my_priem_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_window = UserWin()
    user_window.show()
    sys.exit(app.exec())
