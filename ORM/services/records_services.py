from praktika.ORM.models.records import Records
from praktika.ORM.services.database import SessionLocal


class RecordsService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def add_record(self, doctor_id: int, patient_id: int, record_time: str) -> Records:
        """Добавление новой записи на прием в базу данных."""
        new_record = Records(
            doctor_id=doctor_id,
            patient_id=patient_id,
            record_time=record_time
        )
        self.db.add(new_record)
        self.db.commit()
        self.db.refresh(new_record)
        return new_record

    def get_all_records(self):
        """Выборка всех записей на прием из базы данных."""
        return self.db.query(Records).all()