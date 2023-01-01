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

# Set the character image
# character_image = pygame.image.load('.\character_images\SpriteSheet.png')
character_image = pygame.image.load('character.png')
width = character_image.get_rect().width
height = character_image.get_rect().height
character_image = pygame.transform.scale(character_image, (width/3.5, height/3.5))
character = Character(100, 100, character_image)

# Get the character image size
character_size = character_image.get_size()

# Set the character starting position
character_position = [0, 600 - height/3]

# Set the character speed (pixels per frame)
character_speed = 5

# Set the game clock
clock = pygame.time.Clock()

# Main game loop
while True:

    # Handle events
    character.handle_key_events()

    # Update the character's position
    character.update(WIDTH, HEIGHT)

    # Check for collisions with the platform
    plat = Platform(WIDTH/2, HEIGHT/1.3, 100, 20)
    character.collide_with_platform(plat)

    # Clear the screen
    screen.fill('white')

    pygame.draw.rect(screen, (255, 0, 0), plat)
    # debug([int(x) for x in character_position])
    # debug(f'{str(int(character.x))}, {str(int(character.y))}')
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
