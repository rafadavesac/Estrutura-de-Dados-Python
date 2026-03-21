class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

    def mostrar_dados(self):
        return f"ID: {self.id_cliente} | Nome: {self.nome}"