import pygame
from  pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx)

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Places ship in the center of the bottom side"""
        self.center = self.screen_rect.centerx

    def update(self):
        """Updates ship's position with flag"""
        #Updates center, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Updates rect because of self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)