from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from praktika.ORM.services.database import Base


class Patients(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, nullable=False)
    patient_last_name = Column(String, nullable=False)
    patient_phone_number = Column(Integer, nullable=False)
    patient_reception_time = Column(String, nullable=False)

    # Внешний ключ на сотрудника (врача)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), index=True)

    employee = relationship("Employees", back_populates='patients')
    records = relationship('Records', back_populates='patients')