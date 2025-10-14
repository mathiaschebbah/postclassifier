from agents.models.model import Model

class PostClassifier:
    def __init__(self, model: Model) -> None:
        self.model = model
        self.responses = []

    def classify(self, image_url, caption: str):
        for _ in range(5):
            self.responses.append(self.model.call(image_url, caption))
        return self.responses