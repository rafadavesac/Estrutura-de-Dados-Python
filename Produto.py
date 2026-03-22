from estruturas.LSE import LSE
import os

# Para garantir que o python sempre use a pasta onde o script está salvo
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_DADOS = os.path.join(DIRETORIO_ATUAL, "dados")

class Produto:
    def __init__(self, id):
        self.id = id
        self.nome = None 
        self.quantia = 0
        self.preco = 0.0

    def cadastrar_produto(self, nome, quantia, preco, lista_produtos):
        if not nome.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        if quantia < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
            
        self.nome = nome
        self.quantia = quantia
        self.preco = preco
        lista_produtos.inserir_fim(self)

    def listar_produtos(self, lista_produtos):
        atual = lista_produtos.head
        if not atual:
            print("📦 Nenhum produto cadastrado no estoque.")
            return
        
        while atual != None:
            p = atual.valor
            print(f"ID: {p.id} | Nome do produto: {p.nome} | Quantidade: {p.quantia} | Preço: R${p.preco:.2f}")
            atual = atual.proximo

    def pesquisar_produto(self, lista_produtos, termo):
        atual = lista_produtos.head
        encontrados = False
        while atual:
            p = atual.valor
            if str(p.id) == termo or termo.lower() in p.nome.lower():
                print(f"Produto encontrado!\nID: {p.id} | Nome: {p.nome} | Estoque: {p.quantia} | Preço: R${p.preco:.2f}")
                encontrados = True
            atual = atual.proximo
        if not encontrados:
            print("❌ Nenhum produto encontrado com esse termo.")

    def calcular_valor_estoque(self, lista_produtos):
        total = 0
        atual = lista_produtos.head
        while atual:
            total += (atual.valor.quantia * atual.valor.preco)
            atual = atual.proximo
        print(f"\nValor total do estoque: R${total:.2f}")

def salvar_produtos(lista_lse):

    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)

    caminho = os.path.join(PASTA_DADOS, "produtos.txt")
    with open(caminho, "w", encoding="utf-8") as f:
        atual = lista_lse.head
        while atual:
            p = atual.valor
            f.write(f"{p.id};{p.nome};{p.quantia};{p.preco}\n")
            atual = atual.proximo

def carregar_produtos(lista_lse):
    caminho = os.path.join("dados", "produtos.txt")

    if not os.path.exists(caminho):
        return 0
    
    maior_id = -1
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip():
                partes = linha.strip().split(";")
                p = Produto(int(partes[0]))
                p.nome = partes[1]
                p.quantia = int(partes[2])
                p.preco = float(partes[3])
                lista_lse.inserir_fim(p)

                if p.id > maior_id:
                    maior_id = p.id

    return maior_id + 1