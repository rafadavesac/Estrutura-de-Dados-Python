class Fila:
    def __init__(self):
        self._items = []

    def enfileirar(self, item):
        self._items.append(item) #sempre vai adicionar no final da lista
        #outro modo: self._items.insert(0, item) e pop()

    def dequeue(self):

        if len(self._items) == 0:
            print("A fila está vazia")
            return
        
        self._items.pop(0) # vai remover o index 0 da lista (o primeiro item da lista)

    def next_to_leave_line(self):
        print(self._items[0])
        return

    def is_empty(self):
        return len(self._items) == 0
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)