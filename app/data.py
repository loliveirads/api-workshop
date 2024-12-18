from typing import List, Dict
class Produtos:
    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Um telefone que é inteligente",
            "preco": 1500.0,
            "disponivel": True,
        },
        {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Um computador que é móvel",
            "preco": 3500.0,
            "disponivel": False,
        },
            {
            "id": 3,
            "nome": "Tablet",
            "descricao": "Um computador que é móvel",
            "preco": 800.0,
            "disponivel": False,
        }
    ]

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"status": 404, "Mensagem": "Produto não encontrado"}
    
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        return produto
