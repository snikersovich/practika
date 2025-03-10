import sys
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget, QTableWidget, \
    QHBoxLayout, QTableWidgetItem, QApplication, QFormLayout
from PyQt6.QtGui import QFont, QIcon
from sqlalchemy.exc import NoResultFound

from praktika.ORM.services.database import SessionLocal
from praktika.ORM.services.patients_services import PatientsService
from praktika.ORM.services.employees_services import EmployeeService
from praktika.ORM.services.records_services import RecordsService


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
        self.load_employee_data()
        self.load_patient_data()

    def initUI(self):
        self.setWindowTitle('Панель администратора')
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #057D9F;")

        self.patients_table = QTableWidget(0, 6)
        self.patients_table.setStyleSheet("background-color: white; color: black;")
        self.patients_table.setFixedSize(600, 200)

        self.employees_table = QTableWidget(0, 4)
        self.employees_table.setStyleSheet("background-color: white; color: black;")
        self.employees_table.setFixedSize(600, 200)

        self.patients_table.setHorizontalHeaderLabels(
            ['ID', 'Фамилия', 'Имя', 'Номер палаты', 'Время записи на прием', 'Врач'])
        self.employees_table.setHorizontalHeaderLabels(['ID', 'Фамилия', 'Имя', 'Специальность'])

        # Создание кнопок и их подключение
        self.create_patient_buttons()
        self.create_employee_buttons()

        patients_layout = QHBoxLayout()
        employees_layout = QHBoxLayout()

        patients_layout.addWidget(self.patients_table)
        patients_layout.addLayout(self.patients_buttons_layout)

        employees_layout.addWidget(self.employees_table)
        employees_layout.addLayout(self.employees_buttons_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(patients_layout)
        main_layout.addLayout(employees_layout)

        self.setLayout(main_layout)

    def create_patient_buttons(self):
        self.patients_buttons_layout = QVBoxLayout()

        add_patient_button = QPushButton('Добавить пациента')
        edit_patient_button = QPushButton('Редактировать пациента')
        delete_patient_button = QPushButton('Удалить пациента')

        add_patient_button.clicked.connect(self.add_patient)
        edit_patient_button.clicked.connect(self.edit_patient)
        delete_patient_button.clicked.connect(self.delete_patient)

        for button in [add_patient_button, edit_patient_button, delete_patient_button]:
            button.setStyleSheet("background-color: white; color: black;")
            self.patients_buttons_layout.addWidget(button)

    def create_employee_buttons(self):
        self.employees_buttons_layout = QVBoxLayout()

        add_employees_button = QPushButton('Добавить сотрудника')
        edit_employees_button = QPushButton('Редактировать сотрудника')
        delete_employees_button = QPushButton('Удалить сотрудника')

        add_employees_button.clicked.connect(self.add_employee)
        edit_employees_button.clicked.connect(self.edit_employee)
        delete_employees_button.clicked.connect(self.delete_employee)

        for button in [add_employees_button, edit_employees_button, delete_employees_button]:
            button.setStyleSheet("background-color: white; color: black;")
            self.employees_buttons_layout.addWidget(button)

    def load_patient_data(self):
        db = SessionLocal()
        patients_service = PatientsService(db)
        patients = patients_service.get_all_patients()
        db.close()

        self.patients_table.setRowCount(len(patients))

        for row, patient in enumerate(patients):
            self.patients_table.setItem(row, 0, QTableWidgetItem(str(patient.patient_id)))
            self.patients_table.setItem(row, 1, QTableWidgetItem(str(patient.patient_last_name)))
            self.patients_table.setItem(row, 2, QTableWidgetItem(str(patient.patient_name)))
            self.patients_table.setItem(row, 3, QTableWidgetItem(str(patient.patient_phone_number)))
            self.patients_table.setItem(row, 4, QTableWidgetItem(str(patient.patient_reception_time)))
            self.patients_table.setItem(row, 5, QTableWidgetItem(str(patient.employee_id)))

    def add_patient(self):
        self.patient_form_window = QWidget()
        self.patient_form_window.setWindowTitle("Добавить пациента")
        layout = QFormLayout()

        name_input = QLineEdit()
        last_name_input = QLineEdit()
        phone_number = QLineEdit()
        reception_time = QLineEdit()
        employee_id = QLineEdit()

        layout.addRow("Фамилия:", last_name_input)
        layout.addRow("Имя:", name_input)
        layout.addRow("Номер телефона:", phone_number)
        layout.addRow("Время записи на прием:", reception_time)
        layout.addRow("Лечащий врач:", employee_id)

        add_button = QPushButton("Добавить")
        add_button.clicked.connect(lambda: self.save_new_patient(
            name_input.text(), last_name_input.text(), phone_number.text(), reception_time.text(), employee_id.text()))
        layout.addRow(add_button)

        self.patient_form_window.setLayout(layout)
        self.patient_form_window.show()

    def save_new_patient(self, name, last_name, phone_number, reception_time, employee_id):
        db = SessionLocal()
        patients_service = PatientsService(db)
        try:
            patients_service.add_patients(name, last_name, phone_number, reception_time, employee_id)
            QMessageBox.information(self, 'Успех', 'Пациент добавлен успешно!')
            self.load_patient_data()
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', str(e))
        finally:
            db.close()

    def edit_patient(self):
        selected_row = self.patients_table.currentRow()
        if selected_row >= 0:
            patient_id = int(self.patients_table.item(selected_row, 0).text())

            # Открываем форму редактирования
            self.patient_form_window = QWidget()
            self.patient_form_window.setWindowTitle("Редактировать пациента")
            layout = QFormLayout()

            name_input = QLineEdit(self.patients_table.item(selected_row, 2).text())
            last_name_input = QLineEdit(self.patients_table.item(selected_row, 1).text())
            phone_number = QLineEdit(self.patients_table.item(selected_row, 3).text())
            reception_time = QLineEdit(self.patients_table.item(selected_row, 4).text())
            employee_id = QLineEdit(self.patients_table.item(selected_row, 5).text())

            layout.addRow("Фамилия:", last_name_input)
            layout.addRow("Имя:", name_input)
            layout.addRow("Номер телефона:", phone_number)
            layout.addRow("Время записи на прием:", reception_time)
            layout.addRow("Лечащий врач:", employee_id)

            edit_button = QPushButton("Сохранить изменения")
            edit_button.clicked.connect(lambda: self.save_edits_patient(
                patient_id, name_input.text(), last_name_input.text(), phone_number.text(), reception_time.text(),
                employee_id.text()))
            layout.addRow(edit_button)

            self.patient_form_window.setLayout(layout)
            self.patient_form_window.show()

    def save_edits_patient(self, patient_id, name, last_name, phone_number, reception_time, employee_id):
        db = SessionLocal()
        patients_service = PatientsService(db)
        try:
            patients_service.update_patient(patient_id, name, last_name, phone_number, reception_time, employee_id)
            QMessageBox.information(self, 'Успех', 'Данные пациента обновлены успешно!')
            self.load_patient_data()
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', str(e))
        finally:
            db.close()

    def delete_patient(self):
        selected_row = self.patients_table.currentRow()
        if selected_row >= 0:
            patient_id = int(self.patients_table.item(selected_row, 0).text())
            db = SessionLocal()
            patients_service = PatientsService(db)
            success = patients_service.delete_patient(patient_id)
            db.close()
            if success:
                QMessageBox.information(self, 'Успех', 'Пациент удалён успешно!')
                self.load_patient_data()
            else:
                QMessageBox.warning(self, 'Ошибка', 'Пациента с таким ID не найдено.')

    def load_employee_data(self):
        db = SessionLocal()
        employees_service = EmployeeService(db)
        employees = employees_service.get_all_employees()
        db.close()

        self.employees_table.setRowCount(len(employees))

        for row, employee in enumerate(employees):
            self.employees_table.setItem(row, 0, QTableWidgetItem(str(employee.employee_id)))
            self.employees_table.setItem(row, 1, QTableWidgetItem(str(employee.employee_last_name)))
            self.employees_table.setItem(row, 2, QTableWidgetItem(str(employee.employee_name)))
            self.employees_table.setItem(row, 3, QTableWidgetItem(str(employee.employee_specialty)))

    def add_employee(self):
        self.employee_form_window = QWidget()
        self.employee_form_window.setWindowTitle("Добавить сотрудника")
        layout = QFormLayout()

        name_input = QLineEdit()
        last_name_input = QLineEdit()
        specialty_input = QLineEdit()

        layout.addRow("Фамилия:", last_name_input)
        layout.addRow("Имя:", name_input)
        layout.addRow("Специальность:", specialty_input)

        add_button = QPushButton("Добавить")
        add_button.clicked.connect(lambda: self.save_new_employee(
            name_input.text(), last_name_input.text(), specialty_input.text()))
        layout.addRow(add_button)

        self.employee_form_window.setLayout(layout)
        self.employee_form_window.show()

    def save_new_employee(self, name, last_name, specialty):
        db = SessionLocal()
        employee_service = EmployeeService(db)
        try:
            employee_service.add_employee(name, last_name, specialty)
            QMessageBox.information(self, 'Успех', 'Сотрудник добавлен успешно!')
            self.load_employee_data()
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', str(e))
        finally:
            db.close()

    def edit_employee(self):
        selected_row = self.employees_table.currentRow()
        if selected_row >= 0:
            employee_id = int(self.employees_table.item(selected_row, 0).text())


            self.employee_form_window = QWidget()
            self.employee_form_window.setWindowTitle("Редактировать сотрудника")
            layout = QFormLayout()

            name_input = QLineEdit(self.employees_table.item(selected_row, 2).text())
            last_name_input = QLineEdit(self.employees_table.item(selected_row, 1).text())
            specialty_input = QLineEdit(self.employees_table.item(selected_row, 3).text())

            layout.addRow("Фамилия:", last_name_input)
            layout.addRow("Имя:", name_input)
            layout.addRow("Специальность:", specialty_input)

            edit_button = QPushButton("Сохранить изменения")
            edit_button.clicked.connect(lambda: self.save_edits_employee(
                employee_id, name_input.text(), last_name_input.text(), specialty_input.text()))
            layout.addRow(edit_button)

            self.employee_form_window.setLayout(layout)
            self.employee_form_window.show()

    def save_edits_employee(self, employee_id, name, last_name, specialty):
        db = SessionLocal()
        employee_service = EmployeeService(db)
        try:
            employee_service.update_employee(employee_id, name, last_name, specialty)
            QMessageBox.information(self, 'Успех', 'Данные сотрудника обновлены успешно!')
            self.load_employee_data()
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', str(e))
        finally:
            db.close()

    def delete_employee(self):
        selected_row = self.employees_table.currentRow()
        if selected_row >= 0:
            employee_id = int(self.employees_table.item(selected_row, 0).text())
            db = SessionLocal()
            employee_service = EmployeeService(db)
            try:
                success = employee_service.delete_employee(employee_id)
                if success:
                    QMessageBox.information(self, 'Успех', 'Сотрудник удалён успешно!')
                    self.load_employee_data()
                else:
                    QMessageBox.warning(self, 'Ошибка', 'Сотрудника с таким ID не найдено.')
            except NoResultFound:
                QMessageBox.warning(self, 'Ошибка', 'Сотрудника с таким ID не найдено.')
            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', str(e))
            finally:
                db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_win = AdminWin()
    admin_win.show()
    sys.exit(app.exec())
