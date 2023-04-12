import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def saudacao():
    print("bom dia")
    return {"msg": "Bom dia"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main.main:app", host="0.0.0.0", port=8000, reload=True)