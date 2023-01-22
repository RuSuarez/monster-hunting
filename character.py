import pygame
import sys
import os

# Define some constants for the physics properties of our character
GRAVITY = 0.8
JUMP_SPEED = 15
MOVE_SPEED = 0.6

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y):
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
        # Running frames
        self.frames_run = []
        for file_name in os.listdir('images/hero_sprites/run/'):
            self.frames_run.append(pygame.image.load(f"images/hero_sprites/run/{file_name}")) 
        # Jumping frames
        self.frames_jump = []
        for file_name in os.listdir('images/hero_sprites/jump/'):
            self.frames_jump.append(pygame.image.load(f"images/hero_sprites/jump/{file_name}")) 
        # Falling frames
        self.frames_fall = []
        for file_name in os.listdir('images/hero_sprites/fall/'):
            self.frames_fall.append(pygame.image.load(f"images/hero_sprites/fall/{file_name}"))   
        # Idle frames
        self.frames_idle = []
        for file_name in os.listdir('images/hero_sprites/idle/'):
            self.frames_idle.append(pygame.image.load(f"images/hero_sprites/idle/{file_name}"))    
        self.current_frame = 0
        self.image = self.frames_run[self.current_frame]
        self.frame_rate = 0.035
        # Get the width and height of the character's image
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        # Set animations


    def draw(self, surface):
        """Draw the character to the specified surface."""
        surface.blit(self.image, self.rect)

    def update(self, WIDTH, HEIGHT, time_passed_seconds):
        # Update the velocity based on the acceleration
        self.vx += self.ax
        self.vy += self.ay
        # Update the position based on the velocity
        self.x += self.vx
        if self.vx > 0:
            going_right = True
        else:
            going_right = False
        self.y += self.vy
        # Apply friction to the character's movement
        self.vx *= 0.8
        # Check for boundary collisions and adjust the character's position if necessary
        max_out_window = 30
        if self.x < -max_out_window:
            self.x = WIDTH - self.width + max_out_window
        elif self.x > WIDTH - self.width + max_out_window:
            self.x = -max_out_window
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height
            self.vy = 0
        # Update the rect attribute based on the new position
        keys = pygame.key.get_pressed()

        if self.vy < 0:
            self.current_frame += time_passed_seconds / self.frame_rate
            if self.current_frame >= len(self.frames_jump):
                self.current_frame = 0
            if self.vx >= 0:
                self.image = self.frames_jump[int(self.current_frame)]
            else:
                self.image = pygame.transform.flip(self.frames_jump[int(self.current_frame)], True, False)

        elif self.vy > 0:
            self.current_frame += time_passed_seconds / self.frame_rate
            if self.current_frame >= len(self.frames_fall):
                self.current_frame = 0
            if self.vx >= 0:
                self.image = self.frames_fall[int(self.current_frame)]
            else:
                self.image = pygame.transform.flip(self.frames_fall[int(self.current_frame)], True, False)

        elif keys[pygame.K_RIGHT]:
            self.current_frame += time_passed_seconds / self.frame_rate
            if self.current_frame >= len(self.frames_run):
                self.current_frame = 0
            self.image = self.frames_run[int(self.current_frame)]

        elif keys[pygame.K_LEFT]:
            self.current_frame += time_passed_seconds / self.frame_rate
            if self.current_frame >= len(self.frames_run):
                self.current_frame = 0
            self.image = pygame.transform.flip(self.frames_run[int(self.current_frame)], True, False)

        else:
            self.current_frame += time_passed_seconds / self.frame_rate
            if self.current_frame >= len(self.frames_idle):
                self.current_frame = 0
            if going_right:
                self.image = self.frames_idle[int(self.current_frame)]
            else:
                self.image = pygame.transform.flip(self.frames_idle[int(self.current_frame)], True, False)

        # Updating rect
        self.rect.x = self.x
        self.rect.y = self.y

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and  self.vy == 0:
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
            # Updating rect
            self.rect.x = self.x
            self.rect.y = self.y

