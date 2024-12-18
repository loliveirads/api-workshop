from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos
from typing import List
from .routes import router

app = FastAPI()

app.include_router(router)