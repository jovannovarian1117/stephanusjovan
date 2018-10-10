import sys

import pygame
from picture import ImageIcon
import game_function as gf
from Settings import Settings
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init() #initialsize for game
    theSettings = Settings()
    screen = pygame.display.set_mode((theSettings.screen_width, theSettings.screen_height))
    pygame.display.set_caption("Rubix has own super power nibba")# game caption
    play_button = Button(theSettings,screen,"Play")
    stats = GameStats(theSettings)
    sb = Scoreboard(theSettings,screen,stats)
    rubix = ImageIcon(screen,theSettings)
    alien = Alien(theSettings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(theSettings, screen, rubix, aliens)


    while True:
        gf.check_events(theSettings, screen,stats,sb,play_button, rubix,aliens, bullets)

        if stats.game_active:
            rubix.update()
            bullets.update()
            gf.update_bullets(theSettings, screen, stats,sb, rubix, aliens, bullets)
            gf.update_aliens(theSettings,stats,screen,rubix,aliens,bullets)
            gf.update_screen(theSettings, screen, stats,sb, rubix, aliens, bullets,)
run_game()


