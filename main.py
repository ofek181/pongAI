from pongGame.display_module import Display
from pongGame.ball_module import Ball


def main():
    ball = Ball()
    display = Display()
    while True:
        display.animate_game(ball)


if __name__ == '__main__':
    main()

