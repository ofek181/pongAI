import pygame_menu
from pongGame.pong_module import Pong
from pongAI.run_neat import AI
from pongGame.consts_file import DisplayConsts


def main():
    pong = Pong()
    menu = pygame_menu.Menu('Pong', DisplayConsts.SCREEN_WIDTH, DisplayConsts.SCREEN_HEIGHT,
                            theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Play against the fittest neural network', AI.test)
    menu.add.button('Train a neural network with NEAT', AI.train)
    menu.add.button('Play against a human', pong.run_game)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(pong.display.screen)


if __name__ == '__main__':
    main()
