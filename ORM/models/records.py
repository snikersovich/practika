from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from praktika.ORM.services.database import Base


class Records(Base):
    __tablename__ = 'records'

    record_id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('employees.employee_id'), index=True)
    patient_id = Column(Integer, ForeignKey('patients.patient_id'), index=True)
    record_time = Column(String, nullable=False)

    # Связи с другими таблицами
    employee = relationship("Employees", back_populates="records")
    patients = relationship("Patients", back_populates="records")