import pygame
from pongGame.display_module import Display
from pongGame.consts_file import DisplayConsts


class AlgoDisplay(Display):
    def __init__(self):
        super().__init__()

    def draw_training(self, static_paddle, paddles: list, balls: list):
        """
            Implements the animation of the ball and paddles.
                Parameters:
                    static_paddle: the static right hand paddle during training
                    paddles: list of all the paddle genomes
                    balls: list of all the balls of the game.
        """
        # clear screen
        self.screen.fill((0, 0, 0))

        # draw the scoring and middle line
        pygame.draw.line(self.screen, DisplayConsts.LINE_FONT,
                         [DisplayConsts.SCREEN_WIDTH / 2, 0],
                         [DisplayConsts.SCREEN_WIDTH / 2, DisplayConsts.SCREEN_HEIGHT],
                         DisplayConsts.LINE_WIDTH)

        # draw the balls
        for ball in balls:
            pygame.draw.circle(self.screen, DisplayConsts.FONT_COLOR, (ball.x_pos, ball.y_pos), ball.m_radius)

        # draw the left and right paddles
        rect = pygame.Rect(static_paddle.x_pos, static_paddle.y_pos,
                           static_paddle.m_size[0], static_paddle.m_size[1])
        pygame.draw.rect(self.screen, DisplayConsts.FONT_COLOR, rect)
        for paddle in paddles:
            rect = pygame.Rect(paddle.x_pos, paddle.y_pos,
                               paddle.m_size[0], paddle.m_size[1])
            pygame.draw.rect(self.screen, DisplayConsts.FONT_COLOR, rect)

        pygame.time.Clock().tick(DisplayConsts.FPS)  # respect fps for screen updates
        pygame.display.update()  # update the screen
