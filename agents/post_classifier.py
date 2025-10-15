from agents.models.model import Model

class PostClassifier:
    """
    Classe permettant de classifier des posts à l'aide d'un modèle donné.
    """

    def __init__(self, model: Model) -> None:
        """
        Initialise le classifier avec un modèle.
        Args:
            model (Model): Instance du modèle à utiliser pour la classification.
        """
        self.model = model
        self.responses = []

    def classify(self, image_url_1, image_url_2, caption: str):
        """
        Classifie un post à partir de l'URL d'une image et d'une légende (caption).
        Args:
            image_url (str): Lien vers l'image à classifier.
            caption (str): Légende associée à l'image.

        Returns:
            list: Liste des réponses du modèle pour chaque appel.
        """
        self.responses.append(self.model.call(image_url_1, image_url_2, caption))
        return str(self.responses[0])