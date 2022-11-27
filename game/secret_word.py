import random

class SecretWord:

    def __init__(self):

        self._secret_word = ["class"]
        # self._secret_word = ["class", "january", "border", "image", "film", "promise", "kids", "lungs",
        # "doll", "rhyme", "damage", "plants", "dance", "computer", "python", "secret", "plan"]
        self._random_word = random.choice(self._secret_word)
        self._word = ""
        self._length = 0
        self._already_guessed_word = []
        self._wrong_guesses = 0

    def get_word(self):
        """Get and hold a secret word to display.
        
        Args:
            self (Director): An instance of Director.
        
        Returns:
            string: A random word
        """
        
        self._word = self._random_word
        return self._word
    
    def show_secret_word(self):

        secret_word = self.get_word()
        self._length = len(secret_word)
        display = print("_" * self._length)
        return display
    
    def guess_word(self, guess):

        random_word = self.get_word()
        length = len(random_word)
        show_word = "_" * length

        for letter in random_word:
            if guess in random_word:
                self._already_guessed_word.extend([guess])
                index = random_word.find(guess)
                random_word = random_word[:index] + "_" + random_word[index + 1:]
                show_word = show_word[:index] + guess + show_word[index + 1:]
                print(show_word)
        
        if guess in self._already_guessed_word:
            print("Please, try another letter.")
        
        else:
            self._wrong_guesses += 1
    
    # def guess_word(self, guess):

    #     # display = self.show_secret_word()
    #     # for letter in self.get_word():
    #     #     if guess in self.get_word():
    #     #         index = self.get_word().find(guess)
    #     #         index = guess
        
        
    #     if guess in self.show_secret_word():
    #         self._already_guessed_word.extend([guess])
    #         index = self.show_secret_word().find(guess)
    #         # index = guess
    #         self.show_secret_word()[index].replace("_", guess)

            
    #     #     # index.replace("_", guess)
    #     #     # word = word[:index] + "_" + word[index + 1:]
    #     #     # display = display[:index] + guess + display[index + 1:]
    #     #     # print(display)
        
    #     # elif guess in self._already_guessed_word:
    #     #     print("Try another letter.")
        
    #     # else:
    #     #     self._wrong_guesses += 1
        
    #     # if word == "_" * self._length:

    def guessed_word(self):
        if self._word == "_" * self._length:
            print("You guessed it!")