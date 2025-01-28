from sqlalchemy import Column, Integer, String, BOOLEAN, Float, ForeignKey
from praktika.ORM.services.database import Base


class Patients(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, nullable=False)
    patient_last_name = Column(String, nullable=False)
    patient_name_phone_number = Column(Integer, nullable=False)
    patient_reception_time = Column(String, nullable=False)
    patients_doctor = Column(Integer, ForeignKey=True, index=True)