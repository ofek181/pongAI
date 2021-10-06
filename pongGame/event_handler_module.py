import pygame
import sys
from .consts_file import EventConsts


class EventHandler:
    """
        A static class to implement the event handler of the game.
        Methods
        ----------------------------
        handle_events() -> int:
         a function to handle the user events during the game run time.
    """

    @staticmethod
    def handle_events() -> int:
        """
        Handles the user's inputs during the game.
        Returns
            The action ID according to its enum class

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return EventConsts.QUIT.value
                    # pygame.event.post(pygame.event.Event(pygame.QUIT))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return EventConsts.LEFT_PADDLE_MOVE_UP.value
        if keys[pygame.K_s]:
            return EventConsts.LEFT_PADDLE_MOVE_DOWN.value
        if keys[pygame.K_UP]:
            return EventConsts.RIGHT_PADDLE_MOVE_UP.value
        if keys[pygame.K_DOWN]:
            return EventConsts.RIGHT_PADDLE_MOVE_DOWN.value

        return EventConsts.NO_ACTION.value

