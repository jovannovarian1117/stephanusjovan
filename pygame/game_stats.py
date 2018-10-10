class GameStats():
    def __init__(self,theSettings):
        self.theSettings = theSettings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.rubix_left = self.theSettings.rubix_limit
        self.score = 0
        self.level = 1



