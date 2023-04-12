from fastapi import FastAPI

app = FastAPI()

vendas = {
    'a': {"item" : "massa de bolo", "preco":5.3, "quantidade": 5},
    'b': {"item" : "feremento", "preco":3, "quantidade": 2},
    'c': {"item" : "acucar", "preco":3.45, "quantidade": 6},
    'd': {"item" : "leite", "preco":4.2, "quantidade": 12}
}

@app.get('/')
def home():
    return {"Vendas":len(vendas)} # CONVENÇÃO PADRÃO REST API SEMPRE EM JSON (NO CASO EM DICIONARIO)

@app.get('/vendas/{idVenda}')
def pegar_venda(idVenda: str):
    return vendas[idVenda]
