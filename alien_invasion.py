import sys

import pygame  # pygame is a cross-platform set of Python modules designed for writing video games.

from settings import Settings

def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # create a spaceship
    ship = Ship(screen)

    # Start the main loop of the game.
    while True:
        
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # In every loop refill the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Visalize the latest screen
        pygame.display.flip()

run_game()

