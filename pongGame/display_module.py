import pygame
from .consts_file import DisplayConsts


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
        show_winner(self):
         Displays the winner of the match.
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
        self.screen = pygame.display.set_mode((DisplayConsts.SCREEN_WIDTH, DisplayConsts.SCREEN_HEIGHT))

    def show_winner(self, player: str):
        """
            Displays the winner over the screen.
        """
        font = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.WINNER_SIZE)
        surface = font.render(player, True, DisplayConsts.FONT_COLOR)  # Display game over
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 2, DisplayConsts.SCREEN_HEIGHT // 3)
        self.screen.blit(surface, rect)
        pygame.display.update()  # update the screen

    def show_score(self, score_left: int, score_right: int):
        """
            Displays the score over the screen
        """
        font_left = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        surface_left = font_left.render(str(score_left), True, DisplayConsts.FONT_COLOR)  # show score
        rect_left = surface_left.get_rect()
        rect_left.midtop = (DisplayConsts.SCREEN_WIDTH // 2.4, DisplayConsts.SCREEN_HEIGHT // 20)
        self.screen.blit(surface_left, rect_left)

        font_right = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        surface_right = font_right.render(str(score_right), True, DisplayConsts.FONT_COLOR)  # show score
        rect_right = surface_right.get_rect()
        rect_right.midtop = (DisplayConsts.SCREEN_WIDTH // 1.7, DisplayConsts.SCREEN_HEIGHT // 20)
        self.screen.blit(surface_right, rect_right)

        pygame.display.update()  # update the screen

    def animate_game(self, paddle_left, paddle_right, ball):
        """
            Implements the game animation on the screen attribute.
                Parameters:
                    paddle_left : left paddle of the game.
                    paddle_right: right paddle of the game.
                    ball: ball of the game.
        """
        # draw the ball
        pygame.draw.circle(self.screen, DisplayConsts.FONT_COLOR, (ball.x_pos, ball.y_pos), ball.m_radius)

        # draw the left and right paddles
        paddle_rect_bot = pygame.Rect(paddle_left.x_pos, paddle_left.y_pos,
                                      paddle_left.m_size[0], paddle_left.m_size[1])
        pygame.draw.rect(self.screen, DisplayConsts.FONT_COLOR, paddle_rect_bot)

        paddle_rect_top = pygame.Rect(paddle_right.x_pos, paddle_right.y_pos,
                                      paddle_right.m_size[0], paddle_right.m_size[1])
        pygame.draw.rect(self.screen, DisplayConsts.FONT_COLOR, paddle_rect_top)

        # draw middle line
        pygame.draw.line(self.screen, DisplayConsts.LINE_FONT,
                         [DisplayConsts.SCREEN_WIDTH / 2, 0],
                         [DisplayConsts.SCREEN_WIDTH / 2, DisplayConsts.SCREEN_HEIGHT],
                         DisplayConsts.LINE_WIDTH)

        pygame.time.Clock().tick(DisplayConsts.FPS)  # respect fps for screen updates
        pygame.display.update()  # update the screen

