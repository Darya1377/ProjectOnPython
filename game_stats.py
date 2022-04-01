class GameStats():
    """Statistics for the game"""
    def __init__(self, ai_settings):
        """Initializes statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Starting game in inactive mode
        self.game_active = False
        #High score can't be deleted
        self.high_score = 0

    def reset_stats(self):
        """Initializes statistics which changes during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1