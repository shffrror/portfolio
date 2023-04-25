import pygame
pygame.init()

screen = pygame.display.set_mode([800, 800])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 0), (250, 250), 75)

    starting_x = 0
    starting_y = 0
    red_black_bool_track = 0
    while starting_x <= 800:
        starting_y = 0
        while starting_y <= 800:
            if red_black_bool_track == 0:
                pygame.draw.rect(screen, (255, 0, 0), (starting_x, starting_y, 100, 100))
            else:
                pygame.draw.rect(screen, (0, 0, 255), (starting_x, starting_y, 100, 100))
            starting_y += 100
            red_black_bool_track = not red_black_bool_track

        starting_x += 100

    # pygame.draw.rect(window, color, (x, y, width, height)

    pygame.display.flip()

pygame.quit()