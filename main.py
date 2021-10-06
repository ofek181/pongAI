from pongGame.display_module import Display
from pongGame.ball_module import Ball
from pongGame.paddle_module import Paddle


def main():
    ball = Ball()
    paddle_bot = Paddle()
    paddle_top = Paddle(x_pos=50, y_pos=200)
    display = Display()
    while True:
        display.animate_game(paddle_bot, paddle_top, ball)
        display.show_score(2, 4)
        display.show_winner("player 1 wins!")


if __name__ == '__main__':
    main()

