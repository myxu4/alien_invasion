import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
# Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/alien_ship-removebg-preview.png')
        self.rect = self.image.get_rect()
# Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
# Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)