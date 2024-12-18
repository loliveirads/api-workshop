# FastAPI
from fastapi import FastAPI, APIRouter, Depends, HTTPException

# SQLAlchemy (Conexão e ORM)
from sqlalchemy.orm import Session

# Pydantic (Schemas)
from pydantic import BaseModel
from typing import List, Optional

# Configuração do ambiente (.env)
import os
from dotenv import load_dotenv

# Modelos e Configurações
from .model import Produto  # Modelo ORM da tabela produtos
from .schema import ProdutosSchema  # Schema Pydantic para validação
from .config import SessionLocal, get_db  # Configuração do banco de dados

router = APIRouter()

@router.get("/") # Request
def ola_mundo(): #Response
    return {"ola":"Mundo"}

@router.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()  # SELECT * FROM produtos


@router.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.post("/produtos", response_model=ProdutosSchema)
def inserir_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.delete("/produtos/{produto_id}", response_model=ProdutosSchema)
async def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    

@router.put("/produtos/{produto_id}", response_model=ProdutosSchema)
def atualizar_produto(
    produto_id: int, produto_data: ProdutosSchema, db: Session = Depends(get_db)
):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh(db_produto)
        return db_produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

