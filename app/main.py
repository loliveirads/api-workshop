from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos

app = FastAPI()

lista_de_produtos = Produtos()

@app.get("/") # Request
def ola_mundo(): #Response
    return {"ola":"Mundo"}

@app.get("/produtos")
def listar_produtos():
    return lista_de_produtos.listar_produtos()

@app.get("/produtos/{id}")
def buscar_produto(id: int):
    return lista_de_produtos.buscar_produto(id)

@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    return lista_de_produtos.adicionar_produtos(produto.model_dump())
