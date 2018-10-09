import pygame

class ImageIcon():
    def __init__(self,screen,theSettings):
        self.screen = screen
        self.theSettings = theSettings
        self.image = pygame.image.load('rubixs.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() # rect stand stands for rectangle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.theSettings.rubix_speed_factor
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= self.theSettings.rubix_speed_factor
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1
        self.rect.centerx = self.center

    def center_rubix(self):
        self.center = self.screen_rect.centerx


    def blitme(self):
        self.screen.blit(self.image,self.rect)