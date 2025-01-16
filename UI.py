import pygame
from game_of_life import GameOfLife
class GameUI:
    def __init__(self):
        self.cell_size = [32, 32]
        self.cell_game = GameOfLife()
        pygame.init()
        self.screen = pygame.display.set_mode(( self.cell_size[0] * 10,  self.cell_size[1] * 10))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('частички жизни')
        self.life_sprite = pygame.image.load('life.png')
        self.clear_sprite = pygame.image.load('clear.png')
    def draw_world(self):
        name_to_sprite = {" ": self.clear_sprite, "0": self.life_sprite}
        for y in range(10):
            for x in range(10):
                cell = self.cell_game.get_cell(x, y)
                self.screen.blit(name_to_sprite[cell], (x*self.cell_size[0], y*self.cell_size[1]))

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.cell_game.update_world()

    def run(self):
        while True:
            self.input()
            self.draw_world()
            pygame.display.update()

GameUI().run()