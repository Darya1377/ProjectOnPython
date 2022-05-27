import sys
from time import sleep
import pygame
from src.bullet import Bullet
from src.alien import Alien

def check_high_score(stats, sb):
    """Checks if new highscore appeared"""
    if stats.score > stats.high_score:
        stats.highscore = stats.score
        sb.prep_high_score()

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Checks hitting of aliens and bottom side of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Processing hitting of ship and alien"""
    if stats.ships_left > 0:
        #Decreasing ships_left
        stats.ships_left -= 1
        #Updating gaming info
        sb.prep_ships()
        #Cleaning of aliens' and bullets' lists
        aliens.empty()
        bullets.empty()
        #Creating new fleet and placing ship in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_fleet_edges(ai_settings, aliens):
    """Reacts on getting the edge for alien"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drops and changes direction of the fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates all aliens' positions in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #Checking alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    #Checking aliens on the edge of screen's bottom side
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Initializes number of rows on the screen"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """Counting number of aliens in row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creating an alien and place it in row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Creating aliens' fleet"""
    #Creating alien and counting number of aliens in row
    #Space between aliens-neighbours is one alien's width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Creating aliens' fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates bullets' positions and deletes old bullets"""
    #Updates bullets' positions
    bullets.update()
    # Deleting bullets outside screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Processing of bullets' collisions with aliens"""
    #Deleting bullets and aliens taking part in colliisions
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
            check_high_score(stats, sb)
    if len(aliens) == 0:
        #If fleet lose, next level starts
        bullets.empty()
        ai_settings.increase_speed()
        #Level up
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reacts on pushing buttons"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Creating new bullet and including it into group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум еще не достигнут"""
    #Making new group and including it into bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Reacts on not pushing buttons"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb,
                 play_button, ship, aliens, bullets):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    """Activates new game by button Play pushing"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Mouse cursor hides
        pygame.mouse.set_visible(False)
        #Reset game settings
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True
        #Deleting score and level images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #Clearing aliens' and bullets' lists
        aliens.empty()
        bullets.empty()
        #Creating new fleet and placing ship by the center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Обновляет изображения на экране и сам экран"""
    # При каждом проходе цикла обновляется экран
    screen.fill(ai_settings.bg_color)
    #Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #Print score
    sb.show_score()
    #Play button active if only game is inactive
    if not stats.game_active:
        play_button.draw_button()
    # Отображение последнего прорисованного экрана
    pygame.display.flip()