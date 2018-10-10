import pygame.font
from pygame.sprite import Group
from picture import ImageIcon

class Scoreboard():
    def __init__(self,theSettings,screen,stats):
        #class to report score
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.theSettings = theSettings
        self.stats = stats
        self.prep_high_score()

        # font settings
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #prepare score image
        self.prep_score()
        self.prep_rubixs()


    def prep_score(self):
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.theSettings.bg_color)
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.rubixs.draw(self.screen)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.theSettings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level.image = self.font.render(str(self.stats.level), True, self.text_color, self.theSettings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect_right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_rubixs(self):
        self.rubixs = Group()
        for rubix_number in range(self.stats.shipx_left):
            rubix = ImageIcon(self.theSettings,self.screen)
            rubix.rect.x = 10 + rubix_number * rubix.rect.width
            rubix.rect.y = 10
            self.rubixs.add(rubix)
