class Block:
    def __init__(self):
        self.y = 0
        self.x = 0 
        self.orientation = "default" 

    def rotate(self):
        if self.orientation == "default":
            self.orientation = "right"
        elif self.orientation == "right":
            self.orientation = "flipped"
        elif self.orientation == "flipped":
            self.orientation = "left"
        elif self.orientation == "left":
            self.orientation == "default"

    def move(self, direction):
        if direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 2 
        elif direction == "right":
            self.x += 2 

class SBlock(Block):
    def __init__(self):
        super().__init__()

        self.type = "S"
    def __str__(self):
        return f"x: {self.x} | y: {self.y} | {self.orientation} | {self.type}"


class IBlock(Block):
    def __init__(self):
        super().__init__()

        self.type = "I"

    def __str__(self):
        return f"x: {self.x} | y: {self.y} | {self.orientation} | {self.type}"


class JBlock(Block):
    def __init__(self):
        super().__init__()

        self.type = "J"

    def __str__(self):
        return f"x: {self.x} | y: {self.y} | {self.orientation} | {self.type}"


class LBlock(Block):
    def __init__(self):
        super().__init__()

        self.type = "L"

    def __str__(self):
        return f"x: {self.x} | y: {self.y} | {self.orientation} | {self.type}"


class OBlock(Block):
    def __init__(self):
        super().__init__()

        self.type = "O"

    def __str__(self):
        return f"x: {self.x} | y: {self.y} | {self.orientation} | {self.type}"


class TBlock(Block):
    def __init__(self):
        super().__init__()

        self.type = "T"

    def __str__(self):
        return f"x: {self.x} | y: {self.y} | {self.orientation} | {self.type}"


class ZBlock(Block):
    def __init__(self):
        super().__init__()

        self.type = "Z"

    def __str__(self):
        return f"x: {self.x} | y: {self.y} | {self.orientation} | {self.type}"
