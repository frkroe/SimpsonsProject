# INSTRUCCIONES FUNDAMENTALES
FROM python

# INSTRUCCIONES DE CONFIGURACIÓN
COPY ./main.py /app/
COPY ./requirements.txt /app/
WORKDIR /app/app/
RUN pip install -r requirements.txt

# INSTRUCCIONES DE EJECUCIÓN
CMD ["python", "main.py"]