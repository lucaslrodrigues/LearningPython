FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./docker /code/docker

CMD ["uvicorn", "docker.docker_app.main:app", "--host", "0.0.0.0", "--port", "80"]


# RUN python3 -m venv .venv
# RUN . .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
# RUN pip install --no-cache-dir
# COPY main.py docker/docker_app

# CMD [". .venv/bin/activate", "poetry run start"]

# CMD ["python3", "cd docker", "source .venv/bin/activate", "poetry run start"]