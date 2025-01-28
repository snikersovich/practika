import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QIcon, QFont


class AdminWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вход администратора')
        self.setWindowIcon(QIcon('resources/zamok'))
        self.setFixedSize(300, 200)
        self.setStyleSheet("background-color: #057D9F;")

        self.login_label = QLabel('Логин:')
        self.login_input = QLineEdit()
        self.login_input.setStyleSheet("background-color: white; color: black;")

        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("background-color: white; color: black;")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.submit_button = QPushButton('Войти')
        self.submit_button.setStyleSheet("background-color: white; color: black;")
        self.submit_button.clicked.connect(self.check_credentials)

        font = QFont()
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_input.setFont(font)
        self.password_label.setFont(font)
        self.password_input.setFont(font)
        self.submit_button.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.login_input.text()
        password = self.password_input.text()

        if username == "123" and password == "123":
            QMessageBox.information(self, 'Успех', 'Вход выполнен успешно!')
            self.open_admin_dashboard()
            self.close()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль!')

    def open_admin_dashboard(self):
        self.dashboard = AdminDashboard()
        self.dashboard.show()


class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Панель администратора')
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #057D9F;")

        self.patients_table = QTableWidget(0, 4)
        self.patients_table.setStyleSheet("background-color: white; color: black;")
        self.patients_table.setFixedSize(500, 200)

        self.doctors_table = QTableWidget(0, 4)
        self.doctors_table.setStyleSheet("background-color: white; color: black;")
        self.doctors_table.setFixedSize(500, 200)

        self.patients_table.setHorizontalHeaderLabels(['ФИО', 'Номер палаты', 'Диагноз', 'Врач'])
        self.doctors_table.setHorizontalHeaderLabels(['Фамилия', 'Имя', 'Специальность', 'Пациенты'])

        add_patient_button = QPushButton('Добавить пациента')
        edit_patient_button = QPushButton('Редактировать пациента')
        delete_patient_button = QPushButton('Удалить пациента')

        add_doctor_button = QPushButton('Добавить врача')
        edit_doctor_button = QPushButton('Редактировать врача')
        delete_doctor_button = QPushButton('Удалить врача')

        add_patient_button.clicked.connect(self.add_patient)
        add_patient_button.setStyleSheet("background-color: white; color: black;")
        edit_patient_button.clicked.connect(self.edit_patient)
        edit_patient_button.setStyleSheet("background-color: white; color: black;")
        delete_patient_button.clicked.connect(self.delete_patient)
        delete_patient_button.setStyleSheet("background-color: white; color: black;")

        add_doctor_button.clicked.connect(self.add_doctor)
        add_doctor_button.setStyleSheet("background-color: white; color: black;")
        edit_doctor_button.clicked.connect(self.edit_doctor)
        edit_doctor_button.setStyleSheet("background-color: white; color: black;")
        delete_doctor_button.clicked.connect(self.delete_doctor)
        delete_doctor_button.setStyleSheet("background-color: white; color: black;")

        patients_layout = QHBoxLayout()
        doctors_layout = QHBoxLayout()

        patients_buttons_layout = QVBoxLayout()
        doctors_buttons_layout = QVBoxLayout()

        patients_buttons_layout.addWidget(add_patient_button)
        patients_buttons_layout.addWidget(edit_patient_button)
        patients_buttons_layout.addWidget(delete_patient_button)

        doctors_buttons_layout.addWidget(add_doctor_button)
        doctors_buttons_layout.addWidget(edit_doctor_button)
        doctors_buttons_layout.addWidget(delete_doctor_button)

        patients_layout.addWidget(self.patients_table)
        patients_layout.addLayout(patients_buttons_layout)

        doctors_layout.addWidget(self.doctors_table)
        doctors_layout.addLayout(doctors_buttons_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(patients_layout)
        main_layout.addLayout(doctors_layout)

        self.setLayout(main_layout)

    def add_patient(self):
        row_count = self.patients_table.rowCount()
        self.patients_table.insertRow(row_count)
        for i in range(self.patients_table.columnCount()):
            item = QTableWidgetItem('')
            self.patients_table.setItem(row_count, i, item)

    def edit_patient(self):
        selected_row = self.patients_table.currentRow()
        if selected_row != -1:
            fio_item = self.patients_table.item(selected_row, 0).text()
            room_number_item = self.patients_table.item(selected_row, 1).text()
            diagnosis_item = self.patients_table.item(selected_row, 2).text()
            doctor_item = self.patients_table.item(selected_row, 3).text()
            print(f'Вы редактируете данные пациента {fio_item}')

    def delete_patient(self):
        selected_row = self.patients_table.currentRow()
        if selected_row != -1:
            self.patients_table.removeRow(selected_row)

    def add_doctor(self):
        row_count = self.doctors_table.rowCount()
        self.doctors_table.insertRow(row_count)
        for i in range(self.doctors_table.columnCount()):
            item = QTableWidgetItem('')
            self.doctors_table.setItem(row_count, i, item)

    def edit_doctor(self):
        selected_row = self.doctors_table.currentRow()
        if selected_row != -1:
            fio_item = self.doctors_table.item(selected_row, 0).text()
            specialty_item = self.doctors_table.item(selected_row, 1).text()
            patients_item = self.doctors_table.item(selected_row, 2).text()
            print(f'Вы редактируете данные врача {fio_item}')

    def delete_doctor(self):
        selected_row = self.doctors_table.currentRow()
        if selected_row != -1:
            self.doctors_table.removeRow(selected_row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_win = AdminWin()
    admin_win.show()
    sys.exit(app.exec())
