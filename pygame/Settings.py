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
        self.bullet_speed_factor = 5
        self.bullet_width = 100
        self.bullet_height = 20
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 3

        #how quickly the game speed up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialized_dynamic_settings()

    def initialized_dynamic_settings(self):
        self.rubix_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        self.rubix_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print (self.alien_points)




