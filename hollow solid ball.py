import pygame

pygame.init()
window = pygame.display.set_mode((1500, 800))
window.fill((255, 255, 255))

GREEN = (0, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.draw.circle(window, GREEN, (150, 20), 75)
    pygame.draw.circle(window, GREEN, (150, 200), 50, 3)
    pygame.display.update()
pygame.quit()