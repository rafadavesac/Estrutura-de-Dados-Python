class Pilha:

    def __init__(self):
        self._itens = [] # '_' deixa a variavel/dado privada -> para não utilizar o item privado fora da classe

    def push(self, item): #adiciona o item sempre no topo da pilha (último dado colocado na lista)
        self._itens.append(item)

    def pop(self): #vai sempre remover o item do topo da pilha
        if self.is_empty():
            raise IndexError("Não é possível remover dados de uma pilha vazia")
        
        return self._itens.pop() #pop sempre exclui o ultimo dado que foi adicionado
        #retorna o item que foi removido

    def peek(self): #retorna que item está no topo
        if self.is_empty():
            raise IndexError("Não é possível remover dados de uma pilha vazia")
        
        return self._itens[-1]
        
    def is_empty(self): #retorna um boolean
        return len(self._itens) == 0 #se estiver vazia retorna true


    def __str__(self): # retorna o valor formatado da pilha
        return str(self._itens)

    def __len__(self): #retorna a quantidade de itens da pilha
        return len(self._itens)