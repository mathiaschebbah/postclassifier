from pathlib import Path
from agents.models.OpenAI import OpenAIModel

from agents.post_classifier import PostClassifier

prompt = (Path(__file__).resolve().parent / "agents" / "prompts" / "post_classifier.prompt").read_text(encoding="utf-8")
image_url = "https://imgs.search.brave.com/Vfbe7HLgZwme_Oq0prnNXP316wSq1Wsfgg7BAhvVoNY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQ3/MDQ5MzU4Ni9waG90/by9wYXJpcy1mcmFu/Y2UtZ2VuZXJhbC12/aWV3cy1hdC10aGUt/amFjcXVlbXVzLW9i/c2Vzc2lvbi1leGhp/Yml0aW9uLWF0LWdh/bGVyaWVzLWxhZmF5/ZXR0ZS1vbi5qcGc_/cz02MTJ4NjEyJnc9/MCZrPTIwJmM9V0JY/Y2V3QWJzYVZSUWVf/RmRWLUFrZGZRZGln/VFh0eWZfUlRZUmZ3/Wjcyaz0"
caption = (Path(__file__).resolve().parent / "agents" / "captions" / "post_insta.prompt").read_text(encoding="utf-8")

post_classifier = PostClassifier(model=OpenAIModel(prompt))

print(post_classifier.classify(image_url, caption))
