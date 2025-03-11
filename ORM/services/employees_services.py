from sqlalchemy.exc import NoResultFound
from praktika.ORM.services.database import SessionLocal
from praktika.ORM.models.employees import Employees


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

    def update_employee(self, employee_id, name, last_name, specialty):
        print(f"Updating employee: {employee_id}, {name}, {last_name}, {specialty}")
        employee = self.db.query(Employees).filter(Employees.employee_id == employee_id).first()
        if employee:
            employee.employee_name = name
            employee.employee_last_name = last_name
            employee.employee_specialty = specialty
            self.db.commit()
            print("Employee updated successfully")
        else:
            raise ValueError("Сотрудник не найден")

    def delete_employee(self, employee_id: int) -> bool:
        """Удаляет сотрудника по идентификатору."""
        employee = self.get_employee(employee_id)
        if not employee:
            return False
        self.db.delete(employee)
        self.db.commit()
        return True

    def get_all_employees(self):
        """Выборка всех сотрудников из базы данных."""
        return self.db.query(Employees).all()
