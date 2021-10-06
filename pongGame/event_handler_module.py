import pygame
import sys
from .consts_file import Action


class EventHandler:
    """
        A static class to implement the event handler of the game.
        Methods
        ----------------------------
        handle_left_events() -> int:
         a function to handle the left user events during the game run time.
        handle_right_events() -> int:
         a function to handle the right user events during the game run time.
    """

    @staticmethod
    def handle_left_events() -> Action:
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
                    return Action.QUIT
                    # pygame.event.post(pygame.event.Event(pygame.QUIT))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return Action.MOVE_UP
        if keys[pygame.K_s]:
            return Action.MOVE_DOWN

        return Action.NO_ACTION

    @staticmethod
    def handle_right_events() -> Action:
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
                    return Action.QUIT
                    # pygame.event.post(pygame.event.Event(pygame.QUIT))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return Action.MOVE_UP
        if keys[pygame.K_DOWN]:
            return Action.MOVE_DOWN

        return Action.NO_ACTION

