class GameOfLife:
    def __init__(self):
        self.world = [
            [' ', 'jizn',' ',' ',' ', ' ', ' ',' ',' ','jizn',],
            ['jizn', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            ['jizn', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
        ]
    
    def get_cell(self, x, y):
        return self.world[y][x]

    def set_cell(self, x, y, value):
        self.world[y][x] = value

    def get_count_life_around(self, x, y):
        count = 0
        # будет возвращать количество живых клеток вокруг
        for y1 in range(-1, 2):
            for x1 in range(-1, 2):
                if x1 != 0 and y1 != 0:
                    x += x1 
                    y += y1
                    x = x % len(self.world[0])
                    y = y % len(self.world)
                    if self.get_cell(x, y) == 'jizn':
                        count += 1
        return count                                
    def update_cell(self, x, y):
        cell = self.get_cell(x, y)
        if cell == ' ':
            if self.get_count_life_around(x, y) == 3:
                value = 'jizn'
                self.set_cell(x, y, value)
        else:
            if not (2 <= self.get_count_life_around(x, y) <= 3):
                value = ' '
                self.set_cell(x, y, value)
    def update_world(self):
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                self.update_cell(x, y)
