from agents.image_classifier import ImageClassifier

image_classifier = ImageClassifier()

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

print(image_classifier.classify(image_url))

