class Venda:
    def __init__(self, id_venda, cliente, produto, quantidade):
        self.id_venda = id_venda
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = quantidade * produto.preco

    def mostrar_dados(self):
        return (
            f"ID Venda: {self.id_venda} | "
            f"Cliente: {self.cliente.nome} | "
            f"Produto: {self.produto.nome} | "
            f"Quantidade: {self.quantidade} | "
            f"Total: R$ {self.valor_total:.2f}"
        )