from abc import ABC, abstractmethod

class Model(ABC):
    """
    Classe abstraite définissant l'interface commune pour tous les modèles.
    Cette classe établit le contrat que doivent respecter tous les modèles concrets.
    """

    def __init__(self, prompt: str):
        """
        Initialise le modèle avec un prompt donné.
        
        Args:
            prompt (str): Le prompt de base pour le modèle
        """
        self.prompt = prompt
    
    @abstractmethod
    def call(self, image_url: str, text: str) -> str:
        """
        Effectue un appel au modèle avec une image et du texte.
        
        Args:
            image_url (str): URL ou chemin vers l'image à analyser
            text (str): Texte additionnel à envoyer avec l'image
            
        Returns:
            str: La réponse du modèle
        """
        pass
    
    @abstractmethod
    def get_model_prompt(self) -> str:
        """
        Méthode pour récupérer le prompt du modèle.
        
        Returns:
            str: Le prompt actuellement configuré
        """
        pass
