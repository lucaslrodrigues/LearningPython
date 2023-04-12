import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[int]
    name: str
    age: int = "Impreciso"
    gender: str = "Não identificado"
    color: str = "Nenhuma especifica"

DataBase: List[Animal] = []


@app.get("/animal")
def view_database():
    return DataBase

@app.get("/animal/{id}")
def view_animal(id: str):
    # resposta = [r for r in DataBase if id == r.id]
    for a in DataBase:
        if a.id == id:
            return a
    return {'msg': 'Error 404 Not Found'}

@app.post("/animal")
def insert_root(animal: List[Animal]):
    for a in animal:
        a.id = str(uuid4())
        DataBase.append(a)

    return DataBase

@app.delete("/animal/{id}")
def delete_root(id: str):

    posicao = -1
    for index, animal in enumerate(DataBase):
        if animal.id == id:
            posicao = index
            break
    
    if posicao != -1:
        DataBase.pop(posicao)
        return {'msg': 'Animal removido com sucesso'}
    return {'msg': 'Error 404 not found'}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("docker_app.main:app", host="127.0.0.1", port=8000, reload=True)