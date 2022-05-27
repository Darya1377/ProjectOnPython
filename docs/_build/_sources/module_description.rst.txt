==========================================
Description of modules
==========================================

* alien_invasion

  Executable script. Initializes a game and creates an object of a screen. Starts the main game cycle.
  Tracks the events of a keyboard and a mouse. Displays the last drawn screen.::

    def run_game()

* alien.py

  Class for one alien.
  This class initializes the alien and makes starting position for it.
  It also checks the edges, if an alien reached the end of the screen.
  Class also displays the alien in the current position, moves the alien to the right or left.::

    from pygame.sprite import Sprite

    class Alien(Sprite):
    """Class for one alien"""

        def __init__(self, ai_settings, screen):

        def check_edges(self):
        """returns True if alien in the edge of screen"""

        def blitme(self):
        """displays the alien in the current position"""

* bullet.py

  Class for managing bullets. Creates bullet's object in ship's position.
  Moves the bullet up the screen. Outputs a bullet to the screen.::

    from pygame.sprite import Sprite

    class Bullet(Sprite):
    """Class for managing bullets"""

        def __init__(self, ai_settings, screen, ship):
        """Creates bullet's object in ship's position"""

        def update(self):
        """Moves the bullet up the screen"""

        def draw_bullet(self):
        """Outputs a bullet to the screen"""

* button.py

  Class that initializes button's attributes. Creates text on it, makes it functional.::

    class Button():

        def __init__(self, ai_settings, screen, msg):
        """Initializes button's attributes"""

        def prep_msg(self, msg):
        """Makes msg rectangular and aligns text by the center"""

        def draw_button(self):
        """Draws button"""

* game_functions.py

  The ensemble of functions. Checks if a new score has appeared. Checks hitting of aliens and bottom side of screen.
  Processes hitting of ship and alien. Reacts on getting the edge of a screen for alien.
  Drops and changes direction of the fleet. Updates all aliens' positions in the fleet.
  Initializes number of rows on the screen. Counts number of aliens in row.
  Creates an alien and place it in row. Creates aliens' fleet. Updates bullets' positions and deletes old bullets.
  Processes bullets' collisions with aliens. Reacts on pushing buttons.
  Fires a bullet if the maximum has not yet been reached. Reacts on not pushing buttons.
  Handles keystrokes and mouse events. Activates new game by button Play pushing.
  Updates the images on the screen and the screen itself.::

    from src.bullet import Bullet
    from src.alien import Alien

    def check_high_score(stats, sb):
    """Checks if new highscore appeared"""

    def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Checks hitting of aliens and bottom side of screen"""

    def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Processing hitting of ship and alien"""

    def check_fleet_edges(ai_settings, aliens):
    """Reacts on getting the edge for alien"""

    def change_fleet_direction(ai_settings, aliens):
    """Drops and changes direction of the fleet"""

    def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates all aliens' positions in the fleet"""

    def get_number_rows(ai_settings, ship_height, alien_height):
    """Initializes number of rows on the screen"""

    def get_number_aliens_x(ai_settings, alien_width):
    """Counting number of aliens in row"""

    def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creating an alien and place it in row"""

    def create_fleet(ai_settings, screen, ship, aliens):
    """Creating aliens' fleet"""

    def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Updates bullets' positions and deletes old bullets"""

    def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Processing of bullets' collisions with aliens"""

    def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reacts on pushing buttons"""

    def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if the maximum has not yet been reached"""

    def check_keyup_events(event, ship):
    """Reacts on not pushing buttons"""

    def check_events(ai_settings, screen, stats, sb,
                 play_button, ship, aliens, bullets):
    """Handles keystrokes and mouse events"""

    def check_play_button(ai_settings, screen, stats, sb, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    """Activates new game by button Play pushing"""

    def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Updates the images on the screen and the screen itself"""

* game_stats.py

  Class to hold statistics for the game. Initializes statistics which changes during the game.::

    class GameStats():
    """Statistics for the game"""

        def __init__(self, ai_settings):
        """Initializes statistics"""

        def reset_stats(self):
        """Initializes statistics which changes during the game"""

* scoreboard.py

  Class for print gaming info. Initializes attributes of score counting.
  Makes a score, high score, level graphical. Prints score, highscore and ships left on the screen.
  Prints how many ships/attempts left.::

    from src.ship import Ship

    class Scoreboard():
    """Class for print gaming info"""

        def __init__(self, ai_settings, screen, stats):
        """Initializes attributes of score counting"""

        def prep_score(self):
        """Makes score graphical"""

        def prep_high_score(self):
        """Makes high score graphical"""

        def show_score(self):
        """Prints score, highscore and ships left on the screen"""

        def prep_level(self):
        """Makes level graphical"""

        def prep_ships(self):
        """Prints how many ships/attempts left"""



* setings.py

  Class for storing all game settings. Initializes settings that you can change during the game.
  Increases speed settings.::

    class Settings():
    """Class for storing all game settings"""

        def __init__(self):
        """Initializing settings"""

        def initialize_dynamic_settings(self):
        """Initializes settings that you can change during the game"""

        def increase_speed(self):
        """Increases speed settings"""

* ship.py

  Initializes the ship and sets its initial position. Places a ship. Updates ship's position with flag.
  Draws a ship in a current position.::

    class Ship(Sprite):

        def __init__(self, ai_settings, screen):
        """Initializes the ship and sets its initial position"""

        def center_ship(self):
        """Places ship in the center of the bottom side"""

        def update(self):
        """Updates ship's position with flag"""

        def blitme(self):
        """Draws a ship in a current position"""

