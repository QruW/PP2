import pygame
import os

# Initialize Pygame
pygame.init()
# Music folder
MUSIC_FOLDER = "music/"
playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")] # all files in the folder with .mp3 extension
current_track = 0

# Load first track
if playlist:
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))
# Play and pause music via spacebar
def play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
# Next track via right arrow key
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))
    pygame.mixer.music.play()
# Previous track via left arrow key
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))
    pygame.mixer.music.play()

# Pygame window setup
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Music Player")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()
    
    screen.fill((20, 30, 40))
    pygame.display.flip()

pygame.quit()