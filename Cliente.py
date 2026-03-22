from estruturas.LSE import LSE
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_DADOS = os.path.join(DIRETORIO_ATUAL, "dados")

class Cliente:
    def __init__(self, id):
        self.id = id
        self.nome = None 

    def cadastrar_cliente(self, nome, lista_clientes):
        if not nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        self.nome = nome
        lista_clientes.inserir_fim(self)

    def listar_clientes(self, lista_clientes):
        atual = lista_clientes.head
        if not atual:
            print("👥 Nenhum cliente cadastrado.")
            return
        while atual != None:
            cliente = atual.valor
            print(f"ID: {cliente.id} | Nome: {cliente.nome}")
            atual = atual.proximo

    def exibir_gastos_totais(self, lista_clientes, fila_vendas):
        print("\n=== TOTAL GASTO POR CLIENTE ===")
        atual = lista_clientes.head
        if not atual:
            print("Nenhum cliente cadastrado.")
            return
        while atual is not None:
            cliente = atual.valor
            total_cliente = 0
            for venda in fila_vendas._items:
                if venda.cliente.id == cliente.id:
                    total_cliente += venda.valor_total
            print(f"ID: {cliente.id} | Nome: {cliente.nome} | Total Gasto: R${total_cliente:.2f}")
            atual = atual.proximo

def salvar_clientes(lista_lse):

    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)

    caminho = os.path.join(PASTA_DADOS, "clientes.txt")
    
    with open(caminho, "w", encoding="utf-8") as f:
        atual = lista_lse.head
        while atual:
            c = atual.valor
            f.write(f"{c.id};{c.nome}\n")
            atual = atual.proximo

def carregar_clientes(lista_lse):
    caminho = os.path.join("dados", "clientes.txt")
    if not os.path.exists(caminho):
        return 0
    maior_id = -1
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                partes = linha.strip().split(";")
                novo = Cliente(int(partes[0]))
                novo.nome = partes[1]
                lista_lse.inserir_fim(novo)
                if novo.id > maior_id:
                    maior_id = novo.id
    return maior_id + 1