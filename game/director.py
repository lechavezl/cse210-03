


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret_word = SecretWord()
        self._is_playing = True
        self._parachute = Parachute()
        self._player = Player()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """THE COMMENTS HERE.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_updates(self):
        """THE COMMENTS HERE.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """THE COMMENTS HERE.

        Args:
            self (Director): An instance of Director.
        """
        
        pass