import pygame
from game_object import Snake
from food import Food
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.window_size = 750
        self.screen = pygame.display.set_mode([self.window_size] * 2)
        self.clock = pygame.time.Clock()
        self.new_game()

    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.snake.update()
        pygame.display.flip()
        self.clock.tick(60)

    def draw(self):
        self.screen.fill('black')
        self.food.draw()
        self.snake.draw()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            self.snake.control(event)

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()