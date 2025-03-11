from praktika.ORM.models.records import Records
from praktika.ORM.models.patients import Patients
from praktika.ORM.services.database import SessionLocal


class RecordsService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def add_record(self, name, last_name, phone, specialist, chosen_date, chosen_time):
        session = SessionLocal()
        new_patient = Patients(
            patient_name=name,
            patient_last_name=last_name,
            patient_phone_number=phone,
            patient_reception_date=chosen_date,  # Передаем дату приема
            patient_reception_time=chosen_time,  # Передаем время приема
            employee_id=specialist  # Передаем идентификатор специалиста
        )

        session.add(new_patient)

        try:
            session.commit()
            print("Запись успешно добавлена")  # Успешное добавление
        except Exception as e:
            print(f"Ошибка при добавлении записи: {e}")
            session.rollback()  # Откат в случае ошибки
        finally:
            session.close()

    def get_all_records(self):
        """Выборка всех записей на прием из базы данных."""
        return self.db.query(Records).all()