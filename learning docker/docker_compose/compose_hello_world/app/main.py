from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root():
    return {"Response":"Hello World"}
