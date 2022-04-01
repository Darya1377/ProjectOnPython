import sys
import pygame
from setings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #Инициализирует pygame, setings and screen's object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Play button creating
    play_button = Button(ai_settings, screen, "Play")
    #Ship creating
    ship = Ship(ai_settings, screen)
    #Creating group for bullets
    bullets = Group()
    #Creating aliens' group
    aliens = Group()
    #Creating rows of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #Цвет фона
    bg_color = (230, 230, 230)

    #Creating an alien
    alien = Alien(ai_settings, screen)

    #Creating an example for saving game statistics and score
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()