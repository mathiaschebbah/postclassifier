from pathlib import Path
from agents.models.openai import OpenAIModel
from agents.models.moondream_model import MoondreamModel

from agents.post_classifier import PostClassifier

prompt = (Path(__file__).resolve().parent / "agents" / "prompts" / "post_classifier.prompt").read_text(encoding="utf-8")
image_url = "https://viacomit.net/wp-content/uploads/2022/02/campagne-adidas-y-3-20-years-re-coded-zinedine-zidane-00.jpg"
caption = (Path(__file__).resolve().parent / "agents" / "captions" / "post_insta.prompt").read_text(encoding="utf-8")

post_classifier = PostClassifier(model=MoondreamModel(prompt))

print(post_classifier.classify(image_url, caption))
