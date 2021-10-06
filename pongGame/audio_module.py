import pygame
from .consts_file import AudioConsts


class Audio:
    """
        A class to implement the audio of the game.
        ----------------------------
        Methods
        ----------------------------
        sound_score(self):
         Play the scoring sound during goal.
        sound_hit(self, score):
         Play the hitting sound during ball paddle intersection.
    """

    @staticmethod
    def sound_score():
        """
            Play the scoring sound.
        """
        pygame.mixer.init()
        channel = pygame.mixer.Channel(0)
        sound = pygame.mixer.Sound(AudioConsts.SCORE_AUDIO)
        channel.play(sound)

    @staticmethod
    def sound_hit():
        """
            Play the hitting sound.
        """
        pygame.mixer.init()
        channel = pygame.mixer.Channel(0)
        sound = pygame.mixer.Sound(AudioConsts.HIT_AUDIO)
        channel.play(sound)

