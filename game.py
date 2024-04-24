import pygame as p
from grid import Grid
import random
from blocks import *
from block import *
from position import Position_of_blocks


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks =  [ Block_I(), Block_J(), Block_L(), Block_O(), Block_S(), Block_T(), Block_Z()]
        self.current_block = self.random_block()
        self.next_block = self.random_block()
        self.game_over = False
        self.score = 0
        self.line = 0
        self.clearing_sound = p.mixer.Sound("Sounds/clear.ogg")
        self.gameover_sound = p.mixer.Sound("Sounds/gameover.ogg")
        p.mixer.music.load("Sounds/music.mp3")  
        p.mixer.music.play(-1)

    

    def score_system(self , lines_cleared):
        if lines_cleared == 1:
            self.score +=100
        elif lines_cleared == 2:
            self.score +=300
        elif lines_cleared == 3:
            self.score+=500 
        elif lines_cleared == 4:
            self.score+=1000 

    def lines(self , lines_cleared):
        if lines_cleared ==1:
            self.line +=1
        elif lines_cleared == 2:
            self.line +=2 
        elif  lines_cleared == 3:
            self.line +=3
        elif  lines_cleared == 4:
            self.line +=4


    

 

    #random blocks
    def random_block(self):
        if len(self.blocks) == 0:
             self.blocks =  [ Block_I(), Block_J(), Block_L(), Block_O(), Block_S(), Block_T(), Block_Z()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def left_move(self):
        self.current_block.move(0,-1)
        if self.block_in_screen() == False or self.if_block_fits() == False:
            self.current_block.move(0,1)
    
    def right_move(self):
        self.current_block.move(0,1)
        if self.block_in_screen() == False or self.if_block_fits() == False:
            self.current_block.move(0,-1)

    def down_move(self):
        self.current_block.move(1,0)
        if self.block_in_screen() == False or self.if_block_fits() == False:
            self.current_block.move(-1,0)
            self.pause_block()

    def if_block_fits(self):
        block_tiles = self.current_block.new_cell_pos()
        for tile in block_tiles:
            if self.grid.cell_empty(tile.row , tile.col) == False:
                return False
        return True
 

    def pause_block(self):
        block_tiles = self.current_block.new_cell_pos()
        for position in block_tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.random_block()
        cleared_rows = self.grid.clearing_the_row()
        if cleared_rows>0:
            self.clearing_sound.play()
            self.score_system(cleared_rows)
            self.lines(cleared_rows)
        if not self.if_block_fits():
            self.game_over = True
            self.current_block.move(-1,0)
            p.mixer.music.pause()
            self.gameover_sound.play()

    
    def rotate_block(self):
        self.current_block.rotate_block()
        if self.block_in_screen() == False or self.if_block_fits()==False:
            self.current_block.undo_rotate()
            
    
    def block_in_screen(self):
        block_tiles = self.current_block.new_cell_pos()
        for tile in block_tiles:
            if self.grid.screen_limit(tile.row , tile.col) == False:
                return False
        return True
    
    def game_reset(self):
        self.grid.game_reset()
        self.blocks =  [ Block_I(), Block_J(), Block_L(), Block_O(), Block_S(), Block_T(), Block_Z()]
        self.current_block = self.random_block()
        self.next_block = self.random_block()
        self.score = 0
        self.line = 0
        p.mixer.music.play(-1)



    def draw_blocks(self, game_screen):
        self.grid.draw_grid(game_screen)
        self.current_block.draw_blocks(game_screen,11,11)

        #soltuion or I and O block
        if self.next_block.id == 4:
            self.next_block.draw_blocks(game_screen, 255 ,290)
        if self.next_block.id == 7:
            self.next_block.draw_blocks(game_screen, 255 ,290)
        if not (self.next_block.id == 4 or  self.next_block.id == 7):
            self.next_block.draw_blocks(game_screen, 270,280)