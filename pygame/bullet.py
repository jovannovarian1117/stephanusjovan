import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,theSettings,screen,rubix):
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0, theSettings.bullet_width,theSettings.bullet_height)
        self.rect.centerx = rubix.rect.centerx
        self.rect.top = rubix.rect.top

        self.y = float(self.rect.y)

        self.color = theSettings.bullet_color
        self.speed_factor = theSettings.bullet_speed_factor

    def bulletUpdate(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


