# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel
from typing import Optional

app = FastAPI();

class user_info(BaseModel):
    id: Optional[int]
    name: str
    login: str
    senha: str

@app.get('/')
def read_root():
    with sqlite3.connect('data_user_sqlite.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        query = ('select * from users;')

        cur.execute(query)

        data = cur.fetchall()
    return(data)

@app.post('/user')
def new_user(userData: user_info):
    with sqlite3.connect('data_user_sqlite.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        query = ("insert into users values ('%d', '%s', '%str', '%str')" % (userData.id, userData.name, userData.login, userData.senha))

        cur.execute(query)

        data = cur.fetchall()
    return(data)

@app.put('/user/{id}')
def change_user_info(userData: user_info, id: int):
    with sqlite3.connect('data_user_sqlite.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # return {"response": "update users set name = '%s', login = '%s', senha = '%s') where id = %d;" % (userData.name, userData.login, userData.senha, id)}
        query = ("update users set name = '%s', login = '%s', senha = '%s' where id = %d;" % (userData.name, userData.login, userData.senha, id))

        cur.execute(query)

        data = cur.fetchall()
    return(data)

@app.delete('/user/{id}')
def change_user_info(userData: user_info, id: int):
    with sqlite3.connect('data_user_sqlite.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # return {"response": "update users set name = '%s', login = '%s', senha = '%s') where id = %d;" % (userData.name, userData.login, userData.senha, id)}
        query = ("delete from users where id = %d;" % (id))

        cur.execute(query)

        data = cur.fetchall()
    return(data)