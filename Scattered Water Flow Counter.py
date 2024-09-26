import tkinter as tk

class Game:
    def __init__(self, size, obstacle, start):
        self.size = size
        self.obstacle = obstacle
        self.start = start

    def generate_map(self):
        temp_map = [[-1 for _ in range (self.size + 2)] for _ in range (self.size + 2)]
        for row in range (self.size):
            temp_map[row + 1][1:self.size + 1] = [0 for _ in range (self.size)]
        self.map = temp_map

    def generate_obstacle(self):
        for obstacle in (self.obstacle):
            if (obstacle[0] > obstacle[2]):
                obstacle[0], obstacle[2] = obstacle[2], obstacle[0]
            if (obstacle[1] > obstacle[3]):
                obstacle[1], obstacle[3] = obstacle[3], obstacle[1]
            for i in range (obstacle[1], obstacle[3] + 1):
                self.map[i][obstacle[0]:obstacle[2] + 1] = [1 for _ in range (obstacle[0], obstacle[2] + 1)]

    def generate_result(self):
        root = tk.Tk()
        root.title('Reflection Result')
        for row in range (len(self.map)):
            for col in range (len(self.map)):
                color = 'white'
                if (self.map[row][col] == 0):
                    color = 'gray'
                elif (self.map[row][col] == 1):
                    color = 'black'
                elif (self.map[row][col] == 2):
                    color = 'light blue'
                if (row == 0 and col == 0):
                    cell = tk.Label(root, text = f'Reflections : {self.__reflection}', bg = color, width = 10, height = 5)
                elif (row == 0 and col != 0 and col != len(self.map) - 1):
                    cell = tk.Label(root, text = f'X-{col}', bg = color, width = 10, height = 5)
                elif (col == 0 and row != 0 and row != len(self.map) - 1):
                    cell = tk.Label(root, text = f'Y-{row}', bg = color, width = 10, height = 5)
                else:
                    cell = tk.Label(root, bg = color, width = 10, height = 5)
                cell.grid(row = row, column = col)
        root.mainloop()

    def start_game(self):
        self.__reflection = 0
        self.flow(0, self.start)

    def flow(self, row, col):
        self.map[row][col] = 2
        if (row != self.size + 1):
            if (self.map[row + 1][col] == 1):
                if (self.map[row][col - 1] != 1 or self.map[row][col + 1] != 1):
                    self.__reflection += 1
                if (self.map[row][col - 1] != 1 and self.map[row][col - 1] != 2):
                    self.find_way(row, col - 1, 0)
                if (self.map[row][col + 1] != 1 and self.map[row][col + 1] != 2):
                    self.find_way(row, col + 1, 1)
            else:
                self.flow(row + 1, col)

    def find_way(self, row, col, way):
        if (self.map[row][col] != 1):
            self.map[row][col] = 2
            if (self.map[row + 1][col] != 1):
                self.flow(row + 1, col)
            elif (way == 0 and self.map[row][col - 1] != 2):
                self.find_way(row, col - 1, 0)
            elif (way == 1 and self.map[row][col + 1] != 2):
                self.find_way(row, col + 1, 1)

try:
    size = int(input('Map size\t: '))
    total_obstacles = int(input('Total obstables\t: '))
    obstacle = []
    for i in range (total_obstacles):
        temp_obstacle = list(map(int, input(f'Obstacle {i + 1} (x1 y1 x2 y2)\t: ').split()))
        if (len(temp_obstacle) != 4):
            raise
        elif (all(num <= size and num > 0 for num in (temp_obstacle))):
            obstacle.append(temp_obstacle)
        else:
            raise
    start = int(input('Water starts from\t\t: '))
    if (start > size or start < 1):
        raise
except:
    print('Input is invalid')
else:
    game = Game(size, obstacle, start)
    game.generate_map()
    game.generate_obstacle()
    game.start_game()
    game.generate_result()
