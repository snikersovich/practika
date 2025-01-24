from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWin
import sys
import traceback

from praktika.ORM.services.database import init_db, SessionLocal


def main():
    init_db()
    db = SessionLocal()
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec())


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))


sys.excepthook = excepthook

if __name__ == '__main__':
    main()