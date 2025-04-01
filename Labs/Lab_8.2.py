import pygame
from color_palette import *
import random

pygame.init()
# Set up the screen dimensions and cell size
WIDTH = 600
HEIGHT = 600
CELL = 30
# Set up the colors
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 20)
# Define the grid
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)
# Define the classes for the points, snake and food
class Point:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self): 
        for i in range(len(self.body) - 1, 0, -1): 
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx # Move the head of the snake
        self.body[0].y += self.dy # Move the body of the snake

        if self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL: # Check for wall collisions
            return False

        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y: ## Check for self-collisions
                return False
        
        return True

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorBLUE, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorGREEN, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)
            return True
        return False

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake_body):
                break
# Initialize the game
FPS = 5
score = 0
level = 1
clock = pygame.time.Clock()
food = Food()
snake = Snake()
# Set up the moving functionality
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)
    draw_grid()
# If the snake moves out of bounds or collides with itself, the game ends
    # Check for collisions with walls or itself
    if not snake.move():
        running = False
# Check for collisions with food
    # If the snake eats the food, increase the score and generate a new food
    if snake.check_collision(food):
        score += 1
        if score % 3 == 0: # Increase level every 3 points
            level += 1 
            FPS += 2 # Increase speed with each level
    
    snake.draw()
    food.draw()
# Display the score and level
    score_text = font.render(f"Score: {score}", True, colorYELLOW)
    level_text = font.render(f"Level: {level}", True, colorYELLOW)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
