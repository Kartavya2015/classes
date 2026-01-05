import pygame

pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("A Pygame Window")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()