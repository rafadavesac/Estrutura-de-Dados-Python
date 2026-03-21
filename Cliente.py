from estruturas.LSE import LSE
#Cadastro de clientes
#listar clientes
#exibir clientes e valores totais gastos
class Cliente:

    def __init__(self,id):
        self.id = id
        self.nome = None 

    def cadastrar_cliente(self, nome, lista_clientes):
        self.nome = nome
        lista_clientes.inserir_fim(self)

    def listar_clientes(self, lista_clientes):
        atual = lista_clientes.head
        
        while atual != None:
            cliente = atual.valor
            print(f"ID: {cliente.id} | Nome: {cliente.nome}")
            atual = atual.proximo