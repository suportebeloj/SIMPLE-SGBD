from sqlalchemy import (Column, Integer, DateTime, String, Float, Text)
from .orm import Base, engine

from datetime import datetime


class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nome = Column(String(150), unique=True)
    criado_em = Column(DateTime, default=datetime.now)
    atualizado_em = Column(DateTime, onupdate=datetime.now)

    def __repr__(self):
        return self.nome


class Entrada(Base):
    __tablename__ = 'entradas'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    valor = Column(Float)
    descricao = Column(Text, nullable=True)
    creado_em = Column(DateTime, default=datetime.now)
    atualizado_em = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'{self.titulo} - R${self.valor}'


class Saida(Base):
    __tablename__ = 'saidas'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    valor = Column(Float)
    descricao = Column(Text, nullable=True)
    creado_em = Column(DateTime, default=datetime.now)
    atualizado_em = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'{self.titulo} - R${self.valor}'


class Inteface:
    def __init__(self):
        self.base = Base.metadata.create_all(engine)
