FROM python:3
COPY app /app
COPY json_storage /json_storage
COPY Password_storage /Password_storage
COPY Sq_database /Sq_database
CMD ["python", "/app/main.py"]
