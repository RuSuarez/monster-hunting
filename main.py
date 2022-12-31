import pygame as pg
import sys
from debugging import debug

# Initialize Pygame
pg.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pg.display.set_mode(window_size)

# Set the title of the window
pg.display.set_caption('Pygame Game')

# Set the character image
character_image = pg.image.load('character.png')
width = character_image.get_rect().width
height = character_image.get_rect().height
character_image = pg.transform.scale(character_image, (width/3.5, height/3.5))

# Get the character image size
character_size = character_image.get_size()

# Set the character starting position
character_position = [0, 600 - height/3]

# Set the character speed (pixels per frame)
character_speed = 5

# Set the game clock
clock = pg.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Get the keys that are currently pressed
    keys = pg.key.get_pressed()

    # Move the character based on the arrow keys
    if keys[pg.K_UP]:
        character_position[1] -= character_speed
    if keys[pg.K_DOWN]:
        character_position[1] += character_speed
    if keys[pg.K_LEFT]:
        character_position[0] -= character_speed
    if keys[pg.K_RIGHT]:
        character_position[0] += character_speed

    # Clear the screen
    screen.fill('white')
    debug([int(x) for x in character_position])

    # Draw the character
    screen.blit(character_image, character_position)

    # Update the display
    pg.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)
