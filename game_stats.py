
class GameStats():

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        f=open ( "high_score.txt", "r") 
        self.high_score = int(f.read())
        self.level = 1
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0