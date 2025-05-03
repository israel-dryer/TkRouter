class History:
    def __init__(self):
        self._stack = []
        self._index = -1

    def push(self, path):
        self._stack = self._stack[:self._index + 1]
        self._stack.append(path)
        self._index += 1
        return path

    def replace(self, path):
        if self._index >= 0:
            self._stack[self._index] = path
        else:
            self.push(path)

    def back(self):
        if self._index > 0:
            self._index -= 1
            return self._stack[self._index]

    def forward(self):
        if self._index + 1 < len(self._stack):
            self._index += 1
            return self._stack[self._index]

    def go(self, delta):
        target_index = self._index + delta
        if 0 <= target_index < len(self._stack):
            self._index = target_index
            return self._stack[self._index]

    def current(self):
        return self._stack[self._index] if self._index >= 0 else None

    def clear(self):
        self._stack = []
        self._index = -1
