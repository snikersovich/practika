from sqlalchemy import Column, Integer, String, BOOLEAN, Float, ForeignKey
from praktika.ORM.services.database import Base


class Records(Base):
    __tablename__ = 'records'

    doctor_id = Column(Integer, ForeignKey=True, index=True)
    patient_id = Column(Integer, ForeignKey=True, index=True)
    records_time = Column(String, nullable=False)