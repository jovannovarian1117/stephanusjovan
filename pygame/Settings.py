import sys
import pygame

class Settings():
    def __init__(self):
        #screen settings general
        self.screen_width = 1350 # width settings
        self.screen_height = 700
        self.bg_color = (69,139,0)
        self.rubix_speed_factor = 5
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 2
        self.fleet_direction = 1
        self.rubix_limit = 3
        #+1 is right -1 is left


        #this is for bullet below
        # bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 3




