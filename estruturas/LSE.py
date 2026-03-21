from estruturas.nodo import Nodo


class LSE:
    def __init__(self):
        self.head = None
        self.tail = None
        self.quantia_itens = 0

    def is_empty(self):
        return self.head is None or self.quantia_itens == 0

    def inserir_inicio(self, dado_a_ser_inserido):
        novo_nodo = Nodo(dado_a_ser_inserido)

        if self.is_empty():
            self.head = novo_nodo
            self.tail = novo_nodo
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
            self.tail.proximo = novo_nodo
            self.tail = novo_nodo

        self.quantia_itens += 1

    def remover_inicio(self):
        if self.is_empty():
            return None

        self.quantia_itens -= 1

        if self.head == self.tail:
            dado_removido = self.head.valor
            self.head = None
            self.tail = None
            return dado_removido

        dado_removido = self.head.valor
        self.head = self.head.proximo
        return dado_removido

    def remover_fim(self):
        if self.is_empty():
            return None

        self.quantia_itens -= 1

        if self.head == self.tail:
            dado_removido = self.tail.valor
            self.head = None
            self.tail = None
            return dado_removido

        atual = self.head
        while atual.proximo != self.tail:
            atual = atual.proximo

        dado_removido = self.tail.valor
        self.tail = atual
        self.tail.proximo = None
        return dado_removido

    def imprimir_lista_completa(self):
        atual = self.head
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def imprimir_lado_a_lado(self):
        saida = ""
        atual = self.head
        while atual is not None:
            if atual == self.head:
                saida += "[" + str(atual.valor) + "]"
            else:
                saida += " => [" + str(atual.valor) + "]"
            atual = atual.proximo
        print(saida)