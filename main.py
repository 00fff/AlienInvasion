import sys 
import pygame
import os 

# Change directory to USB
path = "E:/AlienShooter/" 
os.chdir(path)

# Important Variables
FPS = 60 
screen_height = 800
screen_width = 1200

# Create Game Window 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Shooter")

# Assets 
bg = pygame.image.load("assets/bg.jpg")
ship_img = pygame.image.load("assets/ship.png")

# Define Functions 
def draw_bg():
    screen.blit(bg, (0, 0))

# Define Classes 
class Ship:
    def __init__(self):
        self.image = pygame.transform.scale(ship_img, (100, 75))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen_width // 2, screen_height - 10)  # Position ship at the bottom center
        self.y = self.rect.y
        self.x = self.rect.x 
    
    def blitme(self):
        screen.blit(self.image, self.rect)  # Blit the image at the ship's rect position
    def update(self):   
        # makes a variable which changes depending on what button is clicked 
        dx = 0
        # makes a variable for key getting pressed 
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 1  # Move left
        if key[pygame.K_d]:
            dx += 1  # Move right
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        # Update the rect position based on the calculated dx
        self.rect.x += dx
        print(self.rect.left)
        print(dx)

# Instances 
player = Ship()
run = True 
while run:
    draw_bg()
    player.blitme()
    player.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        


pygame.quit()
