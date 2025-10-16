import os
from pathlib import Path
from openai import OpenAI, responses
from dotenv import load_dotenv
from .model import Model
from typing import Optional

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / ".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
"""Chargement de la clé d'api"""

class OpenAIModel(Model):
    def __init__(self, prompt: str):
        super().__init__(prompt)
        self.openai = OpenAI(api_key=OPENAI_API_KEY)
        self.model = "gpt-5"

    def call(self, image_url_1 : str, text: str) -> str: 
        response = self.openai.responses.create(
            model=self.model,
            reasoning={
                    "effort": "high",
                },
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": self.prompt + text},
                    {
                        "type": "input_image",
                        "image_url": str(image_url_1),
                        "detail": "high",
                    },
                
                ],
            }],
        )
        return response.output_text

    def get_model_prompt(self) -> str:
        return self.prompt
