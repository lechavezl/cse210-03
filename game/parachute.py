class Parachute:

    def __init__(self):

        self._wrong_guesses = 0
        # self._parachute = ""

    def get_parachute(self):
        """Create the parachute and display it based on the
        player's guesses. If the player make a wrong guesses,
        this method will cut and display the parachute again.
        """

        if self._wrong_guesses == 0:

            parachute = """
              ___
             /___\\
             \\   /
              \\ /
               o
              /|\\
              / \\"""
        
        elif self._wrong_guesses == 1:
            parachute = """
             /___\\
             \\   /
              \\ /
               o
              /|\\
              / \\"""
        
        elif self._wrong_guesses == 2:
            parachute = """
             \\   /
              \\ /
               o
              /|\\
              / \\"""
        
        elif self._wrong_guesses == 3:
            parachute = """
             \\ /
               o
              /|\\
              / \\"""
        
        elif self._wrong_guesses == 4:
            parachute = """
               x
              /|\\
              / \\"""

    def cut_parachute(self):
        """Check if the parachue is entirely cut off. If this is true,
        then end the game.
        """

        pass