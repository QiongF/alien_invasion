import pygame

class Ship():

    def __init__(self, screen):
        """initiate ship and set its initial location"""
        self.screen = screen
        
        # Load ship image and acquaire bounding rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Place the new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """draw spaceship at specified location"""
        self.screen.blit(self.image, self.rect)
    
    
