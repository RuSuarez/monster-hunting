import pygame
import sys

# Define some constants for the physics properties of our character
GRAVITY = 0.6
JUMP_SPEED = 15
MOVE_SPEED = 0.8

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        super().__init__()
        # Set the initial position of the character
        self.x = x
        self.y = y
        # Set the initial velocity of the character
        self.vx = 0
        self.vy = 0
        # Set the initial acceleration of the character
        self.ax = 0
        self.ay = GRAVITY
        # Set the image of the character
        self.image = image
        # Get the width and height of the character's image
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height


    def draw(self, surface):
        """Draw the character to the specified surface."""
        surface.blit(self.image, self.rect)

    def update(self, WIDTH, HEIGHT):
        # Update the velocity based on the acceleration
        self.vx += self.ax
        self.vy += self.ay
        # Update the position based on the velocity
        self.x += self.vx
        self.y += self.vy
        # Apply friction to the character's movement
        self.vx *= 0.9
        # Check for boundary collisions and adjust the character's position if necessary
        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH - self.width:
            self.x = WIDTH - self.width
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height
            self.vy = 0
        # Update the rect attribute based on the new position
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump()
                elif event.key == pygame.K_LEFT:
                    self.ax = -MOVE_SPEED
                elif event.key == pygame.K_RIGHT:
                    self.ax = MOVE_SPEED
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.ax = 0


    def jump(self):
        # Set the character's vertical velocity to the jump speed
        if int(self.vy) < 1:
            self.vy = -JUMP_SPEED

    def collide_with_platform(self, platform):
        # Check if the character is colliding with the platform
        collide = pygame.Rect.colliderect(self.rect, platform.rect)
        # if self.rect.colliderect(platform.rect):
        if collide:
            # Calculate the overlap between the character and the platform
            overlap_x = self.rect.right - platform.rect.left
            overlap_y = self.rect.bottom - platform.rect.top
            # If the overlap is smaller in the x-direction, the character is colliding from the sides
            if overlap_x < overlap_y:
                if self.vx > 0:
                    # The character is moving to the right, so the collision is on the left side of the character
                    self.x -= overlap_x
                    self.vx = 0
                else:
                    # The character is moving to the left, so the collision is on the right side of the character
                    self.x += overlap_x
                    self.vx = 0
            # If the overlap is smaller in the y-direction, the character is colliding from above or below
            else:
                if self.vy > 0:
                    # The character is moving down, so the collision is on the top of the character
                    self.y -= overlap_y
                    self.vy = 0
                else:
                    # The character is moving up, so the collision is on the bottom of the character
                    self.y += overlap_y
                    self.vy = 0

