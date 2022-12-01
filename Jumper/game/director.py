from game.secret_word import SecretWord
from game.parachute import Parachute
from game.terminal_service import TerminalService


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret_word (SecretWord): The game's secret word.
        parachute  (Parachute): The game's parachute.
        terminal_service (TerminalService): For getting and displaying information on the terminal.
        is_playing (boolean): Whether or not to keep playing.
        guess (str/input): Stores the player's guess. 
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret_word = SecretWord()
        self._parachute = Parachute()
        self._terminal_service = TerminalService()
        self._is_playing = True
        self._guess = ""
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()
            self._end_game()

    def _get_inputs(self):
        """Prin the secret word and ask the user to guess a letter.

        Args:
            self (Director): An instance of Director.
        """

        self._guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
        print()
        
    def _do_updates(self):
        """Checks if the user's guess is the secret word. If so, show the secret word when the user
        guesses correctly.

        Args:
            self (Director): An instance of Director.
        """
        self._secret_word.guess_word(self._guess)
        
    def _do_outputs(self):
        """Shows the secret word after the users guesses a letter.
        Shows the parachute

        Check is the user guesses correctly or incorrectly. If the guess is wrong, cut lines
        on the parachute.

        Args:
            self (Director): An instance of Director.
        """

        self._terminal_service.write_text(self._secret_word.show_secret_word())
        write_parachute = self._parachute.get_parachute(self._secret_word)
        self._terminal_service.write_text(write_parachute)

    
    def _end_game(self):
        """Ends the game when the user guess the secret word or when the
        parachute is entirely cut off.

        Args:
            self (Director): An instance of Director.
        """

        if self._secret_word.guessed_word(self._parachute.get_parachute(self._secret_word)):
            self._is_playing = False
        
        elif self._parachute.cut_parachute(self._secret_word):
            self._is_playing = False