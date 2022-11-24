import random

class SecretWord:

    def __init__(self):

        self._secret_word = ["class", "january", "border", "image", "film", "promise", "kids", "lungs",
        "doll", "rhyme", "damage", "plants", "dance", "computer", "python", "secret", "plan"]
        self._random_word = random.choice(self._secret_word)

    def get_world(self):
        """Get and hold a secret word to display.
        
        Args:
            self (Director): An instance of Director.
        
        Returns:
            string: A random word
        """
        
        word = self._random_word
        return word
    
    def show_secret_world(self):

        secret_world = self.get_world()

        print("_" * len(secret_world))