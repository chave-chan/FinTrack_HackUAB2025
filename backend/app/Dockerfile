# Usa Python como base
FROM python:3.11

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del backend
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]