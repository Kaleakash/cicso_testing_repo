from app.controller import StudentController
from app.core import SingletonMeta
from app.database import Database
from app.repository import IStudentRepository, SqlAlchemyStudentRepository
from app.service import IStudentService, StudentService


class LayerFactory(metaclass=SingletonMeta):
    """Factory wiring the layers: database -> repository -> service -> controller.

    Swap implementations here (Open/Closed, Dependency Inversion) without touching
    other layers.
    """

    def create_database(self) -> Database:
        return Database()

    def create_repository(self) -> IStudentRepository:
        return SqlAlchemyStudentRepository(self.create_database())

    def create_service(self) -> IStudentService:
        return StudentService(self.create_repository())

    def create_controller(self) -> StudentController:
        return StudentController(self.create_service())
