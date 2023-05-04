# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# WORKDIR /app

# COPY requirements.txt /app

# RUN pip install -r requirements.txt

# COPY . /app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.8

# ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && pip install psycopg2

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]