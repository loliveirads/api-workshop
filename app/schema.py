from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Optional


class ProdutosSchema(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    disponivel: bool
