import pygame
import logging


class MultiplierCheckers:
    def __init__(self):
        #logging.basicConfig(filename='game_info_output.log', level=logging.INFO)
        pygame.init()
        pygame.display.set_caption("Wendell's Multiplier Checkers")
        self.screen = pygame.display.set_mode([800, 800])
        self.running = True
        # Checkers are stored as a list of lists with values [x_coordinate, y_coordinate, multiplier]
        self.black_checkers = [[150, 50, 0], [350, 50, 0], [550, 50, 0], [750, 50, 0], [50, 150, 0], [250, 150, 0],
                               [450, 150, 0], [650, 150, 0], [150, 250, 0], [350, 250, 0], [550, 250, 0], [750, 250, 0]]
        self.white_checkers = [[50, 550, 0], [250, 550, 0], [450, 550, 0], [650, 550, 0], [150, 650, 0], [350, 650, 0],
                               [550, 650, 0], [750, 650, 0], [50, 750, 0], [250, 750, 0], [450, 750, 0], [650, 750, 0]]

    def game_runner(self):
        logging.info("Running game")
        self.draw_board()
        self.set_pieces()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click()
        pygame.quit()

    def handle_click(self):
        click_position = pygame.mouse.get_pos()
        self.determine_click_square(click_position)

    # Handles determining where a specific click coordinate falls on board squares
    def determine_click_square(self, coordinates):
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[1]
        # Each square is 100 size
        # Calculate if mod > 0 where x >= lower_limit of square range and x <= upper_limit
        print(x_coordinate)
        print(y_coordinate)

    def set_pieces(self):
        logging.info("Setting pieces")
        for location in self.black_checkers:
            pygame.draw.circle(self.screen, (0, 0, 0), (location[0], location[1]), 50)
        for location in self.white_checkers:
            pygame.draw.circle(self.screen, (255, 255, 255), (location[0], location[1]), 50)

        pygame.display.flip()

    def draw_board(self):
        logging.info("Drawing board")
        x_coordinate = 0
        color_switch_bool = 0
        while x_coordinate <= 800:
            y_coordinate = 0
            while y_coordinate <= 800:
                if color_switch_bool == 0:
                    pygame.draw.rect(self.screen, (138, 43, 226), (x_coordinate, y_coordinate, 100, 100))
                else:
                    pygame.draw.rect(self.screen, (0, 191, 255), (x_coordinate, y_coordinate, 100, 100))
                y_coordinate += 100
                color_switch_bool = not color_switch_bool
            x_coordinate += 100

        pygame.display.flip()


def main():
    game = MultiplierCheckers()
    game.game_runner()


if __name__ == "__main__":
    main()
