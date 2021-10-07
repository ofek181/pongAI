import pygame
import pygame_menu
from .consts_file import DisplayConsts


class Display:
    """
        A class to implement the display of the game.
        ----------------------------
        Attributes
        ----------------------------
        _screen : pygame object
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
        draw_objects(self, paddle_left, paddle_right, ball):
         Uses pygame methods in order to display the ball and paddles.
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Display object.
        """
        pygame.init()
        self._screen = pygame.display.set_mode((DisplayConsts.SCREEN_WIDTH, DisplayConsts.SCREEN_HEIGHT))

    def show_winner(self, player: str):
        """
            Displays the winner over the screen.
        """
        # clear screen
        self._screen.fill((0, 0, 0))

        # draw winner
        font = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.WINNER_SIZE)
        surface = font.render(player, True, DisplayConsts.FONT_COLOR)  # Display game over
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 2, DisplayConsts.SCREEN_HEIGHT // 3)
        self._screen.blit(surface, rect)

        pygame.display.update()  # update the screen

    def __draw_screen(self, score_left: int, score_right: int):
        """
            Displays the score over the screen
        """
        # draw the scoring system
        font_left = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        surface_left = font_left.render(str(score_left), True, DisplayConsts.FONT_COLOR)  # show score
        rect_left = surface_left.get_rect()
        rect_left.midtop = (DisplayConsts.SCREEN_WIDTH // 2.4, DisplayConsts.SCREEN_HEIGHT // 20)
        self._screen.blit(surface_left, rect_left)

        font_right = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        surface_right = font_right.render(str(score_right), True, DisplayConsts.FONT_COLOR)  # show score
        rect_right = surface_right.get_rect()
        rect_right.midtop = (DisplayConsts.SCREEN_WIDTH // 1.7, DisplayConsts.SCREEN_HEIGHT // 20)
        self._screen.blit(surface_right, rect_right)

        # draw the middle line
        pygame.draw.line(self._screen, DisplayConsts.LINE_FONT,
                         [DisplayConsts.SCREEN_WIDTH / 2, 0],
                         [DisplayConsts.SCREEN_WIDTH / 2, DisplayConsts.SCREEN_HEIGHT],
                         DisplayConsts.LINE_WIDTH)

    def draw_objects(self, paddle_left, paddle_right, ball, score_left: int, score_right: int):
        """
            Implements the animation of the ball and paddles.
                Parameters:
                    paddle_left : left paddle of the game.
                    paddle_right: right paddle of the game.
                    ball: ball of the game.
                    score_left: score of left player.
                    score_right: score of right player.
        """
        # clear screen
        self._screen.fill((0, 0, 0))

        # draw the scoring and middle line
        self.__draw_screen(score_left, score_right)

        # draw the ball
        pygame.draw.circle(self._screen, DisplayConsts.FONT_COLOR, (ball.x_pos, ball.y_pos), ball.m_radius)

        # draw the left and right paddles
        rect = pygame.Rect(paddle_left.x_pos, paddle_left.y_pos,
                           paddle_left.m_size[0], paddle_left.m_size[1])
        pygame.draw.rect(self._screen, DisplayConsts.FONT_COLOR, rect)
        rect = pygame.Rect(paddle_right.x_pos, paddle_right.y_pos,
                           paddle_right.m_size[0], paddle_right.m_size[1])
        pygame.draw.rect(self._screen, DisplayConsts.FONT_COLOR, rect)

        pygame.time.Clock().tick(DisplayConsts.FPS)  # respect fps for screen updates
        pygame.display.update()  # update the screen

    def draw_menu(self, paddle_left, paddle_right, ball, score_left: int, score_right: int):
        menu = pygame_menu.Menu('Welcome', 400, 300,
                                theme=pygame_menu.themes.THEME_BLUE)

        # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
        menu.add.button('Play', self.draw_objects(paddle_left, paddle_right, ball, score_left, score_right))
        menu.add.button('Quit', pygame_menu.events.EXIT)

