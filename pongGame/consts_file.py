import os
local_dir_audio = os.path.join(os.path.dirname(__file__), "audio")


class DisplayConsts:
    FPS = 30
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500
    FONT_COLOR = (255, 255, 255)
    GAME_OVER_FONT_COLOR = (200, 40, 80)
    FONT_SIZE = 70
    GAME_OVER_FONT_SIZE = 80
    FONT_TYPE = 'Comic Sans MS'
    GAME_OVER_FONT_TYPE = 'Comic Sans MS'


class AudioConsts:
    GAME_OVER_AUDIO = os.path.join(local_dir_audio, 'game_over.wav')
    SCORE_AUDIO = os.path.join(local_dir_audio, 'score.wav')


class BallConsts:
    BALL_RADIUS = 30
    BALL_STARTING_POSITION_X = 100
    BALL_STARTING_POSITION_Y = 200
    BALL_STARTING_VELOCITY_X = 10
    BALL_STARTING_VELOCITY_Y = 0


class PaddleConsts:
    PADDLE_SIZE = 30


