import pygame
import random

pygame.init()
# Custom event id for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Bg colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# sprite color
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


class Sprtie(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        # Create sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Get the sprite's rect defining its position and size
        self.rect = self.image.get_rect()
        # Set velocity
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Method to update sprites position
    def update(self):
        # Move sprite by velocity
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        # Check for collisions with left or right boundaries
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
                

    def color_change(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

def change_bgcolor():
    global Back_color
    Back_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


sprite_list = pygame.sprite.Group()
sp1 = Sprtie(WHITE, 20, 30)
# randomly positions sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

sprite_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Color changing sprite and background')

Back_color = BLUE
screen.fill(Back_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.color_change()

        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_bgcolor()
    sprite_list.update()
    screen.fill(Back_color)
    sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(420)
pygame.quit()
