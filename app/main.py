from fastapi import FastAPI
from app.routes import order

app = FastAPI()

app.include_router(order.router)


@app.get("/")
def root():
    return {"message": "Orders API running"}
