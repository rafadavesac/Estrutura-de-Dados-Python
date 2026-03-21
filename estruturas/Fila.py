class Fila:
    def __init__(self):
        self._items = []

    def enfileirar(self, item):
        self._items.append(item)

    def dequeue(self):
        if len(self._items) == 0:
            return None
        return self._items.pop(0)

    def next_to_leave_line(self):
        if len(self._items) == 0:
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)