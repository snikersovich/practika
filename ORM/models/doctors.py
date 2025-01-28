from sqlalchemy import Column, Integer, String, BOOLEAN, Float, ForeignKey
from praktika.ORM.services.database import Base


class Doctors(Base):
    __tablename__ = 'doctors'

    doctor_id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String, nullable=False)
    doctor_last_name = Column(String, nullable=False)
    doctor_specialty = Column(String, nullable=False)
    doctor_patients = Column(Integer, ForeignKey=True, index=True)
