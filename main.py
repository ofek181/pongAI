from pongGame.display_module import Display
from pongGame.ball_module import Ball
from pongGame.paddle_module import Paddle


def main():
    ball = Ball()
    paddle_bot = Paddle()
    paddle_top = Paddle(x_pos=50, y_pos=200)
    display = Display()
    while True:
        display.animate_game(ball, paddle_bot, paddle_top)


if __name__ == '__main__':
    main()

