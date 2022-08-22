import datetime
from email.policy import default
from operator import index
from turtle import title

from sqlalchemy import Column, Integer, String

from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index = True)
    cep = Column(Integer, index = True)

class Endereco(Base):
    __tablename__ = "endereco"

    id = Column(Integer, primary_key=True, index=True)
    rua = Column(String(45), index = True)
    bairro = Column(String(45), index = True)
    cep = Column(Integer, index = True)


