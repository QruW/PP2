import pygame
import random
import time

pygame.init()

# Set up the screen
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('resources/AnimatedStreet.png')

running = True

# Set up the FPS
clock = pygame.time.Clock()
FPS = 60 

# Load images
player_img = pygame.image.load('resources/Player.png')
enemy_img = pygame.image.load('resources/Enemy.png')
coin_images = {
    1: pygame.image.load('resources/Coin.png'), # Load the first coin image for nominal 1
    2: pygame.image.load('resources/Coin1.png'), # Load the second coin image for nominal 2
    3: pygame.image.load('resources/Coin2.png') # Load the third coin image for nominal 3
}

# Load sounds
background_music = pygame.mixer.music.load('resources/background.wav')
crash_sound = pygame.mixer.Sound('resources/crash.wav')

font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

# Play background music
pygame.mixer.music.play(-1)

# Set up the game parameters
PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 5

score = 0
COIN_THRESHOLD = 10  # Increase enemy speed after collecting 10 points

# Define the player, enemy, and coin classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-HEIGHT, -50)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nominal = random.randint(1, 3)  # Coin value between 1-3
        self.image = coin_images[self.nominal]
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    
    def generate_random_rect(self):
        self.nominal = random.randint(1, 3)  # Assign new value
        self.image = coin_images[self.nominal]  # Update image
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-HEIGHT, -50)

# Initialize objects
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add([player, enemy, coin])
enemy_sprites.add(enemy)
coin_sprites.add(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    
    player.move()
    enemy.move()
    coin.move()
    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    # Check for collisions
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)
        screen.fill("red")
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False
    
    if pygame.sprite.spritecollideany(player, coin_sprites):
        score += coin.nominal  # Add the nominal value of the coin
        coin.generate_random_rect()
    
    # Increase enemy speed when reaching threshold
    if score >= COIN_THRESHOLD:
        ENEMY_SPEED += 2
        COIN_THRESHOLD += 10  # Increase threshold for next speed up
    
    # Display score
    score_text = small_font.render(f"Coins: {score}", True, "black")
    screen.blit(score_text, (WIDTH - 100, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()