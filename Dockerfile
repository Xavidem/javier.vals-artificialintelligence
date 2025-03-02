FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt .
COPY scripts/ ./scripts/
COPY data/ ./data/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Definir el punto de entrada para ejecutar los scripts
CMD ["bash"]
