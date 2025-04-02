import pygame
from color_palette import *
import random
import time

pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 20)

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y): 
        self.x, self.y = x, y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i - 1].x, self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL:
            return False
        for segment in self.body[1:]:
            if self.body[0].x == segment.x and self.body[0].y == segment.y:
                return False
        return True

    def draw(self):
        pygame.draw.rect(screen, colorBLUE, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorGREEN, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return food.nominal
        return 0

class Food:
    def __init__(self):
        self.generate_random_pos([])

    def generate_random_pos(self, snake_body):
        while True:
            self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)) # Random food spawn position
            self.nominal = random.randint(1, 3) # Different food nominal values
            self.color = [colorRED, colorORANGE, colorYELLOW][self.nominal - 1] # Different food colors according to nominal values
            self.timer = time.time() + random.randint(5, 10)  # Disappears after 5-10 sec (timer)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake_body):
                break

# In othersides there is no changes, only the class Food is changed.

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

FPS, score, level = 5, 0, 1
clock, snake, food = pygame.time.Clock(), Snake(), Food()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    screen.fill(colorBLACK)
    draw_grid()

    if not snake.move():
        running = False

    food_time = time.time()
    if food_time > food.timer:
        food.generate_random_pos(snake.body)

    gained_score = snake.check_collision(food)
    if gained_score:
        score += gained_score
        food.generate_random_pos(snake.body)
        if score % 3 == 0:
            level += 1
            FPS += 2

    snake.draw()
    food.draw()

    screen.blit(font.render(f"Score: {score}", True, colorYELLOW), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, colorYELLOW), (10, 40))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()