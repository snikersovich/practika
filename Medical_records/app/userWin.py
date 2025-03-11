import sys
from datetime import datetime

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QTableWidget, QFormLayout, QLabel, QLineEdit,
                             QMessageBox,
                             QApplication, QComboBox, QDateTimeEdit, QTableWidgetItem)

from praktika.ORM.services.database import SessionLocal
from praktika.ORM.services.records_services import RecordsService
from praktika.ORM.services.employees_services import EmployeeService  # Предполагаем, что у вас есть этот сервис
from praktika.ORM.models.patients import Patients
from praktika.ORM.models.records import Records
from praktika.ORM.models.employees import Employees


class UserWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Городская больница №99')
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('resources/logo99'))
        self.setStyleSheet("background-color: #057D9F;")

        layout = QVBoxLayout()
        self.priem_button = QPushButton("Записаться на прием к врачу")
        self.priem_button.setStyleSheet("background-color: white; color: black;")
        self.priem_button.clicked.connect(self.open_data_input_window)
        layout.addWidget(self.priem_button)

        self.my_priem_button = QPushButton("Мои записи на прием")
        self.my_priem_button.setStyleSheet("background-color: white; color: black;")
        self.my_priem_button.clicked.connect(self.open_my_priem_menu)
        layout.addWidget(self.my_priem_button)

        self.setLayout(layout)

    def open_data_input_window(self):
        self.data_input_window = DataInputWindow(self)
        self.data_input_window.show()

    def open_my_priem_menu(self):
        self.my_priem_window = QWidget()
        self.my_priem_window.setWindowTitle("Мои записи на прием")
        self.my_priem_window.setFixedSize(600, 500)
        self.my_priem_window.setStyleSheet("background-color: #057D9F;")

        self.my_zapis_table = QTableWidget()
        self.my_zapis_table.setStyleSheet("background-color: white; color: black;")
        self.my_zapis_table.setColumnCount(3)
        self.my_zapis_table.setHorizontalHeaderLabels(["Специальность врача", "Дата", "Время"])

        layout = QVBoxLayout()
        layout.addWidget(self.my_zapis_table)
        self.my_priem_window.setLayout(layout)
        self.my_priem_window.show()

        self.load_appointments()

    def load_appointments(self):
        session = SessionLocal()
        records_service = RecordsService(session)
        employees_service = EmployeeService(session)  # Создаем экземпляр сервиса для получения сотрудников
        records = records_service.get_all_records()

        self.my_zapis_table.setRowCount(len(records))

        for row, record in enumerate(records):
            # Получаем специальность врача по его ID
            doctor = employees_service.get_employee(record.doctor_id)  # Получаем врача по ID
            doctor_specialty = doctor.employee_specialty if doctor else "Неизвестно"  # Получаем специальность

            self.my_zapis_table.setItem(row, 0,
                                        QTableWidgetItem(doctor_specialty))  # Вместо ID врача показываем специальность
            self.my_zapis_table.setItem(row, 1, QTableWidgetItem(record.patient_reception_date))
            self.my_zapis_table.setItem(row, 2, QTableWidgetItem(record.patient_reception_time))

        session.close()


class DataInputWindow(QWidget):
    def __init__(self, user_window):
        super().__init__()
        self.user_window = user_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Запись на прием')
        self.setStyleSheet("background-color: #057D9F;")
        self.setFixedSize(400, 300)

        layout = QFormLayout()

        self.last_name_label = QLabel("Фамилия:")
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.last_name_label, self.last_name_edit)

        self.name_label = QLabel("Имя:")
        self.name_edit = QLineEdit()
        self.name_edit.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.name_label, self.name_edit)

        self.phone_label = QLabel("Телефон:")
        self.phone_edit = QLineEdit()
        self.phone_edit.setStyleSheet("background-color: white; color: black;")
        layout.addRow(self.phone_label, self.phone_edit)

        self.date_time_label = QLabel("Дата и время:")
        self.date_time_edit = QDateTimeEdit()
        self.date_time_edit.setStyleSheet("background-color: white; color: black;")
        self.date_time_edit.setMinimumDate(datetime.now().date())
        layout.addRow(self.date_time_label, self.date_time_edit)

        self.doctor_combo = QComboBox()
        self.doctor_combo.setStyleSheet("background-color: white; color: black;")
        self.load_doctors()  # Загрузка списка врачей
        layout.addRow(QLabel("Врач:"), self.doctor_combo)

        self.speciality_label = QLabel("")
        layout.addRow(self.speciality_label)

        self.doctor_combo.currentIndexChanged.connect(self.update_speciality_label)

        self.submit_button = QPushButton("Записаться")
        self.submit_button.setStyleSheet("background-color: white; color: black;")
        self.submit_button.clicked.connect(self.submit_data)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)
        self.update_speciality_label()  # Обновляем информацию о специальности при инициализации

    def load_doctors(self):
        session = SessionLocal()
        employees_service = EmployeeService(session)
        doctors = employees_service.get_all_employees()
        session.close()

        for doctor in doctors:
            self.doctor_combo.addItem(f"{doctor.employee_name} {doctor.employee_last_name}", doctor.employee_id)

    def update_speciality_label(self):
        current_doctor_id = self.doctor_combo.currentData()
        session = SessionLocal()
        employees_service = EmployeeService(session)
        doctor = employees_service.get_employee(current_doctor_id)  # Получение врача по ID
        session.close()

        if doctor:
            self.speciality_label.setText(
                f"Специальность: {doctor.employee_specialty}")  # Правильное получение специальности врача
        else:
            self.speciality_label.setText("Специальность: Неизвестно")  # Если врача нет

    def submit_data(self):
        name = self.name_edit.text().strip()
        last_name = self.last_name_edit.text().strip()
        phone = self.phone_edit.text().strip()
        reception_date = self.date_time_edit.date().toString("dd-MM-yyyy")
        reception_time = self.date_time_edit.time().toString('HH:mm')

        if name and last_name and phone:
            doctor_id = self.doctor_combo.currentData()
            self.save_record(last_name, name, phone, doctor_id, reception_date, reception_time)
            QMessageBox.information(self, "Успех", "Запись успешно добавлена!")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")

    def save_record(self, last_name, name, phone, doctor_id, reception_date, reception_time):
        session = SessionLocal()
        new_patient = Patients(patient_last_name=last_name, patient_name=name, patient_phone_number=phone,
                               patient_reception_date=reception_date, patient_reception_time=reception_time)

        session.add(new_patient)
        session.commit()  # Коммитим, чтобы получить ID пациента

        patient_id = new_patient.patient_id

        new_record = Records(patient_id=patient_id, doctor_id=doctor_id,
                             patient_reception_date=reception_date, patient_reception_time=reception_time)
        session.add(new_record)
        session.commit()  # Коммитим изменения для новой записи

        session.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_window = UserWin()
    user_window.show()
    sys.exit(app.exec())
