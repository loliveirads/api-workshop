from pydantic import BaseModel, PositiveFloat
from typing import Optional

# Schema para criar produtos (inserção)
class ProdutosCreateSchema(BaseModel):
    titulo: str
    descricao: str
    preco: PositiveFloat
    disponivel: bool

# Schema para atualizar produtos (alteração)
class ProdutosUpdateSchema(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    preco: Optional[PositiveFloat]
    disponivel: Optional[bool]

# Schema para resposta
class ProdutosSchema(ProdutosCreateSchema):
    id: int

    class Config:
        from_attributes = True

