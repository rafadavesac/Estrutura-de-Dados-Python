from estruturas.lista_produtos import ListaEncadeadaProdutos
from estruturas.LSE import LSE
from estruturas.fila import Fila
from estruturas.pilha import Pilha

from modelos.produtos import Produto
from modelos.cliente import Cliente
from modelos.venda import Venda

from utils.arquivo_produtos import carregar_produtos, salvar_produtos
from utils.arquivo_clientes import carregar_clientes, salvar_clientes
from utils.arquivo_vendas import carregar_vendas, salvar_vendas, buscar_cliente_por_id


def obter_proximo_id_cliente(lista_clientes):
    maior = 0
    atual = lista_clientes.head

    while atual is not None:
        if atual.valor.id_cliente > maior:
            maior = atual.valor.id_cliente
        atual = atual.proximo

    return maior + 1


def obter_proximo_id_venda(fila_vendas):
    maior = 0

    for venda in fila_vendas._items:
        if venda.id_venda > maior:
            maior = venda.id_venda

    return maior + 1


def listar_clientes(lista_clientes):
    print("\n--- LISTA DE CLIENTES ---")

    if lista_clientes.is_empty():
        print("Nenhum cliente cadastrado.")
        return

    atual = lista_clientes.head
    while atual is not None:
        print(atual.valor.mostrar_dados())
        atual = atual.proximo


def cadastrar_cliente(lista_clientes, historico_operacoes):
    print("\n--- CADASTRO DE CLIENTE ---")

    nome = input("Digite o nome do cliente: ").strip()

    if nome == "":
        print("Erro: o nome não pode ficar vazio.")
        return

    if nome.isdigit():
        print("Erro: o nome não pode ser apenas números.")
        return

    id_cliente = obter_proximo_id_cliente(lista_clientes)
    novo_cliente = Cliente(id_cliente, nome)
    lista_clientes.inserir_fim(novo_cliente)

    if salvar_clientes(lista_clientes):
        historico_operacoes.push(("CADASTRO_CLIENTE", novo_cliente))
        print("Cliente cadastrado com sucesso.")
        print(novo_cliente.mostrar_dados())
    else:
        print("Cliente cadastrado, mas houve erro ao salvar.")


def cadastrar_produto(lista_produtos, historico_operacoes):
    print("\n--- CADASTRO DE PRODUTO ---")

    try:
        id_produto = int(input("Digite o ID do produto: "))
    except ValueError:
        print("Erro: o ID deve ser um número inteiro.")
        return

    if id_produto <= 0:
        print("Erro: o ID deve ser maior que zero.")
        return

    if lista_produtos.id_ja_existe(id_produto):
        print("Erro: já existe um produto com esse ID.")
        return

    nome = input("Digite o nome do produto: ").strip()

    if nome == "":
        print("Erro: o nome não pode ficar vazio.")
        return

    if not any(letra.isalpha() for letra in nome):
        print("Erro: o nome do produto deve ter pelo menos uma letra.")
        return
    

    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Erro: a quantidade deve ser um número inteiro.")
        return

    if quantidade < 0:
        print("Erro: a quantidade não pode ser negativa.")
        return

    try:
        preco = float(input("Digite o preço: ").replace(",", "."))
    except ValueError:
        print("Erro: o preço deve ser numérico.")
        return

    if preco <= 0:
        print("Erro: o preço deve ser maior que zero.")
        return

    novo_produto = Produto(id_produto, nome, quantidade, preco)
    lista_produtos.inserir_produto(novo_produto)

    if salvar_produtos(lista_produtos):
        historico_operacoes.push(("CADASTRO_PRODUTO", novo_produto))
        print("Produto cadastrado com sucesso.")
        print(novo_produto.mostrar_dados())
    else:
        print("Produto cadastrado, mas deu erro ao salvar no arquivo.")


def listar_produtos(lista_produtos):
    print("\n--- LISTA DE PRODUTOS ---")

    produtos = lista_produtos.listar_produtos()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(produto.mostrar_dados())

    print(f"\nTotal de produtos cadastrados: {lista_produtos.contar_produtos()}")


def pesquisar_produto(lista_produtos):
    print("\n--- PESQUISA DE PRODUTO ---")

    if lista_produtos.lista_vazia():
        print("Não existem produtos cadastrados no sistema.")
        return

    print("1 - Buscar por ID")
    print("2 - Buscar por nome")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        try:
            id_produto = int(input("Digite o ID do produto: "))
        except ValueError:
            print("Erro: o ID deve ser número inteiro.")
            return

        if id_produto <= 0:
            print("Erro: o ID deve ser maior que zero.")
            return

        produto = lista_produtos.buscar_por_id(id_produto)

        if produto is None:
            print("Produto não encontrado.")
        else:
            print("Produto encontrado:")
            print(produto.mostrar_dados())

    elif opcao == "2":
        nome = input("Digite o nome do produto: ").strip()

        if nome == "":
            print("Erro: digite um nome para pesquisar.")
            return

        encontrados = lista_produtos.buscar_por_nome(nome)

        if len(encontrados) == 0:
            print("Nenhum produto encontrado com esse nome.")
        else:
            print(f"Foram encontrados {len(encontrados)} produto(s):")
            for produto in encontrados:
                print(produto.mostrar_dados())

    else:
        print("Opção inválida.")


def realizar_venda(lista_clientes, lista_produtos, fila_vendas, historico_operacoes):
    print("\n--- REALIZAR VENDA ---")

    if lista_clientes.is_empty():
        print("Não há clientes cadastrados.")
        return

    if lista_produtos.lista_vazia():
        print("Não há produtos cadastrados.")
        return

    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("Erro: o ID do cliente deve ser inteiro.")
        return

    if id_cliente <= 0:
        print("Erro: o ID do cliente deve ser maior que zero.")
        return

    cliente = buscar_cliente_por_id(lista_clientes, id_cliente)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    try:
        id_produto = int(input("Digite o ID do produto: "))
    except ValueError:
        print("Erro: o ID do produto deve ser inteiro.")
        return

    if id_produto <= 0:
        print("Erro: o ID do produto deve ser maior que zero.")
        return

    produto = lista_produtos.buscar_por_id(id_produto)

    if produto is None:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Digite a quantidade vendida: "))
    except ValueError:
        print("Erro: a quantidade deve ser inteira.")
        return

    if quantidade <= 0:
        print("Erro: a quantidade vendida deve ser maior que zero.")
        return

    if quantidade > produto.quantidade:
        print(f"Erro: estoque insuficiente. Estoque atual: {produto.quantidade}")
        return

    id_venda = obter_proximo_id_venda(fila_vendas)
    nova_venda = Venda(id_venda, cliente, produto, quantidade)

    produto.quantidade -= quantidade
    fila_vendas.enfileirar(nova_venda)

    salvou_vendas = salvar_vendas(fila_vendas)
    salvou_produtos = salvar_produtos(lista_produtos)

    if salvou_vendas and salvou_produtos:
        historico_operacoes.push(("VENDA", nova_venda))
        print("Venda realizada com sucesso.")
        print(nova_venda.mostrar_dados())
    else:
        produto.quantidade += quantidade

        if not fila_vendas.is_empty():
            fila_vendas._items.pop()

        print("Erro: não foi possível salvar os arquivos. A venda foi cancelada.")


def visualizar_fila_vendas(fila_vendas):
    print("\n--- FILA DE VENDAS ---")

    if fila_vendas.is_empty():
        print("Nenhuma venda registrada.")
        return

    for venda in fila_vendas._items:
        print(venda.mostrar_dados())


def exibir_total_vendas(fila_vendas):
    total = 0

    for venda in fila_vendas._items:
        total += venda.valor_total

    print(f"\nValor total de vendas realizadas: R$ {total:.2f}")


def exibir_total_estoque(lista_produtos):
    total = lista_produtos.calcular_valor_total_estoque()
    print(f"\nValor total do estoque: R$ {total:.2f}")


def exibir_gastos_clientes(lista_clientes, fila_vendas):
    print("\n--- CLIENTES E VALORES TOTAIS GASTOS ---")

    if lista_clientes.is_empty():
        print("Nenhum cliente cadastrado.")
        return

    atual = lista_clientes.head

    while atual is not None:
        cliente = atual.valor
        total_gasto = 0

        for venda in fila_vendas._items:
            if venda.cliente.id_cliente == cliente.id_cliente:
                total_gasto += venda.valor_total

        print(f"ID: {cliente.id_cliente} | Nome: {cliente.nome} | Total Gasto: R$ {total_gasto:.2f}")
        atual = atual.proximo


def desfazer_ultima_operacao(lista_clientes, lista_produtos, fila_vendas, historico_operacoes):
    print("\n--- DESFAZER ÚLTIMA OPERAÇÃO ---")

    if historico_operacoes.is_empty():
        print("Não há operações para desfazer.")
        return

    operacao = historico_operacoes.pop()

    if operacao is None:
        print("Não há operações para desfazer.")
        return

    tipo_acao, objeto = operacao

    if tipo_acao == "CADASTRO_CLIENTE":
        lista_clientes.remover_fim()

        if salvar_clientes(lista_clientes):
            print(f"Cadastro do cliente '{objeto.nome}' desfeito com sucesso.")
        else:
            print("Erro: cliente removido da memória, mas não foi possível salvar no arquivo.")

    elif tipo_acao == "CADASTRO_PRODUTO":
        lista_produtos.remover_ultimo()

        if salvar_produtos(lista_produtos):
            print(f"Cadastro do produto '{objeto.nome}' desfeito com sucesso.")
        else:
            print("Erro: produto removido da memória, mas não foi possível salvar no arquivo.")

    elif tipo_acao == "VENDA":
        objeto.produto.quantidade += objeto.quantidade

        if not fila_vendas.is_empty():
            fila_vendas._items.pop()

        salvou_vendas = salvar_vendas(fila_vendas)
        salvou_produtos = salvar_produtos(lista_produtos)

        if salvou_vendas and salvou_produtos:
            print(f"Venda ID {objeto.id_venda} desfeita com sucesso.")
        else:
            print("Erro: venda desfeita na memória, mas não foi possível salvar nos arquivos.")

    else:
        print("Tipo de operação desconhecido.")


def menu():
    lista_clientes = LSE()
    lista_produtos = ListaEncadeadaProdutos()
    fila_vendas = Fila()
    historico_operacoes = Pilha()

    carregar_clientes(lista_clientes)
    carregar_produtos(lista_produtos)
    carregar_vendas(fila_vendas, lista_clientes, lista_produtos)

    while True:
        print("\n===================================")
        print("         SISTEMA DE ESTOQUE        ")
        print("===================================")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Pesquisar produto")
        print("6 - Realizar venda")
        print("7 - Visualizar fila de vendas")
        print("8 - Desfazer última operação")
        print("9 - Exibir valor total do estoque")
        print("10 - Exibir valor total de vendas")
        print("11 - Exibir clientes e valores totais gastos")
        print("12 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                cadastrar_cliente(lista_clientes, historico_operacoes)

            elif opcao == "2":
                listar_clientes(lista_clientes)

            elif opcao == "3":
                cadastrar_produto(lista_produtos, historico_operacoes)

            elif opcao == "4":
                listar_produtos(lista_produtos)

            elif opcao == "5":
                pesquisar_produto(lista_produtos)

            elif opcao == "6":
                realizar_venda(lista_clientes, lista_produtos, fila_vendas, historico_operacoes)

            elif opcao == "7":
                visualizar_fila_vendas(fila_vendas)

            elif opcao == "8":
                desfazer_ultima_operacao(lista_clientes, lista_produtos, fila_vendas, historico_operacoes)

            elif opcao == "9":
                exibir_total_estoque(lista_produtos)

            elif opcao == "10":
                exibir_total_vendas(fila_vendas)

            elif opcao == "11":
                exibir_gastos_clientes(lista_clientes, fila_vendas)

            elif opcao == "12":
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as erro:
            print("Ocorreu um erro:", erro)


if __name__ == "__main__":
    menu()