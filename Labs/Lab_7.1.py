import pygame
import time
import math

# Initialize Pygame
pygame.init()

# Constants for the future using
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
WIDTH2, HEIGHT2 = 150, 150

# Load images
mickey_img = pygame.image.load("mickeyclock.jpeg")  # Background Mickey Mouse image
right_hand_img = pygame.image.load("right_hand.png")  # Minutes hand
left_hand_img = pygame.image.load("left_hand.png")  # Seconds hand

# Scaling images
# Assuming the hand images are larger than the clock size, we scale them down
mickey_img = pygame.transform.scale(mickey_img, (WIDTH, HEIGHT))
right_hand_img = pygame.transform.scale(right_hand_img, (WIDTH2, HEIGHT2))
left_hand_img = pygame.transform.scale(left_hand_img, (WIDTH2, HEIGHT2))

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(mickey_img, (0, 0))  # Settting background
    
    # Get current time
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    # Calculate angles
    min_angle = - (minutes * 6)  # 360 degrees / 60 minutes = 6 degrees per minute
    sec_angle = - (seconds * 6)  # 360 degrees / 60 seconds = 6 degrees per second
    # The angle is negative because Pygame rotates clockwise
    # Rotate hands with using pygame.transform.rotate
    
    min_hand = pygame.transform.rotate(right_hand_img, min_angle)
    sec_hand = pygame.transform.rotate(left_hand_img, sec_angle)
    
    # Get hand rects and adjust position
    min_rect = min_hand.get_rect(center=CENTER)
    sec_rect = sec_hand.get_rect(center=CENTER)
    
    # Setting hands images
    screen.blit(min_hand, min_rect.topleft)
    screen.blit(sec_hand, sec_rect.topleft)
    
    # Update display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)  # Run at 60 FPS

pygame.quit()