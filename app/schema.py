from typing import Optional
from pydantic import BaseModel, PositiveFloat

# Schema para criação de produtos
class ProdutosCreateSchema(BaseModel):
    titulo: str
    descricao: Optional[str]
    preco: PositiveFloat
    disponivel: bool

# Schema para resposta com ID incluído
class ProdutosSchema(ProdutosCreateSchema):
    id: int

    class Config:
        orm_mode = True
