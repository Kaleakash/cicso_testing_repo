from fastapi import FastAPI

from productController import router


app = FastAPI(title="Product API")
app.include_router(router)
