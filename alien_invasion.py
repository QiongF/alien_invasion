import pygame  # pygame is a cross-platform set of Python modules designed for writing video games.

from settings import Settings
from ship import Ship
import game_functions as gf

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
        gf.check_events()      
        gf.update_screen(ai_settings, screen, ship) 

run_game()

