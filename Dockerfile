# Usamos Python 3.12 (o el que tengas)
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos requirements y los instalamos
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para correr FastAPI apuntando a tu main.py dentro de la carpeta app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
