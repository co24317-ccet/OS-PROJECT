class FIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def access(self, page):
        if page in self.queue:
            return False
        if len(self.queue) >= self.capacity:
            self.queue.pop(0)
        self.queue.append(page)
        return True

    @property
    def frames(self):
        return list(self.queue)
