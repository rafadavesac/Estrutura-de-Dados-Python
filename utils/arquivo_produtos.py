import csv
import os
from modelos.produtos import Produto

NOME_ARQUIVO = "produtos.csv"


def criar_arquivo_se_nao_existir():
    try:
        if not os.path.exists(NOME_ARQUIVO):
            with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(["id", "nome", "quantidade", "preco"])
    except Exception as erro:
        print("Erro ao criar arquivo:", erro)


def salvar_produtos(lista_produtos):
    try:
        with open(NOME_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["id", "nome", "quantidade", "preco"])

            produtos = lista_produtos.listar_produtos()

            for produto in produtos:
                escritor.writerow([
                    produto.id_produto,
                    produto.nome,
                    produto.quantidade,
                    produto.preco
                ])

        return True

    except Exception as erro:
        print("Erro ao salvar produtos:", erro)
        return False


def carregar_produtos(lista_produtos):
    criar_arquivo_se_nao_existir()

    try:
        with open(NOME_ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)

            for linha in leitor:
                try:
                    if len(linha) != 4:
                        continue

                    id_produto = int(linha[0])
                    nome = linha[1].strip()
                    quantidade = int(linha[2])
                    preco = float(linha[3])

                    if id_produto <= 0:
                        continue

                    if nome == "":
                        continue

                    if quantidade < 0:
                        continue

                    if preco <= 0:
                        continue

                    if not lista_produtos.id_ja_existe(id_produto):
                        produto = Produto(id_produto, nome, quantidade, preco)
                        lista_produtos.inserir_produto(produto)

                except:
                    continue

    except FileNotFoundError:
        print("Arquivo de produtos não encontrado.")
    except Exception as erro:
        print("Erro ao carregar produtos:", erro)