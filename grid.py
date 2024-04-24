import pygame as p
from colors import Colors


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.cell_colors()




    def screen_limit(self, row , col):
        if row>= 0 and row <self.num_rows and col>=0 and col < self.num_cols:
            return True
        return False
    
    def cell_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False
    
    def row_full(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True

    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0

    def row_moves_down(self, start_row):
        for row in range(start_row, 0, -1):
            for col in range(self.num_cols):
                self.grid[row][col] = self.grid[row - 1][col]
        # Clear the top row after shifting all rows down
            if row == 1:
                for col in range(self.num_cols):
                    self.grid[0][col] = 0

    def clearing_the_row(self):
        completed = 0
        for row in range(self.num_rows - 1, -1, -1):
            while self.row_full(row):
                self.clear_row(row)
                self.row_moves_down(row)
                completed += 1
        return completed
    

    def game_reset(self):
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    self.grid[row][col] = 0


    #drawing the grid
    def draw_grid(self, game_screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = p.Rect(col*self.cell_size +11 , row*self.cell_size +11 , self.cell_size -1, self.cell_size-1)
                p.draw.rect(game_screen, self.colors[cell_value], cell_rect)
