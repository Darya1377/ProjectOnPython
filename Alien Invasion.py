import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #Инициализирует игру и содает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings. screen_height))
    pygame. display.set_caption("Alien Invasion")

    #Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")

    #Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)

    #Создание корабля, группы пуль и пришельцев.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, ship, aliens,
                          bullets, play_button)
         
run_game()
