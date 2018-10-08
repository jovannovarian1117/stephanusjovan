import sys

import pygame
from picture import ImageIcon
import game_function as gf
from Settings import Settings
from pygame.sprite import Group

def run_game():
    pygame.init() #initialsize for game
    theSettings = Settings()
    screen = pygame.display.set_mode((theSettings.screen_width,theSettings.screen_height))
    pygame.display.set_caption("Rubix has own super power nibba") # game caption
    rubix = ImageIcon(screen,theSettings)
    bullets = Group()
    while True:
        gf.check_events(theSettings,screen,rubix,bullets)
        rubix.update()
        bullets.update()
        gf.update_screen(theSettings,screen,rubix,bullets)
        pygame.display.flip()


run_game()


