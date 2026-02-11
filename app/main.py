from fastapi import FastAPI
from app.infraestructure.database import engine, Base
from app.infraestructure.models import order_model

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Orders API running"}
