class GameOfLife:
    def __init__(self):
        self.world = [
            [' ', '0',' ',' ','0', ' ', ' ',' ',' ','0',],
            ['0', ' ',' ',' ','0', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ','0', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            ['0', '0',' ',' ',' ', ' ', '0',' ',' ',' ',],
            [' ', '0',' ',' ',' ', ' ', ' ','0',' ',' ',],
            [' ', ' ',' ',' ',' ', '0', '0','0',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            [' ', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
            ['0', ' ',' ',' ',' ', ' ', ' ',' ',' ',' ',],
        ]
        self.new_world = []

    def print(self):
        print()
        for line in self.world:
            print(line)

    def create_new_world(self):
        self.new_world = []
        for y in range(len(self.world)):
            self.new_world.append([])
            for _ in range(len(self.world[y])):
                self.new_world[-1].append(' ')
    
    def swap(self):
        self.world = self.new_world

    def get_cell(self, x, y):
        return self.world[y][x]

    def set_cell(self, x, y, value):
        self.new_world[y][x] = value

    def get_count_life_around(self, x, y):
        count = 0
        # будет возвращать количество живых клеток вокруг
        for y1 in range(-1, 2):
            for x1 in range(-1, 2):
                if not (x1 == 0 and y1 == 0):
                    x2 = x + x1 
                    y2 = y + y1
                    x2 = x2 % len(self.world[0])
                    y2 = y2 % len(self.world)
                    if self.get_cell(x2, y2) == '0':
                        count += 1
        return count                                

    def update_cell(self, x, y):
        cell = self.get_cell(x, y)
        if cell == ' ':
            if self.get_count_life_around(x, y) == 3:
                value = '0'
                self.set_cell(x, y, value)
        else:
            if 2 <= self.get_count_life_around(x, y) <= 3:
                value = '0'
                self.set_cell(x, y, value)

    def update_world(self):
        self.create_new_world()
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                self.update_cell(x, y)
        self.swap()


game = GameOfLife()
game.print()
for _ in range(20):
    game.update_world()
    game.print()
