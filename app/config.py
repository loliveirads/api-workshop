#1. Importação de Bibliotecas


from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

#2. Carregar Variáveis de Ambiente

load_dotenv()

# Prints para depurar
print("DB_PORT:", os.getenv("DB_PORT"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("POSTGRES_USER:", os.getenv("POSTGRES_USER"))
print("POSTGRES_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))

# Acessar as variáveis
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Garantir que a porta seja um inteiro
if not DB_PORT or not DB_PORT.isdigit():
    raise ValueError("A variável DB_PORT não foi configurada corretamente.")
DB_PORT = int(DB_PORT)
#3. String de Conexão e Engine

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

#4. Configurar Sessão e Base

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

#5. Função get_db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
