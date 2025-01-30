import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GDG on Campus Meetup")
clock = pygame.time.Clock()

# Colors
PURPLE = (149, 0, 255)  # Google's purple
WHITE = (255, 255, 255)
BLUE = (66, 133, 244)   # Google's blue
RED = (234, 67, 53)     # Google's red
YELLOW = (251, 188, 5)  # Google's yellow
GREEN = (52, 168, 83)   # Google's green

# Font setup
title_font = pygame.font.Font(None, 74)
subtitle_font = pygame.font.Font(None, 48)

# Text setup
title_text = title_font.render("GDG on Campus", True, WHITE)
subtitle_text = subtitle_font.render("Building Chrome Dino Game with Python", True, WHITE)
start_text = subtitle_font.render("Press SPACE to begin!", True, WHITE)

# Position setup
title_pos = ((SCREEN_WIDTH - title_text.get_width()) // 2, SCREEN_HEIGHT // 3)
subtitle_pos = ((SCREEN_WIDTH - subtitle_text.get_width()) // 2, SCREEN_HEIGHT // 2)
start_pos = ((SCREEN_WIDTH - start_text.get_width()) // 2, SCREEN_HEIGHT * 2 // 3)

# Animation variables
circle_radius = 20
circles = [
    {'pos': [SCREEN_WIDTH//2 - 90, SCREEN_HEIGHT//4], 'color': BLUE},
    {'pos': [SCREEN_WIDTH//2 - 30, SCREEN_HEIGHT//4], 'color': RED},
    {'pos': [SCREEN_WIDTH//2 + 30, SCREEN_HEIGHT//4], 'color': YELLOW},
    {'pos': [SCREEN_WIDTH//2 + 90, SCREEN_HEIGHT//4], 'color': GREEN}
]

running = True
animation_speed = 2
direction = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Starting the game...")  # Replace with game start logic
            if event.key == pygame.K_ESCAPE:
                running = False

    # Fill screen with background color
    screen.fill(PURPLE)

    # Animate circles
    for circle in circles:
        circle['pos'][1] += animation_speed * direction
        pygame.draw.circle(screen, circle['color'], circle['pos'], circle_radius)
    
    # Bounce animation
    if circles[0]['pos'][1] > SCREEN_HEIGHT//4 + 20 or circles[0]['pos'][1] < SCREEN_HEIGHT//4 - 20:
        direction *= -1

    # Draw text
    screen.blit(title_text, title_pos)
    screen.blit(subtitle_text, subtitle_pos)
    screen.blit(start_text, start_pos)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()