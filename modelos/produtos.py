class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def mostrar_dados(self):
        return f"ID: {self.id_produto} | Nome: {self.nome} | Quantidade: {self.quantidade} | Preço: R$ {self.preco:.2f}"