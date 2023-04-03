from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    nome: str
    preco: float

@app.get('/area-retangulo')
def area_retangulo(largura: int, altura: int = 2):
    area = largura * altura
    return {'area': area}

@app.get("/quadrado/{numero}")
def calcular_quadrado(numero: int):
    resultado = numero * numero
    return {'quadrado': f'O quadrado de {numero} é {resultado}'}

@app.post("/produtos")
def produtos(produto: Produto):
    return {'msg': f'Produto {produto} cadastrado com sucesso!'}