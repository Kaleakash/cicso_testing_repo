
import logging
from time import perf_counter

import structlog
from fastapi import FastAPI

from logging_config import configure_logging

# Configure logging before importing application modules.
configure_logging()
logger = logging.getLogger(__name__)
structured_logger = structlog.get_logger(__name__)

from db import engine, Base

from product_model import Product

from product_controller import router


# Create database tables
logger.info("Initializing database tables")
structured_logger.info("database_tables_initializing")
try:
    Base.metadata.create_all(bind=engine)
except Exception:
    logger.exception("Database table initialization failed")
    structured_logger.exception("database_tables_initialization_failed")
    raise
logger.info("Database tables ready")
structured_logger.info("database_tables_ready")


app = FastAPI(
    title="Product Management API",
    description="FastAPI + SQLAlchemy + SQLite",
    version="1.0"
)


# Register product controller
app.include_router(router)


@app.middleware("http")
async def log_requests(request, call_next):
    started = perf_counter()
    logger.info("Request started: method=%s path=%s", request.method, request.url.path)
    structured_logger.info(
        "request_started", method=request.method, path=request.url.path
    )
    try:
        response = await call_next(request)
    except Exception:
        duration_ms = (perf_counter() - started) * 1000
        logger.exception(
            "Request failed: method=%s path=%s duration_ms=%.2f",
            request.method,
            request.url.path,
            duration_ms,
        )
        structured_logger.exception(
            "request_failed",
            method=request.method,
            path=request.url.path,
            duration_ms=duration_ms,
        )
        raise

    level = logging.INFO if response.status_code < 400 else logging.WARNING
    if response.status_code >= 500:
        level = logging.ERROR
    duration_ms = (perf_counter() - started) * 1000
    logger.log(
        level,
        "Request completed: method=%s path=%s status=%d duration_ms=%.2f",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    structured_logger.log(
        level,
        "request_completed",
        method=request.method,
        path=request.url.path,
        status=response.status_code,
        duration_ms=duration_ms,
    )
    return response


@app.get("/")
def home():
    logger.debug("Returning API health message")
    structured_logger.debug("api_health_message_returned")
    return {
        "message": "Product Management API is running"
    }
