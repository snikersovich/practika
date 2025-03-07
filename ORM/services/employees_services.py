from sqlalchemy.exc import NoResultFound
from praktika.ORM.models.employees import Employees
from praktika.ORM.services.database import SessionLocal


class EmployeeService:
    def __init__(self, db: SessionLocal):
        self.db = db

    def add_employee(self, name: str, last_name: str, specialty: str) -> Employees:
        """Добавление нового сотрудника в базу данных."""
        new_employee = Employees(
            employee_name=name,
            employee_last_name=last_name,
            employee_specialty=specialty,
        )
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee

    def get_employee(self, employee_id: int) -> Employees:
        """Выборка сотрудника из базы данных по ID."""
        employee = self.db.query(Employees).filter(Employees.employee_id == employee_id).first()
        if not employee:
            raise NoResultFound("Сотрудник не найден")
        return employee

    def delete_employee(self, employee_id: int) -> None:
        """Удаления сотрудника из базы данных по ID."""
        employee = self.get_employee(employee_id)
        self.db.delete(employee)
        self.db.commit()

    def get_all_employees(self):
        """Выборка всех сотрудников из базы данных."""
        return self.db.query(Employees).all()