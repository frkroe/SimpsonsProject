# INSTRUCCIONES FUNDAMENTALES
FROM python

# INSTRUCCIONES DE CONFIGURACIÓN
## copiar archivos de python y requirements a carpeta creada "app":
COPY ./main.py /app/
COPY ./requirements.txt /app/
## establecer carpeta "app" como directorio de trabajo:
WORKDIR /app/
## instalar módulos necesarios:
RUN pip install -r requirements.txt

# INSTRUCCIONES DE EJECUCIÓN
CMD ["python", "main.py"]