import pygame

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)  # Red
BG_COLOR = (255, 255, 255)  # White
STEP = 20

# Initial ball position
x, y = WIDTH // 2, HEIGHT // 2

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
running = True

while running:
    screen.fill(BG_COLOR)  # Clear screen
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)  # Draw ball
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - BALL_RADIUS - STEP >= 0:
                y -= STEP
            elif event.key == pygame.K_DOWN and y + BALL_RADIUS + STEP <= HEIGHT:
                y += STEP
            elif event.key == pygame.K_LEFT and x - BALL_RADIUS - STEP >= 0:
                x -= STEP
            elif event.key == pygame.K_RIGHT and x + BALL_RADIUS + STEP <= WIDTH:
                x += STEP

pygame.quit()