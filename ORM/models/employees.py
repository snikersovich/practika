from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from praktika.ORM.services.database import Base


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, nullable=False)
    employee_last_name = Column(String, nullable=False)
    employee_specialty = Column(String, nullable=False)

    # Связь с пациентами
    patients = relationship("Patients", back_populates="employee")
    records = relationship('Records', back_populates='employee')

