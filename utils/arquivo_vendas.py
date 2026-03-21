import os
from modelos.venda import Venda

PASTA_DADOS = "dados"
NOME_ARQUIVO = "dados/vendas.txt"


def criar_arquivo_vendas():
    try:
        if not os.path.exists(PASTA_DADOS):
            os.makedirs(PASTA_DADOS)

        if not os.path.exists(NOME_ARQUIVO):
            with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
                pass
    except Exception as erro:
        print("Erro ao criar arquivo de vendas:", erro)


def buscar_cliente_por_id(lista_clientes, id_cliente):
    atual = lista_clientes.head

    while atual is not None:
        if atual.valor.id_cliente == id_cliente:
            return atual.valor
        atual = atual.proximo

    return None


def salvar_vendas(fila_vendas):
    criar_arquivo_vendas()

    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
            for venda in fila_vendas._items:
                arquivo.write(
                    f"{venda.id_venda};{venda.cliente.id_cliente};{venda.produto.id_produto};{venda.quantidade}\n"
                )
        return True
    except Exception as erro:
        print("Erro ao salvar vendas:", erro)
        return False


def carregar_vendas(fila_vendas, lista_clientes, lista_produtos):
    criar_arquivo_vendas()

    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                try:
                    partes = linha.split(";")

                    if len(partes) != 4:
                        continue

                    id_venda = int(partes[0])
                    id_cliente = int(partes[1])
                    id_produto = int(partes[2])
                    quantidade = int(partes[3])

                    if id_venda <= 0 or id_cliente <= 0 or id_produto <= 0 or quantidade <= 0:
                        continue

                    cliente = buscar_cliente_por_id(lista_clientes, id_cliente)
                    produto = lista_produtos.buscar_por_id(id_produto)

                    if cliente is None or produto is None:
                        continue

                    nova_venda = Venda(id_venda, cliente, produto, quantidade)
                    fila_vendas.enfileirar(nova_venda)

                except:
                    continue

    except Exception as erro:
        print("Erro ao carregar vendas:", erro)