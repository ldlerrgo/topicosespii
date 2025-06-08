# Usa una imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala Flask
RUN pip install flask

# Expone el puerto de la app
EXPOSE 80

# Comando para ejecutar la app
CMD ["python", "app.py"]
