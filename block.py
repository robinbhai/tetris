from colors import Colors
import pygame as p
from position import Position_of_blocks


class Block:
    def __init__(self, id) :
        self.id = id
        self.cells = {} 
        self.cell_size = 30
        self.move_row = 0
        self.move_col = 0
        self.rotation = 0
        self.colors = Colors.cell_colors()

    def move(self, row, col ):
        self.move_row += row
        self.move_col += col

    def new_cell_pos(self):
        block_tiles = self.cells[self.rotation]
        moved_tiles = []
        for position in block_tiles:
            position = Position_of_blocks(position.row + self.move_row, position.col + self.move_col)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate_block(self):
        self.rotation +=1
        if self.rotation == len(self.cells):
            self.rotation = 0

    def undo_rotate(self):
        self.rotation -=1
        if self.rotation == 0:
            self.rotation = len(self.cells)-1
    

 

    def draw_blocks(self, game_screen, offset_x, offset_y):
        block_tiles = self.new_cell_pos()
        for tile in block_tiles:
            tile_rect = p.Rect(offset_x+tile.col*self.cell_size, offset_y+tile.row*self.cell_size, self.cell_size -1 , self.cell_size -1)
            p.draw.rect(game_screen, self.colors[self.id], tile_rect)