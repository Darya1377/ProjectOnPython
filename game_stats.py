class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_settings):
        """Ининциализирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Игра запускается в неактивном состоянии.
        self.game_active = False
        #Игра Alien Invasion запускается в активном состоянии.
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit
