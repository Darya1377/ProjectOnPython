import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями"""
    def __init__(self, ai_settings, screen, ship):
        """Creates bullet's object in ship's position"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Creating bullet in (0,0) position and making right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Bullet's position in float format
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещает пулю вверх по экрану"""
        #Updating bullet's position in float format
        self.y -= self.speed_factor
        #Updating rectangle's position
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)