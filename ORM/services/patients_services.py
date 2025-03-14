from typing import Optional
from praktika.ORM.services.database import SessionLocal
from praktika.ORM.models.patients import Patients


class PatientsService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def add_patients(self, name: str, last_name: str, phone_number: int, reception_date: str, reception_time: str, employee_id: int) -> Patients:
        """Добавление нового пациента в базу данных."""
        new_patient = Patients(
            patient_name=name,
            patient_last_name=last_name,
            patient_phone_number=phone_number,
            patient_reception_date=reception_date,
            patient_reception_time=reception_time,
            employee_id=employee_id
        )
        self.db.add(new_patient)
        self.db.commit()
        self.db.refresh(new_patient)
        return new_patient

    def get_patient_by_id(self, patient_id: int) -> Optional[Patients]:
        """Возвращает пациента по идентификатору."""
        return self.db.query(Patients).filter(Patients.patient_id == patient_id).first()

    def update_patient(self, patient_id, name, last_name, phone_number, reception_date, reception_time, employee_id):
        patient = self.db.query(Patients).filter(Patients.patient_id == patient_id).first()
        if patient:
            patient.patient_name = name
            patient.patient_last_name = last_name
            patient.patient_phone_number = phone_number
            patient.patient_reception_date = reception_date
            patient.patient_reception_time = reception_time
            patient.employee_id = employee_id
            self.db.commit()  # Сохраните изменения
        else:
            raise ValueError("Пациент не найден")

    def delete_patient(self, patient_id: int) -> bool:
        """Удаляет пациента по идентификатору."""
        patient = self.get_patient_by_id(patient_id)
        if not patient:
            return False
        self.db.delete(patient)
        self.db.commit()
        return True

    def get_all_patients(self) -> list[Patients]:
        """Выборка всех пациентов из базы данных."""
        return self.db.query(Patients).all()