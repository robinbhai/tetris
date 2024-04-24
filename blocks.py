from block import Block
from position import Position_of_blocks

class Block_L(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position_of_blocks(0,2), Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(1,2)],
            1: [Position_of_blocks(0,1), Position_of_blocks(1,1), Position_of_blocks(2,1), Position_of_blocks(2,2)],
            2: [Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(2,0)],
            3: [Position_of_blocks(0,0), Position_of_blocks(0,1), Position_of_blocks(1,1), Position_of_blocks(2,1)],
        }
        self.move(0,3)

class Block_S(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position_of_blocks(0,1), Position_of_blocks(0,2), Position_of_blocks(1,0), Position_of_blocks(1,1)],
            1: [Position_of_blocks(0,1), Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(2,2)],
            2: [Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(2,0), Position_of_blocks(2,1)],
            3: [Position_of_blocks(0,0), Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(2,1)],
        }
        self.move(0,3)


class Block_J(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [Position_of_blocks(0,0), Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(1,2)],
            1: [Position_of_blocks(0,1), Position_of_blocks(0,2), Position_of_blocks(1,1), Position_of_blocks(2,1)],
            2: [Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(2,2)],
            3: [Position_of_blocks(0,1), Position_of_blocks(1,1), Position_of_blocks(2,0), Position_of_blocks(2,1)],
        }
        self.move(0,3)

class Block_I(Block):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(1,3)],
            1: [Position_of_blocks(0,2), Position_of_blocks(1,2), Position_of_blocks(2,2), Position_of_blocks(3,2)],
            2: [Position_of_blocks(2,0), Position_of_blocks(2,1), Position_of_blocks(2,2), Position_of_blocks(2,3)],
            3: [Position_of_blocks(0,1), Position_of_blocks(1,1), Position_of_blocks(2,1), Position_of_blocks(3,1)],
        }
        self.move(-1,3)

class Block_T(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position_of_blocks(0,1), Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(1,2)],
            1: [Position_of_blocks(0,1), Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(2,1)],
            2: [Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(2,1)],
            3: [Position_of_blocks(0,1), Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(2,1)],
        }
        self.move(0,3)

class Block_Z(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position_of_blocks(0,0), Position_of_blocks(0,1), Position_of_blocks(1,1), Position_of_blocks(1,2)],
            1: [Position_of_blocks(0,2), Position_of_blocks(1,1), Position_of_blocks(1,2), Position_of_blocks(2,1)],
            2: [Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(2,1), Position_of_blocks(2,2)],
            3: [Position_of_blocks(0,1), Position_of_blocks(1,0), Position_of_blocks(1,1), Position_of_blocks(2,0)],
           }
        self.move(0,3)

class Block_O(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position_of_blocks(0,0), Position_of_blocks(0,1), Position_of_blocks(1,0), Position_of_blocks(1,1)],
             }   
        self.move(0,4)
