from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from praktika.ORM.services.config import DATABASE_URL


Base = declarative_base()
_engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=_engine)


def load_models():
    from praktika.ORM.models.employees import Employees
    from praktika.ORM.models.patients import Patients
    from praktika.ORM.models.records import Records


def init_db():
    load_models()
    Base.metadata.create_all(bind=_engine)
