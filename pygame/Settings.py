import sys
import pygame

class Settings():
    def __init__(self):
        #screen settings general
        self.screen_width = 1000 # width settings
        self.screen_height = 500
        self.bg_color = (69,139,0)
        self.rubix_speed_factor = 1.5

        #this is for bullet below
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (153,50,204)

