import random

class SecretWord:
    """The secret word the users has to guess. 
    
    The responsibility the SecretWord class is to choose a random word from the list, display it using underscores
    and check if the player's guesses the secret word or not.
    
    Attributes:
        secret_word (list): A list of words.
        random_word (srt): Choose one word from the list randomly.
        length (int): Calculate the length of the word.
        display (str): Displays the secret word using underscores "_" based on the word's length.
        already_guessed_word (list): Stores the correct letters guesses to avoid the user repeat the same correct letters.
        wrong_guesses (int): The number of wrong guesses
    """

    def __init__(self):

        """Constructs a new SecretWord.

        Args:
            self (SecretWord): An instance of SecretWord.
        """

        self._secret_word = ["class", "january", "border", "image", "film", "promise", "kids", "lungs", 
        "doll", "rhyme", "damage", "plants", "dance", "computer", "python", "secret", "plan"]
        self._random_word = random.choice(self._secret_word)
        self._length = len(self._random_word)
        self._display = "_" * self._length
        self._already_guessed_word = []
        self._wrong_guesses = 0

    
    def show_secret_word(self):
        """Show the secret word using undersocres "_".

        Args:
            self (SecretWord): An instance of SecretWord.
        
        Returns: The parachute's string
        """

        self._display
        return self._display
    
    def guess_word(self, guess):
        """Check if the users guess is correct of incorrect to dysplay the result.

        Args:
            self (SecretWord): An instance of SecretWord.
            guess: The user's guess.
        """

        if guess in self._random_word:
            self._already_guessed_word.extend([guess])
            index = self._random_word.find(guess)
            self._random_word = self._random_word[:index] + "_" + self._random_word[index + 1:]
            self._display = self._display[:index] + guess + self._display[index + 1:]
        
        elif guess in self._already_guessed_word:
            print("Please, try another letter.")
        
        else:
            self._wrong_guesses += 1


    def guessed_word(self):
        """Check if the user guessed the secret word.

        Args:
            self (SecretWord): An instance of SecretWord.
        
        Returns the comparison of the guesses and secret word.
        """
        if self._random_word == "_" * self._length:
            print(self._display)
            print("You guessed it!")
            return (self._random_word * self._length)