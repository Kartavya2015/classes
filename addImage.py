import pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Display")

backgroundImage = pygame.transform.scale(
    pygame.image.load("OIP.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin = pygame.image.load("OIP (1).jpg").convert_alpha()

penguin_Rect = penguin.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    display_surface = pygame.display.get_surface()
    display_surface.blit(backgroundImage, (0, 0))
    display_surface.blit(penguin, penguin_Rect)
    clock.tick(60)

pygame.quit()
