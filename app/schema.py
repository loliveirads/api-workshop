from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Optional


class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat