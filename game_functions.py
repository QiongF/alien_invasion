import sys

import pygame

def check_events():
    """Responde to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """update screen image and switch to new screen"""
    # In every loop refill the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Visalize the latest screen
    pygame.display.flip()

