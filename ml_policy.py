class MLPolicy:
    def __init__(self, capacity, predictor):
        self.capacity = capacity
        self._frames = []
        self.predictor = predictor

    def access(self, history, page, next_page=None):
        # update predictor stats with next_page if provided
        _ = self.predictor.predict(history, actual_next=next_page)

        if page in self._frames:
            return False

        if len(self._frames) < self.capacity:
            self._frames.append(page)
            return True

        # Predict next likely page
        predicted = self.predictor.predict(history)

        # Evict a page least likely to be used soon
        if predicted in self._frames:
            # evict some other page
            victim = next((f for f in self._frames if f != predicted), self._frames[0])
        else:
            victim = self._frames[0]

        self._frames.remove(victim)
        self._frames.append(page)
        return True

    @property
    def frames(self):
        return list(self._frames)
