# Imagen base
FROM lpintofsgrp/practicabase:1
#FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el script al contenedor
COPY app.py .

# Instala Flask y Requests
RUN pip install flask requests

# Permisos a la carpeta
RUN chown -R appuser:appgroup /app

# Ejecutar con ese usuario
USER appuser

# Expone el puerto en el que correrá la app
EXPOSE 3000

# Comando por defecto para ejecutar la app
CMD ["python", "app.py"]
