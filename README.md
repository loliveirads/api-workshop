# API Workshop

## Descrição
O projeto **API Workshop** é uma aplicação desenvolvida utilizando **FastAPI** e um banco de dados relacional para gerenciar produtos. A aplicação permite realizar operações de CRUD (Create, Read, Update, Delete) em produtos com informações como título, descrição, preço, disponibilidade e categoria.

## Links Importantes
- **Aplicação Streamlit**: [https://workshop-api.streamlit.app/](https://workshop-api.streamlit.app/)
- **Documentação da API**: [https://api-workshop-production.up.railway.app/docs](https://api-workshop-production.up.railway.app/docs)


## Funcionalidades
- **Listar Produtos**: Obtenha uma lista de todos os produtos disponíveis.
- **Obter Produto**: Consulte os detalhes de um produto específico pelo ID.
- **Inserir Produto**: Adicione novos produtos com título, descrição, preço, disponibilidade e categoria.
- **Alterar Produto**: Atualize as informações de um produto existente.
- **Remover Produto**: Exclua um produto do sistema.

## Requisitos
- **Python**: 3.11 ou superior
- **Poetry**: Gerenciador de dependências
- **Banco de Dados**: PostgreSQL
- **Outras Dependências**:
  - FastAPI
  - SQLAlchemy
  - Pydantic

## Configuração do Ambiente

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/loliveirads/api-workshop.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd api-workshop
   ```
3. Crie o ambiente virtual:
   ```bash
   poetry init
   ```
4. Ative o ambiente virtual:
   ```bash
   poetry shell
   ```
5. instale as dependências:
   ```bash
   poetry install
   ```


### Configuração do Banco de Dados
1. Configure o arquivo `.env` com as variáveis de ambiente necessárias:
   ```env
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
   ```
2. Execute as migrações para criar as tabelas no banco de dados:
   ```bash
   alembic upgrade head
   ```

## Executando a Aplicação
1. Inicie o servidor FastAPI:
   ```bash
   task run
   ```
2. Acesse a documentação interativa da API no navegador:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Estrutura do Projeto
```
api-workshop/
├── app/
│   ├── __init__.py
│   ├── main.py       # Configuração e inicialização da aplicação
│   ├── routes.py     # Rotas da API
│   ├── schema.py     # Schemas Pydantic
│   ├── model.py      # Modelos SQLAlchemy
│   └── config.py     # Configuração do banco de dados
├── tests/
│   └── test_main.py  # Testes automatizados
├── .env.example      # Exemplo do arquivo de configuração de ambiente
├── pyproject.toml    # Configuração do Poetry
├── README.md         # Documentação do projeto
└── requirements.txt  # Dependências do projeto
```

## Testes
Execute os testes utilizando o pytest:
```bash
pytest -v
```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

---
## Contato

Para dúvidas, sugestões ou feedbacks:

* **Luiz Fernando** - [luizfsoliveira.lm@gmail.com](mailto:luizfsoliveira.lm@gmail.com)

