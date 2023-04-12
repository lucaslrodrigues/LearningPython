import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def saudacao():
	print("bom dia")
	return {"msg": "bom dia"}

def start():
	uvicorn.run("teste2.main:app", host="0.0.0.0", port=8000, reload=True)
