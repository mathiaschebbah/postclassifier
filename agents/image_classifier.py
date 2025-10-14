from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

read_file = open(os.path.join(os.path.dirname(__file__), "prompts", "imageclassifier.prompt"), "r")
prompt = str(read_file.read())
read_file.close()

class ImageClassifier():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = "gpt-4.1-mini"
        self.prompt = prompt

    def classify(self, image_url):
        response = self.client.responses.create(
            model=self.model,
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": self.prompt},
                    {
                        "type": "input_image",
                        "image_url": image_url,
                    },
                ],
            }],
        )
        return response.output_text

