from estruturas.LSE import LSE
#Cadastro de clientes
#listar clientes
#exibir clientes e valores totais gastos
#salvar dados
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


# FUNÇÕES DE PERSISTÊNCIA DE DADOS

def salvar_clientes(lista_lse):
    with open("clientes.txt", "w", encoding="utf-8") as f:
        atual = lista_lse.head
        while atual:
            c = atual.valor
            f.write(f"{c.id};{c.nome}\n")
            atual = atual.proximo

def carregar_clientes(lista_lse):
    import os
    if not os.path.exists("clientes.txt"):
        return 0
    
    maior_id = -1
    with open("clientes.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                partes = linha.strip().split(";")
                novo = Cliente(int(partes[0]))
                novo.nome = partes[1]
                lista_lse.inserir_fim(novo)
                if novo.id > maior_id:
                    maior_id = novo.id
    return maior_id + 1