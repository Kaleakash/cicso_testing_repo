from abc import ABC, abstractmethod
from typing import Optional

from app.core import SingletonMeta
from app.database import Database
from app.model import Student


class IStudentRepository(ABC):
    """Abstraction the service depends on (DIP, ISP)."""

    @abstractmethod
    def get_all(self) -> list[Student]: ...

    @abstractmethod
    def get_by_id(self, student_id: int) -> Optional[Student]: ...

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Student]: ...

    @abstractmethod
    def add(self, student: Student) -> Student: ...

    @abstractmethod
    def update(self, student: Student, data: dict) -> Student: ...

    @abstractmethod
    def delete(self, student: Student) -> None: ...


class _CombinedMeta(type(IStudentRepository), SingletonMeta):
    pass


class SqlAlchemyStudentRepository(IStudentRepository, metaclass=_CombinedMeta):
    """Only responsible for data access; one short-lived session per operation."""

    def __init__(self, database: Database):
        self._db = database

    def get_all(self) -> list[Student]:
        with self._db.get_session() as s:
            return list(s.query(Student).order_by(Student.id).all())

    def get_by_id(self, student_id: int) -> Optional[Student]:
        with self._db.get_session() as s:
            return s.get(Student, student_id)

    def get_by_email(self, email: str) -> Optional[Student]:
        with self._db.get_session() as s:
            return s.query(Student).filter(Student.email == email).first()

    def add(self, student: Student) -> Student:
        with self._db.get_session() as s:
            s.add(student)
            s.commit()
            s.refresh(student)
            s.expunge(student)
            return student

    def update(self, student: Student, data: dict) -> Student:
        with self._db.get_session() as s:
            current = s.get(Student, student.id)
            for key, value in data.items():
                setattr(current, key, value)
            s.commit()
            s.refresh(current)
            s.expunge(current)
            return current

    def delete(self, student: Student) -> None:
        with self._db.get_session() as s:
            s.delete(s.get(Student, student.id))
            s.commit()
