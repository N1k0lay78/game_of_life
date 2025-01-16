import pygame
from game_of_life import GameOfLife


class GameUI:
    def __init__(self):
        self.cell_size = (32, 32)

        self.game = GameOfLife()

        pygame.init()
        self.screen = pygame.display.set_mode((self.cell_size[0] * 10, self.cell_size[1] * 10))
        pygame.display.set_caption('игра в жизнь')
        
        self.clock = pygame.time.Clock()
        self.life_sprite = pygame.image.load('life.png')
        self.clear_sprite = pygame.image.load('clear.png')

    def draw_world(self):
        name_to_sprite = {" ": self.clear_sprite, "0": self.life_sprite}
        for y in range(10):
            for x in range(10):
                cell = self.game.get_cell(x, y)
                self.screen.blit(name_to_sprite[cell], (x*self.cell_size[0], y*self.cell_size[1]))
     
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.game.update_world()

    def run(self):
        while True:
            self.input()
            self.draw_world()
            pygame.display.update()
            self.clock.tick(30)                    


GameUI().run()
