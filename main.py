import pygame
import sys
from debugging import debug
from character import Character
from plat import Platform
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1500, 600)
WIDTH = window_size[0]
HEIGHT = window_size[1]

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Pygame Game')

character = Character(100, 100)

# Set the character starting position
character_position = [0, 600 - HEIGHT/3]

# Set the character speed (pixels per frame)
character_speed = 5

# Set the game clock
clock = pygame.time.Clock()

# Main game loop
while True:

    # Handle events
    character.handle_key_events()

    time_passed = clock.tick(120)
    time_passed_seconds = time_passed / 1000.0
    # Update the character's position
    character.update(WIDTH, HEIGHT, time_passed_seconds)

    # Check for collisions with the platform
    plat = Platform(WIDTH/2, HEIGHT/1.2, 100, 20)
    character.collide_with_platform(plat)

    # Clear the screen
    screen.fill('white')

    pygame.draw.rect(screen, (255, 0, 0), plat)
    # debug([int(x) for x in character_position])
    debug(f'{str(int(character.x))}, {str(int(character.y))}', 30)
    debug(character.rect, 60)
    debug(character.vy, 90)
    debug(f'{str(int(plat.x))}, {str(int(plat.y))}')
    # debug(character.vy)
    # debug(pygame.Rect.colliderect(character.rect, plat.rect), 30)

    # if int(character.y) != 491:
    #     print(character.vy)

    # Draw the character
    screen.blit(character.image, (character.x, character.y))

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)
