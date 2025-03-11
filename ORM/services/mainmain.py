from PyQt6.QtWidgets import QApplication
from praktika.Medical_records.app.mainWin import MainWin
import sys
from database import init_db, SessionLocal

from praktika.ORM.services.records_services import RecordsService
from praktika.ORM.services.patients_services import PatientsService
from praktika.ORM.services.employees_services import EmployeeService


def main():
    init_db()
    db = SessionLocal()

    try:
        employees_services = EmployeeService(db)

        employees_services.add_employee('Дмитрий', 'Греческий', 'Хирург')
        employees_services.add_employee('Василий', 'Пуповинский', 'Офтальмолог')

        patients_services = PatientsService(db)

        patients_services.add_patients('Петр', 'Колючий', 89145678787, '12.03.2025', '12:00', 1)
        patients_services.add_patients('Евгений', 'Молодой', 89248732398, '12.03.2025', '13:00', 2)

        records_services = RecordsService(db)

        records_services.add_record(1, 1, '89145678787', 'Хирург', '12.03.2025', '12:00')
        records_services.add_record(2, 2, '89248732398', 'Офтальмолог', '12.03.2025', '13:00')

    finally:
        db.close()
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


