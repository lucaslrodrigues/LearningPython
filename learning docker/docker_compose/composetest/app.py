from fastapi import FastAPI
from fastapi.routing import APIRouter

# router = APIRouter()
app = FastAPI()

@app.route('/')
def hello():
    return {'response': 'Hello World'}
