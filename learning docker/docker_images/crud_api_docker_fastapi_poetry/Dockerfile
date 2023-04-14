FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install SQLAlchemy
RUN pip install --pre SQLAlchemy

COPY ./app /code/app

WORKDIR /code/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]