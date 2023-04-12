from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

# def id_create():
#     c = 0
#     if len(DataBase) > 0:
#         while True:
#             verify = True
#             for r in DataBase:
#                 if r["id"] == len(DataBase) + c:
#                     print("Verify", len(DataBase) + c)
#                     c += 1
#                     # id = len(DataBase) + c
#                     verify = False
#             if verify:
#                 return len(DataBase) + c
#                 break
#     else:
#         print("Caiu no return")
#         return 1

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

    # for a in animal:
    #     DataBase.append(a)
    #     print(len(DataBase))
    return DataBase

@app.delete("/animal/{id}")
def delete_root(id: str):
    # cont = 0
    # for data in DataBase:
    #     if id == data.id:
    #         del DataBase[cont]
    #     cont += 1
    # return DataBase

    # OU

    posicao = -1
    for index, animal in enumerate(DataBase):
        if animal.id == id:
            posicao = index
            break
    
    if posicao != -1:
        DataBase.pop(posicao)
        return {'msg': 'Animal removido com sucesso'}
    return {'msg': 'Error 404 not found'}