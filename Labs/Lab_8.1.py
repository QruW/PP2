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

# Set up the title and icon
player_img = pygame.image.load('resources/Player.png')
enemy_img = pygame.image.load('resources/Enemy.png')
coin_img = pygame.image.load('resources/Coin.png')

background_music = pygame.mixer.music.load('resources/background.wav')
crash_sound = pygame.mixer.Sound('resources/crash.wav')

font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

# Set up the game music
pygame.mixer.music.play(-1)

# Set up the objects speeds
PLAYER_SPEED = 5
ENEMY_SPEED = 10
COIN_SPEED = 5

score = 0

# Define the player, enemy, and coin classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img # Load the player image
        self.rect = self.image.get_rect() # Get the rectangle of the image
        self.rect.x = WIDTH // 2 - self.rect.w // 2 # Center the player
        self.rect.y = HEIGHT - self.rect.h # Position the player at the bottom of the screen
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # Move left
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]: # Move right
            self.rect.move_ip(PLAYER_SPEED, 0)
        if self.rect.left < 0: # Prevent going out of bounds
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.generate_random_rect() # Generate a random position for the enemy
    
    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT: # If the enemy goes off the screen, generate a new random position
            self.generate_random_rect() # Generate a new random position
    
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w) # Random x position
        self.rect.y = random.randint(-HEIGHT, -50) # Start from the above the screen, which is more good looking

# For coin used same class configuration as enemy
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.generate_random_rect()
    
    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
    
    def generate_random_rect(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-HEIGHT, -50)

# define the player, enemy, and coin objects
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group() 
enemy_sprites = pygame.sprite.Group() 
coin_sprites = pygame.sprite.Group() 

# Add the player, enemy, and coin to the sprite groups
# This allows for easier collision detection and rendering
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
    # Check for coin collection
    # If the player collects a coin, increase the score and generate a new coin
    if pygame.sprite.spritecollideany(player, coin_sprites):
        score += 1
        coin.generate_random_rect()
    
    score_text = small_font.render(f"Coins: {score}", True, "black")
    screen.blit(score_text, (WIDTH - 100, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()