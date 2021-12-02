#import pygame
class Settings():
    def __init__(self):

# Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        #self.bg = pygame.image.load("images/vibrance_14_11673_oboi_zvezdnoe_nebo_1366x768.jpg")
        self.bg_color = (0, 33, 55)
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self):
        self.ship_speed*= self.speedup_scale
        self.bullet_speed*= self.speedup_scale
        self.alien_speed*= self.speedup_scale