import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_DADOS = os.path.join(DIRETORIO_ATUAL, "dados")

class Venda:
    def __init__(self, id_venda, cliente, produto, quantidade):
        self.id = id_venda
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = quantidade * produto.preco

    def realizar_venda(self, fila_vendas):
        # Validação de estoque (Requisito 6)
        if self.quantidade <= 0:
            print("❌ Erro: A quantidade deve ser maior que zero.")
            return False
            
        if self.produto.quantia >= self.quantidade:
            self.produto.quantia -= self.quantidade
            fila_vendas.enfileirar(self)
            return True
        else:
            print(f"❌ Erro: Estoque insuficiente ({self.produto.quantia} disponíveis).")
            return False

    def visualizar_fila(fila_vendas):
        print("\n--- FILA DE VENDAS ---")
        if fila_vendas.is_empty():
            print("Nenhuma venda registrada.")
            return

        for v in fila_vendas._items:
            print(f"ID: {v.id} | Cliente: {v.cliente.nome} | Produto: {v.produto.nome} | Quantidade: {v.quantidade} | Total: R${v.valor_total:.2f}")

    def calcular_total_vendas(fila_vendas):
        total = sum(v.valor_total for v in fila_vendas._items)
        print(f"\nValor total de todas as vendas realizadas: R${total:.2f}")
        return total

# FUNÇÃO AUXILIAR DE BUSCA (Necessária para carregar os objetos do arquivo)
def buscar_por_id(lista_lse, id_procurado):
    atual = lista_lse.head
    while atual:
        if atual.valor.id == id_procurado:
            return atual.valor
        atual = atual.proximo
    return None



# PERSISTÊNCIA NA PASTA 'DADOS'
def salvar_vendas(fila_vendas):
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)
        
    caminho = os.path.join(PASTA_DADOS, "vendas.txt")
    with open(caminho, "w", encoding="utf-8") as f:

        f.write("id_venda; id_cliente; id_produto; quantidade; valor_total\n")

        for v in fila_vendas._items:
            f.write(f"{v.id}; {v.cliente.id}; {v.produto.id}; {v.quantidade}; {v.valor_total}\n")

def carregar_vendas(fila_vendas, lista_clientes, lista_produtos):
    caminho = os.path.join("dados", "vendas.txt")
    if not os.path.exists(caminho):
        return 0
    
    maior_id = -1
    with open(caminho, "r", encoding="utf-8") as f:

        f.readline()

        for linha in f:
            if linha.strip():
                partes = linha.strip().split(";")
                id_venda = int(partes[0])
                id_cliente = int(partes[1])
                id_produto = int(partes[2])
                quantidade = int(partes[3])
                
                cliente_obj = buscar_por_id(lista_clientes, id_cliente)
                produto_obj = buscar_por_id(lista_produtos, id_produto)
                
                if cliente_obj and produto_obj:
                    nova_venda = Venda(id_venda, cliente_obj, produto_obj, quantidade)
                    fila_vendas.enfileirar(nova_venda)
                    if id_venda > maior_id:
                        maior_id = id_venda
                        
    return maior_id + 1