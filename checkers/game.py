import pygame
import logging


class MultiplierCheckers:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Wendell's Multiplier Checkers")
        self.screen = pygame.display.set_mode([800, 800])
        self.running = True

    def game_runner(self):
        logging.basicConfig(filename='game_info_output.log', level=logging.INFO)
        logging.info("Running game")
        while self.running:
            self.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
        pygame.quit()

    def draw_board(self):
        logging.info("Drawing board")
        # TODO NRL Stop from drawing board constantly
        starting_x = 0
        color_switch_bool = 0
        while starting_x <= 800:
            starting_y = 0
            while starting_y <= 800:
                if color_switch_bool == 0:
                    pygame.draw.rect(self.screen, (138, 43, 226), (starting_x, starting_y, 100, 100))
                else:
                    pygame.draw.rect(self.screen, (0, 191, 255), (starting_x, starting_y, 100, 100))
                starting_y += 100
                color_switch_bool = not color_switch_bool
            starting_x += 100

        pygame.display.flip()


def main():
    game = MultiplierCheckers()
    game.game_runner()


if __name__ == "__main__":
    main()
