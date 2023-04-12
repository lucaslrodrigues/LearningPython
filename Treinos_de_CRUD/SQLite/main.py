from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
banco = [
        {
            "id" : 1,
            "name": "lucas"
        },
        {
            "id" : 2,
            "name": "jose"
        }
    ]

class Item(BaseModel):
    id: Optional[int]
    name: str

# GET

@app.get("/api/{id}")
def read_root(id: int):
    resultado = [r for r in banco if id == r["id"]]
    return resultado

@app.get("/api/view/all")
def read_item():
    return banco

# POST

@app.post("/api/add")
def add_item(data: List[Item]):
    for atributo in data:
        verify = True
        for i in banco:
            if atributo.id == i['id']:
                verify = False
        if verify:
            banco.append({'id': atributo.id,'name': atributo.name})
    return {'msg': "200 ok"}


# PUT
@app.put("/api/update/{id}")
def put_item( id: int, item: dict):
    cont = 0
    for atribute in banco:
        print(atribute)
        if atribute["id"] == id:
            banco[cont] = item
        cont +=1
    return {'msg': "200 ok"}


# PATCh
@app.patch("api/atualizarNome/{id}")
def update_item( id: int, item: dict):
    for atribute in banco:
        print(atribute)
        if atribute["id"] == id:
            atribute["name"] = item['name']
    return {'msg': "200 ok"}

# DELETE

@app.delete("/api/delete")
def delete_item(id: int):
    count = 0
    for atribute in banco:
        if atribute["id"] == id:
            del banco[count]
        count += 1
    return {'msg': "200 ok"}
