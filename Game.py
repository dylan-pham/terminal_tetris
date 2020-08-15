import random
from Block import IBlock, JBlock, LBlock, OBlock, ZBlock, SBlock, TBlock

class Game:
    def __init__(self):
        self.gameover = True
        self.grid = [[0 for i in range(10)] for i in range(21)]
        self.score = 0
        self.level = 1
        self.speed = "slow"
        self.current_block = None
        self.next_block = None
        self.queue = []
        self.bank = None
        # self.brick_types = ['i', 'j', 'l', 'o', 's', 't', 'z']

    def generate_rand_brick(self):
        brick_types = {
            0: IBlock(), 1: JBlock(), 2: LBlock(), 3: OBlock(), 
            4: SBlock(), 5: TBlock(), 6: ZBlock()
        }

        num = random.randint(0, 6)

        return brick_types[num]

    def start(self):
        self.gameover = False
        self.current_block = Game.generate_rand_brick(self)
        self.current_block.x = 65
        self.current_block.y = 10
        self.grid[0][3:7] = [1 for i in range(4)]
        self.next_block = Game.generate_rand_brick(self)
        
        for i in range(5):
            self.queue.append(Game.generate_rand_brick(self))

    def is_gameover(self):
        if 1 in self.grid[0]: 
            return True

        return False

    def is_tetris(self):
        if (
            set(self.grid[20]) == 1
            and set(self.grid[19]) == 1 
            and set(self.grid(18)) == 1
            and set(self.grid[17]) == 1 
        ):
            return True

        return False

    def clear_lines(self, _range):
        return 0

    def place_brick(self, brick_type, position):
        return 0
