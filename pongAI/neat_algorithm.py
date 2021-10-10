import random
import pygame
import neat
import sys
import pickle
from random import randrange
from .algorithm_display import AlgoDisplay
from pongGame.pong_module import Pong
from pongGame.ball_module import Ball
from pongGame.paddle_module import Paddle
from pongGame.event_handler_module import EventHandler
from pongGame.physics_module import Physics
from pongGame.consts_file import BallConsts, GameConsts, DisplayConsts, Action, AudioConsts

global generation


class NeatAI:
    """
        A class implementing the NEAT algorithm on flappyGame.
        ----------------------------
        Methods
        ----------------------------
        eval_genomes(genomes, config):
            Evaluates all genome of birds by pre defined fitness.
        test(config_path, genome_path):
            Loads the winner network and runs the flappy bird game.
        train(config_file):
            Runs the NEAT algorithm to learn how to play flappy bird.

    """
    @staticmethod
    def eval_genomes(genomes, config):
        """
            Evaluates all genome of birds by pre defined fitness.
            :param
                 genomes: each genome includes a list of connection genes.
                 config: the NEAT config file.
            :return:
                None
        """
        # initialize parameters
        global generation
        generation += 1
        neural_networks = []
        balls = []
        paddles = []
        static_paddle = Paddle(x_pos=DisplayConsts.SCREEN_WIDTH - 50, y_pos=0,
                               size=[10, DisplayConsts.SCREEN_HEIGHT])
        genes = []
        display = AlgoDisplay()
        for genome_id, genome in genomes:
            genome.fitness = 0
            network = neat.nn.FeedForwardNetwork.create(genome, config)
            neural_networks.append(network)
            balls.append(Ball(x_vel=random.randint(1, 4), y_vel=randrange(-2, 2)))
            paddles.append(Paddle(x_pos=50, y_pos=DisplayConsts.SCREEN_HEIGHT//2))
            genes.append(genome)

        # game loop for each generation
        while len(balls) > 0:
            # game display and event handling
            display.draw_training(static_paddle=static_paddle, paddles=paddles, balls=balls)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            # move the balls and check collisions
            for index, ball in enumerate(balls):
                ball.move()
                new_vel = Physics.calc_ball_velocity(ball, paddles[index], static_paddle)
                ball.x_vel, ball.y_vel = new_vel.x_vel, new_vel.y_vel

            # remove paddle and ball if the ball is out of screen
            for index, ball in enumerate(balls):
                if ball.x_pos <= 0:
                    genes[index].fitness -= 5
                    neural_networks.pop(index)
                    genes.pop(index)
                    balls.pop(index)
                    paddles.pop(index)

            # reinforce the winning paddles for each living frame
            for index, paddle in enumerate(paddles):
                genes[index].fitness += 0.1
                output = neural_networks[index].activate((balls[index].x_vel, balls[index].y_vel,
                                                         balls[index].x_pos, balls[index].y_pos,
                                                         paddle.x_pos, paddle.y_pos))

                # move paddle up
                if output[0] >= 0.5:
                    paddle.move(-paddle.y_vel)

                # move paddle down
                if output[0] <= -0.5:
                    paddle.move(paddle.y_vel)

                # do nothing
                if -0.5 < output[0] < 0.5:
                    continue

    @staticmethod
    def test(config_path, genome_path="flappyNEAT/winner.pkl"):
        """
            Loads the winner network and runs the flappy bird game
            :param
                config_file: location of config file.
                genome_path: winner network.
            :return:
                None
            """
        # Load NEAT config
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                    neat.DefaultStagnation, config_path)

        # Unpickle saved winner
        with open(genome_path, "rb") as f:
            genome = pickle.load(f)

        # audio parameters
        pygame.mixer.init()
        hit_sound = pygame.mixer.Sound(AudioConsts.HIT_AUDIO)
        score_sound = pygame.mixer.Sound(AudioConsts.SCORE_AUDIO)
        channel1 = pygame.mixer.Channel(0)

        # # initialization
        # ball = Ball()
        # paddle_left =
        # bird = Bird()
        # floor = Floor()
        # display = flappyGame.Display()
        # game_over_manager = Game()
        # neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
        #
        # while True:
        #     # game display and event handling
        #     display.animate_game(bird=bird,pipe_pairs=pipes,floor=floor)
        #     display.show_score(bird=bird)
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()
        #         elif event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_ESCAPE:
        #                 pygame.event.post(pygame.event.Event(pygame.QUIT))
        #
        #     # remove pipe if it moves out of screen and append another pipe to the list
        #     if pipes[0].x + consts.PipeConsts.TOP_IMAGE.get_width() < 0:
        #         pipes.pop(0)  # remove the passed pipe
        #         pipes.append(PipePair(pipes[-1].x + consts.PipeConsts.HORIZONTAL_GAP,
        #                               velocity=pipes[-1].velocity))  # append another pipe
        #
        #     # check score of bird
        #     if Logic.check_score(bird=bird, closest_pipe=closest_pipe):
        #         channel2.play(score_sound)
        #         bird.score += 1
        #         closest_pipe = pipes[1]
        #         next_pipe = pipes[2]
        #
        #     bird.move()
        #     delta_y_closest = abs(bird.y - closest_pipe.bot_pipe_head)
        #     delta_x_closest = abs(bird.x - closest_pipe.x)
        #     delta_y_next = abs(bird.y - next_pipe.bot_pipe_head)
        #     delta_x_next = abs(bird.x - next_pipe.x)
        #
        #     output = neural_network.activate((bird.velocity, closest_pipe.velocity,
        #                                       delta_x_closest, delta_y_closest,
        #                                       delta_x_next, delta_y_next))
        #
        #     # jump if output neuron returns value over 0.5
        #     if output[0] > 0.5:
        #         bird.jump()
        #
        #     # move all pipes
        #     for pipe in pipes:
        #         pipe.move()
        #
        #     # move the floor
        #     floor.move()
        #
        #     if Logic.check_collision(floor, closest_pipe, bird):
        #         channel1.play(game_over_sound)
        #         while True:
        #             display.show_game_over()
        #             display.animate_game(bird, pipes, floor)
        #             # animate bird falling
        #             if bird.y + bird.bird_image.get_height() <= floor.y:
        #                 bird.move()
        #
        #             # exit the game
        #             for event in pygame.event.get():
        #                 if event.type == pygame.QUIT:
        #                     pygame.quit()
        #                     sys.exit()
        #                 elif event.type == pygame.KEYDOWN:
        #                     if event.key == pygame.K_ESCAPE:
        #                         pygame.event.post(pygame.event.Event(pygame.QUIT))

    @staticmethod
    def train(config_file):
        """
            Runs the NEAT algorithm to learn how to play flappy bird.
            :param
                config_file: location of config file
            :return:
                saves the defined winner in a pkl file
            """
        global generation
        generation = 0
        # Load configuration.
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             config_file)

        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(config)

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)

        # Run for up to 100 generations.
        winner = p.run(NeatAI.eval_genomes, 100)

        with open("pongAI/winner.pkl", "wb") as f:
            pickle.dump(winner, f)
            f.close()

        # Display the winning genome.
        print('\nBest genome:\n{!s}'.format(winner))


