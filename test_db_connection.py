from sqlalchemy import create_engine
from app.infraestructure.database import DATABASE_URL

engine = create_engine(DATABASE_URL)
conn = engine.connect()
print("Connection OK!")
conn.close()
