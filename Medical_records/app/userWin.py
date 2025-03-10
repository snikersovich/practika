import sys
from datetime import datetime

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QLabel, QLineEdit, \
    QMessageBox, QApplication, QComboBox, QDateTimeEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class UserWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Городская больница №99')
        self.setWindowIcon(QIcon('resources/logo99'))
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #057D9F;")

        layout = QVBoxLayout()

        self.priem_button = QPushButton("Записаться на прием к врачу")
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
        self.priem_window.setWindowTitle("Выбор специальности врача")
        self.priem_window.setStyleSheet("background-color: #057D9F;")
        self.priem_window.resize(800, 600)

        layout = QVBoxLayout()

        self.otolarinolog_button = QPushButton("Терапевт")
        self.otolarinolog_button.setStyleSheet("background-color: white; color: black;")
        self.otolarinolog_button.clicked.connect(self.open_terapevt_menu)
        layout.addWidget(self.otolarinolog_button)

        self.oftalmolog_button = QPushButton("Хирург")
        self.oftalmolog_button.setStyleSheet("background-color: white; color: black;")
        self.oftalmolog_button.clicked.connect(self.open_hirurg_menu)
        layout.addWidget(self.oftalmolog_button)

        self.oftalmolog_button = QPushButton("Офтальмолог")
        self.oftalmolog_button.setStyleSheet("background-color: white; color: black;")
        self.oftalmolog_button.clicked.connect(self.open_oftalmolog_menu)
        layout.addWidget(self.oftalmolog_button)

        self.otolarinolog_button = QPushButton("Отоларинголог")
        self.otolarinolog_button.setStyleSheet("background-color: white; color: black;")
        self.otolarinolog_button.clicked.connect(self.open_otolarinolog_menu)
        layout.addWidget(self.otolarinolog_button)

        self.priem_window.setLayout(layout)
        self.priem_window.show()

    def open_terapevt_menu(self):
        self.data_input_window = DataInputWindow("Терапевт")
        self.data_input_window.show()

    def open_hirurg_menu(self):
        self.data_input_window = DataInputWindow("Хирург")
        self.data_input_window.show()

    def open_oftalmolog_menu(self):
        self.data_input_window = DataInputWindow("Офтальмолог")
        self.data_input_window.show()

    def open_otolarinolog_menu(self):
        self.data_input_window = DataInputWindow("Отоларинголог")
        self.data_input_window.show()

    def open_my_priem_menu(self):
        self.my_priem_window = QWidget()
        self.my_priem_window.setWindowTitle("Мои записи на прием")
        self.my_priem_window.setStyleSheet("background-color: #057D9F;")
        self.my_priem_window.resize(800, 600)

        my_zapis_table = QTableWidget()

        my_zapis_table.setStyleSheet("background-color: white; color: black;")
        my_zapis_table.setColumnCount(3)
        my_zapis_table.setHorizontalHeaderLabels(
            ["Врач", "Дата", "Время"]
        )

        layout = QVBoxLayout()
        layout.addWidget(my_zapis_table)
        self.my_priem_window.setLayout(layout)
        self.my_priem_window.show()


class DataInputWindow(QWidget):
    def __init__(self, specialist):
        super().__init__()
        self.specialist = specialist
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f'Запись на прием к {self.specialist}')
        self.setStyleSheet("background-color: #057D9F;")
        self.resize(500, 250)

        layout = QFormLayout()

        self.name_label = QLabel("Имя:")
        self.name_edit = QLineEdit()
        self.name_edit.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.name_label, self.name_edit)

        self.last_name_label = QLabel("Фамилия:")
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.last_name_label, self.last_name_edit)

        self.phone_label = QLabel("Телефон:")
        self.phone_edit = QLineEdit()
        self.phone_edit.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.phone_label, self.phone_edit)

        # Добавляем виджет для выбора даты
        self.date_label = QLabel("Выберите дату:")
        self.date_edit = QDateTimeEdit()
        self.date_edit.setCalendarPopup(True)  # Открываем календарь по клику
        self.date_edit.setDisplayFormat("dd.MM.yyyy")  # Формат отображения даты
        self.date_edit.setMinimumDate(datetime.now().date())  # Устанавливаем минимум текущей датой
        self.date_edit.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.date_label, self.date_edit)

        # Добавляем виджет для выбора времени из списка доступных интервалов
        self.time_label = QLabel("Выберите время:")
        self.time_combo = QComboBox()
        self.time_combo.addItems(["09:00", "10:00", "11:00", "12:00", "13:00", "14:00"])  # Пример списка времени
        self.time_combo.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.time_label, self.time_combo)

        self.submit_button = QPushButton("Отправить заявку")
        self.submit_button.setStyleSheet("background-color: white; color: black;")
        self.submit_button.clicked.connect(self.submit_data)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_data(self):
        name = self.name_edit.text().strip()
        last_name = self.last_name_edit.text().strip()
        phone = self.phone_edit.text().strip()
        chosen_date = self.date_edit.date().toString("dd.MM.yyyy")  # Получаем выбранную дату
        chosen_time = self.time_combo.currentText()  # Получаем выбранное время

        # Проверяем, что все поля заполнены
        if not all([name, last_name, phone]):
            message_box = QMessageBox()
            message_box.setWindowTitle("Ошибка")
            message_box.setText("Пожалуйста, заполните все поля.")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()
            return  # Прерывание функции, если не все поля заполнены

        # Логика для сохранения данных в базу данных или отправки заявки
        # ...

        # Сообщение об успешной записи
        message_box = QMessageBox()
        message_box.setWindowTitle("Успешная запись")
        message_box.setText(f"Ваш запрос успешно отправлен!\nМы свяжемся с Вами в ближайшее время.\nВыбранная дата: {chosen_date}\nВыбранное время: {chosen_time}.")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec()

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_window = UserWin()
    user_window.show()
    sys.exit(app.exec())
