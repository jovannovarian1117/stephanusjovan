import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,theSettings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.theSettings = theSettings

        #load the alien image with rect attribute

        self.image = pygame.image.load('osamass.png')
        self.rect = self.image.get_rect()

        #startthe alien position based on the coding codes
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #the exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # alien movement
        self.x += (self.theSettings.alien_speed_factor * self.theSettings.fleet_direction)
        self.rect.x = self.x


