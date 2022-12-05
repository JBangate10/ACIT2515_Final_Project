import pygame

class Food:
    def __init__(self, game):
        self.game = game
        self.rect = pygame.rect.Rect([0, 0, 48, 48])
        self.rect.center = self.game.snake.get_random_position()
    
    def draw(self):
        pygame.draw.rect(self.game.screen, 'blue', self.rect)
