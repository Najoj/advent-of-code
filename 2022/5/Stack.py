class Stack:
    def __init__(self):
        self._stack = []
        self._height = 0

    def push(self, item, bottom=False):
        if item and item.strip():
            self._height += 1
            if bottom:
                self._stack = [item] + self._stack
            else:
                self._stack = self._stack + [item]

    def pop(self):
        if not self._stack:
            return None
        self._height -= 1
        item = self._stack[-1]
        self._stack = self._stack[:-1]
        return item

    def __len__(self):
        return self._height

    def __str__(self):
        string = ' '.join(string for string in self._stack[key])
        return string
