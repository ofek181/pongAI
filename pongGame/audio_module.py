import pygame
from .consts_file import AudioConsts


class Audio:
    """
        A class to implement the audio of the game.
        ----------------------------
        Attributes
        ----------------------------
        channel : pygame.mixer object
         the single channel of audio used in the game.
        ----------------------------
        Methods
        ----------------------------
        __init__(self):
         Constructs all the necessary attributes for the Audio object.
        sound_score(self):
         Play the scoring sound during goal.
        sound_hit(self, score):
         Play the hitting sound during ball paddle intersection.
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Audio object.
        """
        pygame.mixer.init()
        self.channel = pygame.mixer.Channel(0)

    def sound_score(self):
        """
            Play the scoring sound.
        """
        sound = pygame.mixer.Sound(AudioConsts.SCORE_AUDIO)
        self.channel.play(sound)

    def sound_hit(self):
        """
            Play the hitting sound.
        """
        sound = pygame.mixer.Sound(AudioConsts.HIT_AUDIO)
        self.channel.play(sound)

