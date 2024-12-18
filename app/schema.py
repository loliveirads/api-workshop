from pydantic import BaseModel, PositiveInt
from typing import Optional


class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float