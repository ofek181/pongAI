import pygame
from pongGame.consts_file import DisplayConsts


class Display:
    """
        A class to implement the display of the game.
        ----------------------------
        Attributes
        ----------------------------
        screen : pygame object
         an attribute to represent the screen of the game.
        ----------------------------
        Methods
        ----------------------------
        __init__(self):
         Constructs all the necessary attributes for the Display object.
        show_game_over(self):
         Displays the game over screen
        show_score(self, score):
         Displays the score of the game
        animate_game(self, paddle_left, paddle_right, ball):
         Uses pygame methods in order to display the game on the screen.
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Display object.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((DisplayConsts.SCREEN_HEIGHT, DisplayConsts.SCREEN_HEIGHT))

    def show_game_over(self):
        """
            Displays the game over screen
        """
        font = pygame.font.SysFont(DisplayConsts.GAME_OVER_FONT_TYPE, DisplayConsts.GAME_OVER_FONT_SIZE)
        surface = font.render("Game Over", True, DisplayConsts.GAME_OVER_FONT_COLOR)  # Display game over
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 2.5, DisplayConsts.SCREEN_HEIGHT // 20)
        self.screen.blit(surface, rect)
        pygame.display.update()  # update the screen

    def show_score(self, score):
        """
            Displays the score over the screen
        """
        font = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        surface = font.render(str(score), True, DisplayConsts.FONT_COLOR)  # show score
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 2.5, DisplayConsts.SCREEN_HEIGHT // 20)
        self.screen.blit(surface, rect)
        pygame.display.update()  # update the screen

    # def animate_game(self, paddle_left, paddle_right, ball):
    #     """
    #         Implements the game animation on the screen attribute.
    #             Parameters:
    #                 paddle_left : left paddle of the game.
    #                 paddle_right: right paddle of the game.
    #                 ball: ball of the game.
    #     """
    #     pass

    def animate_game(self, ball):
        # self.screen.blit((0, 0, 0)), (0, 0))  # draw background
        pygame.draw.circle(self.screen, (255, 255, 255), (ball.x_pos, ball.y_pos), ball.m_radius)
        print(ball.x_vel)

        pygame.time.Clock().tick(DisplayConsts.FPS)  # respect fps for screen updates
        pygame.display.update()  # update the screen

