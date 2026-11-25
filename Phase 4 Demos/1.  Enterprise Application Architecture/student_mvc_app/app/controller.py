from fastapi import APIRouter, HTTPException, status

from app.core import SingletonMeta
from app.model import StudentCreate, StudentResponse, StudentUpdate
from app.service import (
    DuplicateEmailError,
    IStudentService,
    StudentNotFoundError,
)


class StudentController(metaclass=SingletonMeta):
    """HTTP layer: translates requests/errors, delegates to the service."""

    def __init__(self, service: IStudentService):
        self._service = service
        self.router = APIRouter(prefix="/students", tags=["students"])
        self._register_routes()

    def _register_routes(self) -> None:
        r = self.router
        r.add_api_route("", self.list_students, methods=["GET"],
                        response_model=list[StudentResponse])
        r.add_api_route("/{student_id}", self.get_student, methods=["GET"],
                        response_model=StudentResponse)
        r.add_api_route("", self.create_student, methods=["POST"],
                        response_model=StudentResponse,
                        status_code=status.HTTP_201_CREATED)
        r.add_api_route("/{student_id}", self.update_student, methods=["PUT"],
                        response_model=StudentResponse)
        r.add_api_route("/{student_id}", self.delete_student, methods=["DELETE"],
                        status_code=status.HTTP_204_NO_CONTENT)

    def list_students(self):
        return self._service.list_students()

    def get_student(self, student_id: int):
        return self._call(self._service.get_student, student_id)

    def create_student(self, data: StudentCreate):
        return self._call(self._service.create_student, data)

    def update_student(self, student_id: int, data: StudentUpdate):
        return self._call(self._service.update_student, student_id, data)

    def delete_student(self, student_id: int):
        self._call(self._service.delete_student, student_id)

    @staticmethod
    def _call(fn, *args):
        try:
            return fn(*args)
        except StudentNotFoundError as e:
            raise HTTPException(status.HTTP_404_NOT_FOUND, str(e))
        except DuplicateEmailError as e:
            raise HTTPException(status.HTTP_409_CONFLICT, str(e))
