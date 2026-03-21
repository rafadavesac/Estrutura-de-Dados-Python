class Pilha:
    def __init__(self):
        self._itens = []

    def push(self, item):
        self._itens.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._itens.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._itens[-1]

    def is_empty(self):
        return len(self._itens) == 0

    def __str__(self):
        return str(self._itens)

    def __len__(self):
        return len(self._itens)