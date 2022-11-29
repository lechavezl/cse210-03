import random

class SecretWord:

    def __init__(self):

        self._secret_word = ["class"]
        # self._secret_word = ["class", "january", "border", "image", "film", "promise", "kids", "lungs",
        # "doll", "rhyme", "damage", "plants", "dance", "computer", "python", "secret", "plan"]
        self._random_word = random.choice(self._secret_word)
        self._length = len(self._random_word)
        self._display = "_ " * self._length
        self._already_guessed_word = []
        self._wrong_guesses = 0

    
    def show_secret_word(self):

        self._display
        return self._display
    
    def guess_word(self, guess):

        if guess in self._random_word:
            self._already_guessed_word.extend([guess])
            index = self._random_word.find(guess)
            self._random_word = self._random_word[:index] + "_ " + self._random_word[index + 1:]
            self._display = self._display[:index] + guess + self._display[index + 1:]
        
        elif guess in self._already_guessed_word:
            print("Please, try another letter.")
        
        else:
            self._wrong_guesses += 1


    def guessed_word(self):
        if self._random_word == "_ " * self._length:
            print(self._display)
            print("You guessed it!")
            return (self._random_word * self._length)


        # if self._display == self._random_word:
        #     print("You guessed it!")
        #     return (self._display == self._random_word)
        
        # elif self._wrong_guesses == 4:
        #     print("You were hanged, you lost.")