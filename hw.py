import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red vs Blue")

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BG = (30, 30, 30)

# Sprite rectangles
player = pygame.Rect(100, 150, 50, 50)  # Controlled rectangle
enemy = pygame.Rect(300, 150, 50, 50)   # Static rectangle


# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Keep player inside screen
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    # Draw sprites
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, enemy)

    pygame.display.flip()

pygame.quit()
sys.exit()
