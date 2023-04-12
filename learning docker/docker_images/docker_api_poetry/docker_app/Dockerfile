FROM python:3

WORKDIR /docker

RUN python3 -m venv .venv

COPY . .

RUN .venv/bin/pip install -r requirements.txt

COPY myapp.py .
CMD ["venv/bin/python", "myapp.py", "poetry run start"]

# CMD ["python3", "source .venv/bin/activate", "poetry run start"]