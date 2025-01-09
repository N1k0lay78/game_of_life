class GameOfLife:
    def __init__(self):
        self.world = [
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
        ]
    
    def get_cell(self, x, y):
        return self.world[y][x]

    def set_cell(self, x, y, value):
        self.world[y][x] = value

    def get_count_life_around(self, x, y):
        # будет возвращать количество живых клеток вокруг
        pass
    
    def update_cell(self, x, y):
        cell = self.get_cell(x, y)
        if cell == ' ':
            if self.get_count_life_around(x, y) == 3:
                value = 'jizn'
                self.set_cell(x, y, value)

    def update_world(self):
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                self.update_cell(x, y)
