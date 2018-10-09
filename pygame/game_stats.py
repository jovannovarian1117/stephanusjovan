class GameStats():
    def __init__(self,theSettings):
        self.theSettings = theSettings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.rubix_left = self.theSettings.rubix_limit

