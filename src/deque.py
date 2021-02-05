class Deque:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._data = []
        self._nome_do_arquivo = set()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Deque(" + ", ".join(map(lambda x: str(x), self._data)) + ")"

    def file_name(self, name):
        return name in self._nome_do_arquivo

    def push_front(self, value):
        self._data.insert(self.FIRST_ELEMENT, value)

    def push_back(self, value):
        self._data.append(value)
        self._nome_do_arquivo.add(value['nome_do_arquivo'])

    def pop_front(self):
        if len(self._data) > 0:
            self._nome_do_arquivo.remove(
                self._data[self.FIRST_ELEMENT]['nome_do_arquivo']
            )
            return self._data.pop(self.FIRST_ELEMENT)
        return None

    def pop_back(self):
        if self._data:
            return self._data.pop()
        return None

    def peek_any(self, position):
        if 0 <= position < len(self._data):
            return self._data[position]
        return "Posição Inválida"
