import os
from modelos.cliente import Cliente

NOME_ARQUIVO = "clientes.txt"


def criar_arquivo_clientes():
    try:
        if not os.path.exists(NOME_ARQUIVO):
            with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
                pass
    except Exception as erro:
        print("Erro ao criar arquivo de clientes:", erro)


def salvar_clientes(lista_clientes):
    try:
        with open(NOME_ARQUIVO, "w", encoding="utf-8") as arquivo:
            atual = lista_clientes.head
            while atual is not None:
                cliente = atual.valor
                arquivo.write(f"{cliente.id_cliente};{cliente.nome}\n")
                atual = atual.proximo
        return True
    except Exception as erro:
        print("Erro ao salvar clientes:", erro)
        return False


def carregar_clientes(lista_clientes):
    criar_arquivo_clientes()

    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                try:
                    partes = linha.split(";")

                    if len(partes) != 2:
                        continue

                    id_cliente = int(partes[0])
                    nome = partes[1].strip()

                    if id_cliente <= 0:
                        continue

                    if nome == "":
                        continue

                    novo_cliente = Cliente(id_cliente, nome)
                    lista_clientes.inserir_fim(novo_cliente)

                except:
                    continue

    except Exception as erro:
        print("Erro ao carregar clientes:", erro)