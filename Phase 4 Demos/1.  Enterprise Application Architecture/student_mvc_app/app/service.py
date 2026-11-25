from abc import ABC, abstractmethod

from app.core import SingletonMeta
from app.model import Student, StudentCreate, StudentUpdate
from app.repository import IStudentRepository


class StudentNotFoundError(Exception):
    pass


class DuplicateEmailError(Exception):
    pass


class IStudentService(ABC):
    @abstractmethod
    def list_students(self) -> list[Student]: ...

    @abstractmethod
    def get_student(self, student_id: int) -> Student: ...

    @abstractmethod
    def create_student(self, data: StudentCreate) -> Student: ...

    @abstractmethod
    def update_student(self, student_id: int, data: StudentUpdate) -> Student: ...

    @abstractmethod
    def delete_student(self, student_id: int) -> None: ...


class _CombinedMeta(type(IStudentService), SingletonMeta):
    pass


class StudentService(IStudentService, metaclass=_CombinedMeta):
    """Business rules only; storage is injected via the repository abstraction."""

    def __init__(self, repository: IStudentRepository):
        self._repo = repository

    def list_students(self) -> list[Student]:
        return self._repo.get_all()

    def get_student(self, student_id: int) -> Student:
        student = self._repo.get_by_id(student_id)
        if student is None:
            raise StudentNotFoundError(f"Student {student_id} not found")
        return student

    def create_student(self, data: StudentCreate) -> Student:
        if self._repo.get_by_email(data.email):
            raise DuplicateEmailError(f"Email {data.email} already exists")
        return self._repo.add(Student(**data.model_dump()))

    def update_student(self, student_id: int, data: StudentUpdate) -> Student:
        student = self.get_student(student_id)
        changes = data.model_dump(exclude_unset=True)
        email = changes.get("email")
        if email and email != student.email and self._repo.get_by_email(email):
            raise DuplicateEmailError(f"Email {email} already exists")
        return self._repo.update(student, changes)

    def delete_student(self, student_id: int) -> None:
        self._repo.delete(self.get_student(student_id))
