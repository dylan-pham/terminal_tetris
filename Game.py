import random

class Game:
    def __init__(self, game_over, grid, score):
        self.game_over = False
        self.grid = [[0 for i in range(10)] * 20]
        self.score = 0

    def check_game_over(self):
        return 0

    def clear_grid(self):
        self.grid = [[0 for i in range(10)] * 20]

    def check_tetris(self):
        return 0

    def clear_lines(self, _range):
        return 0

    def place_brick(self, brick_type, position):
        return 0


class Queue:
    generator = Brick_Generator()

    def __init__(self, bricks):
        self.bricks = [generator.generate() for i in range(3)]

    def pop(self):
        bricks.append(generator.generate())    

        return bricks.pop()

    def __str__(self):
        temp = ""

        for brick in self.bricks:
            temp += brick.__str__() + "\n"

        return temp


class Brick:
    def __init__(self, brick_type, position, orientation):
        self.brick_type = brick_type
        self.position = (0, 4)
        self.orientation = orientation

    def rotate(self):
        return 0

    def move(self, direction):
        if direction == "right" and self.position[1] < 20:
            self.position[1] += 1
        elif direction == "left" and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == "down":
            return 0

    def __str__(self):
        return self.brick_type.__str__()


class Brick_Generator:
    def __init__(self, brick_types):
        self.brick_types = ['i', 'j', 'l', 'o', 's', 't', 'z']

    def generate(self):
        return self.brick_types[random.randint(0, 7)]
