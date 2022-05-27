class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализация настроек"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        #Aliens' settings

        self.fleet_drop_speed = 10
        self.alien_points = 50

        #Ship settings

        self.ship_limit = 3

        #Bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Speedup temp of game
        self.speedup_scale = 1.1
        #Inreasing aliens' cost temp
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that you can change during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.1
        self.fleet_direction = 1
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

    def increase_speed(self):
        """Increases speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale