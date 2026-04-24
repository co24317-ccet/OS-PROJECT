class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self._frames = []

    def access(self, page):
        if page in self._frames:
            self._frames.remove(page)
            self._frames.append(page)
            return False
        if len(self._frames) >= self.capacity:
            self._frames.pop(0)
        self._frames.append(page)
        return True

    @property
    def frames(self):
        return list(self._frames)
