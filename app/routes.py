# FastAPI
from fastapi import FastAPI, APIRouter, Depends, HTTPException

# SQLAlchemy (Conexão e ORM)
from sqlalchemy.orm import Session

# Pydantic (Schemas)
from typing import List, Optional
from pydantic import BaseModel, PositiveFloat

# Configuração do ambiente (.env)
import os
from dotenv import load_dotenv

# Modelos e Configurações
from .model import Produto  # Modelo ORM da tabela produtos
from .config import SessionLocal, get_db  # Configuração do banco de dados

from .schema import ProdutosCreateSchema, ProdutosSchema, ProdutosUpdateSchema

router = APIRouter()

@router.get("/")
def ola_mundo():
    return {"ola": "Mundo"}

@router.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()  # SELECT * FROM produtos


@router.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.post("/produtos", response_model=ProdutosSchema)
def inserir_produto(produto: ProdutosCreateSchema, db: Session = Depends(get_db)):
    try:
        # Verificar duplicidade no título
        existente = db.query(Produto).filter(Produto.titulo == produto.titulo).first()
        if existente:
            raise HTTPException(status_code=400, detail="Produto com este título já existe")

        # Criar produto no banco de dados
        db_produto = Produto(**produto.dict())
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao inserir produto: {str(e)}")


@router.delete("/produtos/{produto_id}", response_model=dict)
async def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return {"message": f"Produto com ID {produto_id} removido com sucesso"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.put("/produtos/{produto_id}", response_model=ProdutosSchema)
def atualizar_produto(
    produto_id: int, produto_data: ProdutosUpdateSchema, db: Session = Depends(get_db)
):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto_data.dict(exclude_unset=True).items():
            setattr(db_produto, key, value)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

