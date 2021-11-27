import sys
import pygame
class AlienInvasion:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1366, 768))
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):

        while True:
# Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
# Отображение последнего прорисованного экрана.
            pygame.display.flip()
if __name__ == '__main__':
# Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
