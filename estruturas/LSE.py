from estruturas.Nodo import Nodo


class LSE:

    def __init__(self):
        self.head = None
        self.tail = None
        self.quantia_itens = 0  # -> variável de controle, controla/sabe o length da lista; mais prático do que percorrer a lista cada vez que quiser saber o tamanho dela

    def is_empty(self):
        return self.head == None or self.quantia_itens == 0

    def inserir_inicio(self, dado_a_ser_inserido):
        novo_nodo = Nodo(dado_a_ser_inserido)  # Cria o nodo uma única vez

        if self.is_empty():
            self.head = novo_nodo
            self.tail = novo_nodo  # Ambos apontam para o mesmo objeto
        else:
            novo_nodo.proximo = self.head
            self.head = novo_nodo

        self.quantia_itens += 1

    def inserir_fim(self, dado_a_ser_inserido):
        novo_nodo = Nodo(dado_a_ser_inserido)
        
        if self.is_empty():
            self.head = novo_nodo
            self.tail = novo_nodo
        else:
            # O 'proximo' do atual tail deve ser o novo nodo
            self.tail.proximo = novo_nodo
            # Agora o novo nodo passa a ser o tail oficial
            self.tail = novo_nodo
            
        self.quantia_itens += 1

    def remover_inicio(self):
        if self.is_empty():
            print("A lista está vazia")
            return
        
        self.quantia_itens -= 1

        #se for um ´único dado na lista
        if self.head == self.tail: 
            dado_removido = self.tail
            self.head = None
            self.tail = None
            return dado_removido
        
        #se possuir mais de um dado
        dado_removido = self.head
        self.head = dado_removido.proximo
        dado_removido.proximo = None
        return dado_removido
        

    def remover_fim(self):
        if self.is_empty():
            print("A lista está vazia")
            return
        
        self.quantia_itens -= 1

        #se for um ´único dado na lista
        if self.head == self.tail: 
            dado_removido = self.tail
            self.head = None
            self.tail = None
            return dado_removido
        
        #se possuir mais de um dado
        dado_removido = None
        atual = self.head

        while atual != None:
            if (atual.proximo != None and atual.proximo == self.tail):
                dado_removido = self.tail
                self.tail = atual # o atual é o penúltimo item da lista
                atual.proximo = None
                return dado_removido

            atual = atual.proximo
        

    def imprimir_lista_completa(self):
        atual = self.head
        while atual != None:
            print(atual)
            atual = atual.proximo

    def imprimir_lado_a_lado(self):
        saida = ""
        atual = self.head
        while atual != None:
            if atual == self.head:
                saida += "[" + str(atual) + ']'
            else:
                saida += "=>" + "[" + str(atual) + ']'
            print(saida)