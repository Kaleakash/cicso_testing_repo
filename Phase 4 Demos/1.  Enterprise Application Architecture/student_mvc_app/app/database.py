from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core import SingletonMeta

DATABASE_URL = "sqlite:///./students.db"


class Base(DeclarativeBase):
    pass


class Database(metaclass=SingletonMeta):
    """Singleton owning the engine and session factory."""

    def __init__(self, url: str = DATABASE_URL):
        self.engine = create_engine(url, connect_args={"check_same_thread": False})
        self._session_factory = sessionmaker(bind=self.engine, autoflush=False)

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self._session_factory()
