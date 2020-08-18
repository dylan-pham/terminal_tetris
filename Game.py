import random
import Graphics

class Block:
    def __init__(self, identifier, coordinates, pivot_point): # coordinates = [[y,x]...]
        self.identifier = identifier
        self.coordinates = coordinates
        self.pivot_point = pivot_point

class Game:
    def __init__(self):
        self.gameover = True
        self.grid = [[0 for i in range(10)] for i in range(20)]
        self.score = 0
        self.level = 1
        self.speed = "slow"
        self.current_block = None
        self.next_block = None
        self.queue = []
        self.bank = None

    def generate_rand_block(self):
        blocks = {
            1: Block(1, [[0,3], [0,4], [0,5], [0,6]], [0,5]),
            2: Block(2, [[0,4], [0,5], [1,4], [1,5]], [0,4]),
            3: Block(3, [[0,3], [0,4], [0,5], [1,4]], [0,4]), 
            4: Block(4, [[0,3], [0,4], [0,5], [1,3]], [0,4]),
            5: Block(5, [[0,3], [0,4], [0,5], [1,5]], [0,4]),
            6: Block(6, [[0,4], [0,5], [1,3], [1,4]], [1,4]),
            7: Block(7, [[0,3], [0,4], [1,4], [1,5]], [1,4])
        }

        num = random.randint(1, 7)

        return blocks[num]

    def start(self):
        self.gameover = False
        self.current_block = Game.generate_rand_block(self)
        self.next_block = Game.generate_rand_block(self)

        for i in range(5):
            self.queue.append(Game.generate_rand_block(self))

        for coordinate in self.current_block.coordinates:
            self.grid[coordinate[0]][coordinate[1]] = self.current_block.identifier

    def is_gameover(self):
        return False

    def regen(self):
        self.current_block = self.next_block 
        self.next_block = self.queue.pop()
        self.queue.append(Game.generate_rand_block(self))

    def move_block(self, stdscr, block, direction):
        if direction == "down" and (max([coordinate[0] for coordinate in block.coordinates]) < 19):
            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y][x] = 0
                Graphics.fill_square(stdscr, y, x, 0) 
            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y+1][x] = block.identifier
                Graphics.fill_square(stdscr, y+1, x, block.identifier) 

            for i in range(len(block.coordinates)):
                block.coordinates[i] = [block.coordinates[i][0]+1, block.coordinates[i][1]]
            block.pivot_point = [block.pivot_point[0]+1, block.pivot_point[1]]
        elif direction == "down":
            Game.regen(self)
        elif direction == "right":
            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y][x] = 0
                Graphics.fill_square(stdscr, y, x, 0) 

            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y][x+1] = block.identifier
                Graphics.fill_square(stdscr, y, x+1, block.identifier) 

            for i in range(len(block.coordinates)):
                block.coordinates[i] = [block.coordinates[i][0], block.coordinates[i][1]+1]
            block.pivot_point = [block.pivot_point[0], block.pivot_point[1] + 1]
        elif direction == "left":
            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y][x] = 0
                Graphics.fill_square(stdscr, y, x, 0)

            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y][x-1] = block.identifier
                Graphics.fill_square(stdscr, y, x-1, block.identifier)

            for i in range(len(block.coordinates)):
                block.coordinates[i] = [block.coordinates[i][0], block.coordinates[i][1]-1]
            block.pivot_point = [block.pivot_point[0], block.pivot_point[1]-1]

        elif direction == "bottom":
            max_drops = []

            for y,x in block.coordinates:
                for temp in range(y, 19):
                    if self.grid[temp][x] != 0 and [temp,x] not in block.coordinates:
                        max_drops.append(temp-y-1)
            
            max_drops.append(19-y)
            y_drop = min(max_drops)

            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y][x] = 0
                Graphics.fill_square(stdscr, y, x, 0)

            for coordinate in block.coordinates:
                y = coordinate[0]
                x = coordinate[1]

                self.grid[y+y_drop][x] = block.identifier
                Graphics.fill_square(stdscr, y+y_drop, x, block.identifier)

            for i in range(len(block.coordinates)):
                block.coordinates[i] = [block.coordinates[i][0] + y_drop, block.coordinates[i][1]]

            Game.regen(self)
           

    def rotate_block(self, stdscr, block):
        pivot_y = block.pivot_point[0]
        pivot_x = block.pivot_point[1]

        for coordinate in block.coordinates:
            y = coordinate[0]
            x = coordinate[1]

            self.grid[y][x] = 0
            Graphics.fill_square(stdscr, y, x, 0)
        
        u = 0
        for coordinate in block.coordinates:
            y = coordinate[0]
            x = coordinate[1]

            relative_coordinates = [y-pivot_y, x-pivot_x]
            temp = [relative_coordinates[1], -1*relative_coordinates[0]]
            new = [pivot_y+temp[0], pivot_x+temp[1]]

            self.grid[new[0]][new[1]] = block.identifier
            Graphics.fill_square(stdscr, new[0], new[1], block.identifier)

            block.coordinates[u] = [new[0], new[1]]
            u += 1
