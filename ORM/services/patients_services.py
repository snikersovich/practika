from sqlalchemy.exc import NoResultFound
from praktika.ORM.models.patients import Patients
from praktika.ORM.services.database import SessionLocal


class PatientsService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def add_patients(self, name: str, last_name: str, phone_number: int, reception_time: str, employee_id: int) -> Patients:
        """Добавление нового пациента в базу данных."""
        new_patient = Patients(
            patient_name=name,
            patient_last_name=last_name,
            patient_phone_number=phone_number,
            patient_reception_time=reception_time,
            employee_id=employee_id
        )
        self.db.add(new_patient)
        self.db.commit()
        self.db.refresh(new_patient)
        return new_patient

    def get_all_patients(self):
        """Выборка всех пациентов из базы данных."""
        return self.db.query(Patients).all()