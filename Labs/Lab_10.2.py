import pygame
from color_palette import *  
import random
import time
import psycopg2

pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 20)

# Database connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Tr3301du",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# User login
username = input("Enter your username: ")
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
result = cur.fetchone()

if result: # If user exists, then get progression
    user_id = result[0]
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    last_game = cur.fetchone()
    if last_game:
        score, level = last_game
        print(f"Welcome back {username}! Resuming from level {level} with score {score}.")
    else:
        score, level = 0, 1
else: # If user doesn't exist, create a new user
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    score, level = 0, 1
    print(f"Welcome new user {username}!")

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

    def move(self, wall):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i - 1].x, self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        head = self.body[0]

        # Collision with walls
        for block in wall.body:
            if head.x == block.x and head.y == block.y:
                return False

        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            return False
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
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
            self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            self.nominal = random.randint(1, 3)
            self.color = [colorRED, colorORANGE, colorYELLOW][self.nominal - 1]
            self.timer = time.time() + random.randint(5, 10)
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake_body):
                break

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class Wall: # new class for walls
    def __init__(self):
        self.body = []

    def load_level(self, level): # load level from files where walls are # and blank space are .
        self.body = []
        try:
            with open(f"level{level}.txt", "r") as f:
                for y, line in enumerate(f):
                    for x, char in enumerate(line.strip()):
                        if char == "#":
                            self.body.append(Point(x, y))
        except FileNotFoundError: # for now I created only five levels
            print(f"For now this is all, please wait future updates!")

    def draw(self): # draw walls from txt files
        for wall in self.body:
            pygame.draw.rect(screen, colorWHITE, (wall.x * CELL, wall.y * CELL, CELL, CELL))

FPS = 5
clock = pygame.time.Clock()
snake = Snake()
food = Food()
wall = Wall()
wall.load_level(level)

paused = False
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
            elif event.key == pygame.K_p: # new key for pause
                paused = not paused
                if paused: # if paused, save the score and level to the database
                    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                    conn.commit()

    if not paused: # if not paused, then game will resume
        if not snake.move(wall):
            running = False

        if time.time() > food.timer:
            food.generate_random_pos(snake.body)

        gained_score = snake.check_collision(food)
        if gained_score:
            score += gained_score
            food.generate_random_pos(snake.body)
            if score // 10 + 1 > level:
                level = score // 10 + 1
                FPS += 2
                wall.load_level(level) # every new level also save score
                cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                conn.commit()

    screen.fill(colorBLACK)
    draw_grid()
    wall.draw()
    snake.draw()
    food.draw()
    screen.blit(font.render(f"Score: {score}", True, colorYELLOW), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, colorYELLOW), (10, 40))

    if paused: # pause menu
        pause_overlay = pygame.Surface((WIDTH, HEIGHT))
        pause_overlay.set_alpha(180)
        pause_overlay.fill((50, 50, 50))
        screen.blit(pause_overlay, (0, 0))
        pause_text = font.render("PAUSED", True, colorWHITE)
        instruction_text = font.render("Press 'P' to resume", True, colorWHITE)
        screen.blit(pause_text, (WIDTH // 2 - 50, HEIGHT // 2 - 30))
        screen.blit(instruction_text, (WIDTH // 2 - 100, HEIGHT // 2 + 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
cur.close()
conn.close()