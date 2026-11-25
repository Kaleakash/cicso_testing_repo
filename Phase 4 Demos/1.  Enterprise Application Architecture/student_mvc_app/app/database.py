# from sqlalchemy import create_engine
# from sqlalchemy.orm import DeclarativeBase, sessionmaker

# from app.core import SingletonMeta

# DATABASE_URL = "sqlite:///./students.db"


# class Base(DeclarativeBase):
#     pass


# class Database(metaclass=SingletonMeta):
#     """Singleton owning the engine and session factory."""

#     def __init__(self, url: str = DATABASE_URL):
#         self.engine = create_engine(url, connect_args={"check_same_thread": False})
#         self._session_factory = sessionmaker(bind=self.engine, autoflush=False)

#     def create_tables(self) -> None:
#         Base.metadata.create_all(self.engine)

#     def get_session(self):
#         return self._session_factory()




import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core import SingletonMeta

# Override with e.g. mysql+pymysql://user:password@localhost:3306/student_db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")
#DATABASE_URL = "mysql+pymysql://root:root123@localhost:3306/student_db"


class Base(DeclarativeBase):
    pass


class Database(metaclass=SingletonMeta):
    """Singleton owning the engine and session factory."""

    def __init__(self, url: str = DATABASE_URL):
        options = {}
        if url.startswith("sqlite"):
            options["connect_args"] = {"check_same_thread": False}
        else:
            options["pool_pre_ping"] = True
        self.engine = create_engine(url, **options)
        self._session_factory = sessionmaker(bind=self.engine, autoflush=False)

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self._session_factory()
