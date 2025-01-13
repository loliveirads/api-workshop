from pydantic import BaseModel, PositiveFloat
from typing import Optional
from enum import Enum

# Enum para categorias
class CategoriaEnum(str, Enum):
    ELETRONICOS = "Eletrônicos"
    INFORMATICA = "Informática"
    MOVEIS = "Móveis"
    OUTROS = "Outros"

# Schema para criar produtos
class ProdutosCreateSchema(BaseModel):
    titulo: str
    descricao: Optional[str]
    preco: PositiveFloat
    disponivel: bool
    categoria: Optional[CategoriaEnum]  # Adicionando o enum diretamente

# Schema para atualizar produtos
class ProdutosUpdateSchema(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    preco: Optional[PositiveFloat]
    disponivel: Optional[bool]
    categoria: Optional[CategoriaEnum]  # Adicionando o enum diretamente

# Schema para resposta
class ProdutosSchema(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    preco: float
    disponivel: bool
    categoria: Optional[CategoriaEnum]  # Adicionando o enum diretamente

    class Config:
        from_attributes = True
