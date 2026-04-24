import random

class DummyMLPredictor:
    """
    Tracks accuracy and produces simple predictions.
    Replace with your trained model by implementing predict().
    """
    def __init__(self):
        self.correct = 0
        self.total = 0

    def predict(self, history, actual_next=None):
        if not history:
            pred = 0
        else:
            pred = random.choice(history)

        if actual_next is not None:
            self.total += 1
            if pred == actual_next:
                self.correct += 1
        return pred

    def get_accuracy(self):
        return (self.correct / self.total) if self.total else 0.0


class RealMLPredictor:
    """
    Example hook for integrating a trained model.
    Implement load_model() and predict() as per your framework (PyTorch/TensorFlow).
    """
    def __init__(self, model=None):
        self.model = model

    def load_model(self, path):
        # TODO: load your model here
        pass

    def predict(self, history, actual_next=None):
        # TODO: convert history to tensor and run inference
        # return predicted_page_id
        return 0
