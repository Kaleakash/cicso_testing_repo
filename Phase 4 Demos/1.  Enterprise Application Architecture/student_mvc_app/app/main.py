from fastapi import FastAPI

from app.factory import LayerFactory


def create_app() -> FastAPI:
    factory = LayerFactory()
    factory.create_database().create_tables()
    app = FastAPI(title="Student Management System")
    app.include_router(factory.create_controller().router)
    return app


app = create_app()
