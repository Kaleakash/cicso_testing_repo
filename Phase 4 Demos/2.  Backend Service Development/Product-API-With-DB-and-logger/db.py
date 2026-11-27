
import logging

import structlog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

logger = logging.getLogger(__name__)
structured_logger = structlog.get_logger(__name__)

# SQLite database URL
DATABASE_URL = "sqlite:///./products.db"

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    hide_parameters=True,
)

# Create database session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for SQLAlchemy models
Base = declarative_base()


# Database dependency
def get_db():
    logger.debug("Opening database session")
    structured_logger.debug("database_session_opening")
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
        logger.debug("Database session closed")
        structured_logger.debug("database_session_closed")

