import pygame
from pygame.locals import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # Set the position and size of the platform
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Create a bounding box for the platform
        self.rect = pygame.Rect(x, y, width, height)
