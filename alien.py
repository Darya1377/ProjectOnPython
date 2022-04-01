import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for one alien"""
    def __init__(self, ai_settings, screen):
        """Initializes the alien and makes starting position for it"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #Downloading alien's image and making rect
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()
        #Every new alien appears in left upper corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Saving alien's position
        self.x = float(self.rect.x)

    def check_edges(self):
        """returns True if alien in the edge og screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельца вправо или влево"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x