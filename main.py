from Cliente import Cliente, salvar_clientes, carregar_clientes
from Produto import Produto, salvar_produtos, carregar_produtos
from Venda import Venda, buscar_por_id, carregar_vendas, salvar_vendas
from estruturas.LSE import LSE
from estruturas.Pilha import Pilha
from estruturas.Fila import Fila
import os

lista_clientes = LSE()
lista_produtos = LSE()
fila_vendas = Fila()
historico_operacoes = Pilha()

id_clientes = carregar_clientes(lista_clientes)
id_produtos = carregar_produtos(lista_produtos)
id_vendas = carregar_vendas(fila_vendas, lista_clientes, lista_produtos)

while True:
    print("\n===== MENU ESTOQUE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Pesquisar produto")
    print("6 - Realizar venda")
    print("7 - Ver fila de vendas")
    print("8 - Desfazer última operação")
    print("9 - Exibir valor total do estoque")
    print("10 - Exibir valor total de vendas")
    print("11 - Exibir clientes e valores gastos")
    print("12 - Sair")
    print("========================")
    
    try:
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            novo = Cliente(id_clientes)
            novo.cadastrar_cliente(nome, lista_clientes)
            historico_operacoes.push(("CADASTRO_CLIENTE", novo))
            salvar_clientes(lista_clientes)
            id_clientes += 1
            print(f"Cliente cadastrado com sucesso!\nNome: {novo.nome} | ID: {novo.id}")

        elif opcao == '2':
            Cliente(0).listar_clientes(lista_clientes)

        elif opcao == '3':
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            novo_p = Produto(id_produtos)
            novo_p.cadastrar_produto(nome, qtd, preco, lista_produtos)
            historico_operacoes.push(("CADASTRO_PRODUTO", novo_p))
            salvar_produtos(lista_produtos)
            id_produtos += 1
            print(f"Produto cadastrado com sucesso!\nProduto: {novo_p.nome} | ID: {novo_p.id}")

        elif opcao == '4':
            Produto(0).listar_produtos(lista_produtos)

        elif opcao == '5':
            termo = input("Digite o ID ou Nome do produto: ")
            Produto(0).pesquisar_produto(lista_produtos, termo)

        elif opcao == '6':
            id_c = int(input("ID do Cliente: "))
            cli = buscar_por_id(lista_clientes, id_c)
            if not cli:
                raise ValueError("Cliente não encontrado.")

            id_p = int(input("ID do Produto: "))
            prod = buscar_por_id(lista_produtos, id_p)
            if not prod:
                raise ValueError("Produto não encontrado.")

            qtd = int(input(f"Quantidade de {prod.nome}: "))
            nova_venda = Venda(id_vendas, cli, prod, qtd)
            if nova_venda.realizar_venda(fila_vendas):
                historico_operacoes.push(("VENDA", nova_venda))
                id_vendas += 1
                salvar_vendas(fila_vendas)
                salvar_produtos(lista_produtos)
                print(
                    f"Venda realizada! Total: R${nova_venda.valor_total:.2f}")

        elif opcao == '7':
            Venda.visualizar_fila(fila_vendas)

        elif opcao == '8':
            if historico_operacoes.is_empty():
                print("⚠️ Não há operações para desfazer.")
            else:
                tipo, obj = historico_operacoes.pop()
                if tipo == "CADASTRO_CLIENTE":
                    lista_clientes.remover_fim()
                    salvar_clientes(lista_clientes)
                    id_clientes -= 1
                elif tipo == "CADASTRO_PRODUTO":
                    lista_produtos.remover_fim()
                    salvar_produtos(lista_produtos)
                    id_produtos -= 1
                elif tipo == "VENDA":
                    obj.produto.quantia += obj.quantidade
                    fila_vendas.remover_ultimo()  # Remove a última venda da lista interna da fila
                    salvar_vendas(fila_vendas)
                    salvar_produtos(lista_produtos)
                print(f"Operação de {tipo} desfeita!")

        elif opcao == '9':
            Produto(0).calcular_valor_estoque(lista_produtos)

        elif opcao == '10':
            Venda.calcular_total_vendas(fila_vendas)

        elif opcao == '11':
            Cliente(0).exibir_gastos_totais(lista_clientes, fila_vendas)

        elif opcao == '12':
            print("Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida. Escolha entre 1 e 12.")

    except ValueError as e:
        print(f"⚠️ Erro de entrada: {e}")
    except Exception as e:
        print(f"🔥 Ocorreu um erro inesperado: {e}")
