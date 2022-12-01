class Parachute:
    """The player's parachute. 
    
    The responsibility the Parachute class is to display the parachute and cut lines if the user's guess is wrong.
    If the parachute is entirely cutted off, then ends the game.
    
    Attributes:
        wrong_guesses (int): The number of wrong guesses
    """

    def __init__(self):

        self._wrong_guesses = 0

    def get_parachute(self, secret_word):
        """Create the parachute and display it based on the
        player's guesses. If the player make a wrong guess,
        this method will cut and display the parachute again.

        Args:
            self (Parachute): An instance of Parachute.
            secret_word: An instance of secret word to calculate wrong guesses.
        """

        parachute = """
 ___
/___\\
\\   /
 \\ /
  o
 /|\\
 / \\

^^^^^^^"""

        if secret_word._wrong_guesses == 0:

            parachute= """
 ___
/___\\
\\   /
 \\ /
  o
 /|\\
 / \\

^^^^^^^"""
        
        elif secret_word._wrong_guesses == 1:
            parachute = """
/___\\
\\   /
 \\ /
  o
 /|\\
 / \\

^^^^^^^"""
        
        elif secret_word._wrong_guesses == 2:
            parachute = """
\\   /
 \\ /
  o
 /|\\
 / \\

^^^^^^^"""
        
        elif secret_word._wrong_guesses == 3:
            parachute = """
 \\ /
  o
 /|\\
 / \\

^^^^^^^"""
        
        elif secret_word._wrong_guesses == 4:
            parachute = """
  x
 /|\\
 / \\

^^^^^^^"""
        
        return parachute

    def cut_parachute(self, secret_word):
        """Check if the parachue is entirely cut off. If this is true,
        then end the game.

        Args:
            self (Parachute): An instance of Parachute.
            secret_word: An instance of secret word to calculate wrong guesses.
        
        Returs: The comparison if there is 4 wrong guesses.
        """

        if secret_word._wrong_guesses == 4:
            print(secret_word._display)
            print(self.get_parachute(secret_word))
            print("Your parachute was cut off, you lost.")
            return (secret_word._wrong_guesses == 4)