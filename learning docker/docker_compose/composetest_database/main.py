from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    login = Column(String)
    senha = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/people/")
async def create_User(name: str, email: str, password: str):
    db = SessionLocal()
    User = User(name=name, email=email, password=password)
    db.add(User)
    db.commit()
    db.refresh(User)
    return User

@app.get("/people/")
async def read_people():
    db = SessionLocal()
    people = db.query(User).all()
    return people

@app.get("/people/{User_id}")
async def read_User(User_id: int):
    db = SessionLocal()
    User = db.query(User).filter(User.id == User_id).first()
    return User

@app.put("/people/{User_id}")
async def update_User(User_id: int, name: str = None, email: str = None, password: str = None):
    db = SessionLocal()
    User = db.query(User).filter(User.id == User_id).first()
    if name:
        User.name = name
    if email:
        User.email = email
    if password:
        User.password = password
    db.commit()
    db.refresh(User)
    return User

@app.delete("/people/{User_id}")
async def delete_User(User_id: int):
    db = SessionLocal()
    User = db.query(User).filter(User.id == User_id).first()
    db.delete(User)
    db.commit()
    return {"message": "User deleted successfully"}
