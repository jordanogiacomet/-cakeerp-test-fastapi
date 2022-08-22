from fastapi import FastAPI, Depends, HTTPException
from typing import List
from schemas import SchemaItem, SchemaItemCreate, SchemaEndereco, SchemaEnderecoCreate
from sqlalchemy.orm import Session
from database import get_db, engine
from crud import create_endereco, get_endereco, get_items, get_item, create_item, get_enderecos
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/pessoas", response_model = List[SchemaItem]) #Definimos que esse endpoint vai devolver no formato que eu defini no schema item
def read_items(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items

@app.post("/pessoas", response_model=SchemaItem)
def post_item(item: SchemaItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

####################################################################################################################################

@app.get("/endereco", response_model = List[SchemaEndereco]) #Definimos que esse endpoint vai devolver no formato que eu defini no schema item
def read_endereco(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    endereco = get_enderecos(db, skip=skip, limit=limit)
    return endereco

@app.post("/endereco", response_model=SchemaEndereco)
def post_endereco(item: SchemaEnderecoCreate, db: Session = Depends(get_db)):
    return create_endereco(db=db, item=item)

