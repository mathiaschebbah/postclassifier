from logging import exception
from pathlib import Path
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
"""Chargement de la clé d'api"""

prompt = (Path(__file__).resolve().parent / "prompts" / "post_classifier.prompt").read_text(encoding="utf-8")
"""Chargement du prompt"""


class PostClassifier():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = "gpt-4.1-mini"
        self.prompt = prompt
        self.reponses_acceptables = ["Oui, elle est triste.", "Non, elle n'est pas triste."]

    def classify(self, image_url, caption: str) -> str: 
        for i in range(self.iter):
            self.tries += 1
            response = self.client.responses.create(
                model=self.model,
                input=[{
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": self.prompt + caption},
                        {
                            "type": "input_image",
                            "image_url": str(image_url),
                            "detail": "low",
                        },
                    ],
                }],
            )
            if response.output_text.strip() in self.reponses_acceptables:
                print(response.output_text)
            else:
                raise exception("La réponse du modèle est incorrecte.")


