import os
from pathlib import Path
from openai import OpenAI, responses
from dotenv import load_dotenv
from .model import Model
import moondream as md
from typing import Optional, overload

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent.parent / ".env")
MOONDREAM_API_KEY = os.getenv("MOONDREAM_API_KEY")

class MoondreamModel(Model):
    def __init__(self, prompt: str):
        super().__init__(prompt)
        model = md.Model(api_key=MOONDREAM_API_KEY)

    def call(self, image_url_1 : str, text: str) -> str: 
        result = self.model.query(image_url_1, self.prompt + text)
        answer = result["answer"]

        return answer
