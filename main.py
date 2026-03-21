from Cliente import Cliente, salvar_clientes, carregar_clientes
from estruturas.LSE import LSE
from estruturas.Pilha import Pilha
from estruturas.Fila import Fila
import os

lista_clientes = LSE()

id_clientes = carregar_clientes(lista_clientes)

historico_operacoes = Pilha()

while True:

    try:

        opcao = int(input("Selecione uma das opções: \n"
                        "1- Cadastrar cliente\n"
                        "2- Listar clientes\n"
                        "3- Desfazer última operação\n"
                        "4- Sair\n"
                        ))

        if opcao == 1:
            nome = input("Digite o nome: ")
           
            novo_cliente = Cliente(id_clientes)
            novo_cliente.cadastrar_cliente(nome, lista_clientes)

            
            # Guarda uma tupla: (Tipo da ação, Objeto afetado)
            historico_operacoes.push(("CADASTRO_CLIENTE", novo_cliente))

            salvar_clientes(lista_clientes)

            id_clientes += 1
            os.system('cls') 
            print(f"\n\nCadastro concluído com sucesso!\nNome: {novo_cliente.nome}\nId: {novo_cliente.id}\n\n")

        elif opcao == 2:
            if id_clientes == 0:
                print("Nenhum cliente foi cadastrado ainda")
            else:
                Cliente(0).listar_clientes(lista_clientes)
        
        elif opcao == 3:
            if len(historico_operacoes) <= 0:
                print("Não há operações para desfazer")
            else:
                # O pop() remove e retorna a última tupla guardada
                operacao = historico_operacoes.pop()
                tipo_acao, objeto = operacao # tipo_acao: "CADASTRO_CLIENTE", objeto: objeto cliente

                if tipo_acao == "CADASTRO_CLIENTE":
                    lista_clientes.remover_fim()
                    salvar_clientes(lista_clientes) # Atualiza o arquivo
                    id_clientes -= 1  
                    print(f"Cadastro de '{objeto.nome}' desfeito com sucesso!")

        elif opcao ==4:
            print('Sessão finalizada!')
            break

        else:
                raise ValueError(f"O número {opcao} não é um número do menu")

    except Exception as e:
        # 'e' armazena o erro 
        print(f"❌ Ocorreu um erro: {e}")
        print("Por favor, tente novamente.")