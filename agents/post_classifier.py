from openai.resources.responses.responses import Responses
from agents.models.open_ai_model import OpenAIModel

class PostClassifier(OpenAIModel):
    def __init__(self, prompt: str) -> None:
        super().__init__(prompt)
        self.responses = []
        
    def classify(self, image_url, caption: str) -> str:
        for i in range(5):
            self.responses.append(self.model_call(image_url, caption))
        return self.responses