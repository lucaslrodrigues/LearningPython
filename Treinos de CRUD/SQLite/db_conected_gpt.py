from fastapi import FastAPI
from pydantic import BaseModel 
from sqlalchemy import create_engine, Column, Integer, String, Float 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base 

app = FastAPI()

# database connection

DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase" 
engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base()

# model 
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(50)) 
    price = Column(Float) 
    description = Column(String(100)) 

# schema 
class ItemCreate(BaseModel): 
    name: str 
    price: float 
    description: str = None 

class ItemUpdate(BaseModel): 
    name: str = None 
    price: float = None 
    description: str = None 
    
class ItemRead(BaseModel): 
    id: int 
    name: str 
    price: float 
    description: str = None 
    
# database methods 

def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 
        
def create_item(db, item: ItemCreate): 
    db_item = Item(name=item.name, price=item.price, description=item.description) 
    db.add(db_item) 
    db.commit() 
    db.refresh(db_item) 
    return db_item 

def get_item(db, item_id: int): 
    return db.query(Item).filter(Item.id == item_id).first() 

def get_items(db): 
    return db.query(Item).all() 

def update_item(db, item: Item, item_update: ItemUpdate): 
    for var, value in vars(item_update).items(): 
        if value is not None: 
            setattr(item, var, value) 
            db.commit() 
            db.refresh(item) 
    return item 
        
def delete_item(db, item: Item): 
    db.delete(item) 
    db.commit() 
    
# routes 

@app.post("/items/", response_model=ItemRead) 
def create_item_route(item: ItemCreate, db=Depends(get_db)): 
    return create_item(db, item) 

@app.get("/items/", response_model=List[ItemRead]) 
def read_items_route(db=Depends(get_db)): 
    items = get_items(db) 
    return items @app.get("/items/{item_id}", response_model=ItemRead) 

def read_item_route(item_id: int, db=Depends(get_db)): 
    item = get_item(db, item_id) 
    if item is None: 
        raise HTTPException(status_code=404, detail="Item not found") 
    return item @app.put("/items/{item_id}", response_model=ItemRead) 

def update_item_route(item_id: int, item_update: ItemUpdate, db=Depends(get_db)): 
    item = get_item(db, item_id) 
    if item is None: 
        raise HTTPException(status_code=404, detail="Item not found") 
    return update_item(db, item, item_update)  

@app.delete("/items/{item_id}") 
def delete_item_route(item_id: int, db=Depends(get_db)): 
    item = get_item(db, item_id) 
    if item is None: 
        raise HTTPException(status_code=404,detail="Item not found")