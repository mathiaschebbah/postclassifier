from pathlib import Path

from agents.post_classifier import PostClassifier

post_classifier = PostClassifier()

image_url = "https://imgs.search.brave.com/PLuBwWdpysNwK25zTOjZmG653qYgv82nJSodypQ_fQY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA0LzM0LzQ0LzY3/LzM2MF9GXzQzNDQ0/Njc3Nl8ya2lwU01w/UEVTczdrWkQzUFlz/bTFrTmJiUFE4amVp/Yy5qcGc"
caption = (Path(__file__).resolve().parent / "agents" / "captions" / "post_insta.prompt").read_text(encoding="utf-8")

print(post_classifier.classify(image_url, caption))

