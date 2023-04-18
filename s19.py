import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((700, 500))
pygame.draw.rect(screen, RED, [0, 0, 50, 50])
pygame.display.flip()

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
