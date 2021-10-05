from abc import ABC, abstractmethod


class Game(ABC):
    """
        Game interface for future use.
    """
    @abstractmethod
    def run_game(self):
        """
            Future main loop of the game.
        """
        pass

    @abstractmethod
    def is_game_over(self):
        """
            Checks for game over state.
        """
        pass

    @abstractmethod
    def calc_frame(self):
        """
            Calculates a single frame of the game.
        """
        pass
