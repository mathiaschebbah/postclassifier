from pathlib import Path

from agents.post_classifier import PostClassifier

prompt = (Path(__file__).resolve().parent / "agents" / "prompts" / "post_classifier.prompt").read_text(encoding="utf-8")
image_url = "https://media.gettyimages.com/id/1470493731/fr/photo/paris-france-general-views-at-the-jacquemus-obsession-exhibition-at-galeries-lafayette-on.jpg?s=1024x1024&w=gi&k=20&c=jcXJy7UTkDS6js6xLKjWje2_JYJ2xiQGDvHCpFF6um8="
caption = (Path(__file__).resolve().parent / "agents" / "captions" / "post_insta.prompt").read_text(encoding="utf-8")

post_classifier = PostClassifier(prompt)


print(post_classifier.classify(image_url, caption))
