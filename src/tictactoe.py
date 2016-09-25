from itertools import product
import random


class ButtonState(object):
    X = "X"
    O = "O"
    empty = "0"

class GameStatus(object):
    Won = 'W'
    Loss = 'L'
    InProgress = 'I'

class TicTacToe():
    def __init__(self):
        self.grid = [[ButtonState.empty for i in range(3)] for j in range(3)]

    def input_to_grid(self,value,row, column):
        self.grid[row][column] = value;
        return self.grid
    def divide(self, i, j):
        try:
            return self.x/self.y
        except ZeroDivisionError:
            return None
    def get_game_status(self, user):
        #check the columns, diagonals, rows with a counter"
        row_counter = 0
        col_counter = 0
        diagonal_counter = 0
        #1 - row
        #2 - col
        #3 - diagonals
        if(user == "X"):
            search_value = "X"
            for i in range(3):
                for j in range(3):
                    if(self.grid[i][j] == search_value):
                        row_counter+=1
                    if(self.grid[j][i] == search_value):
                        col_counter += 1
                    if((i + j) % 2 == 0):
                        if(self.grid[i][j] == search_value):
                            diagonal_counter += 1
                if((row_counter == 3 ) or (col_counter == 3) or (diagonal_counter == 3)):
                    return GameStatus.Won
                row_counter=0
                col_counter=0











a = TicTacToe()
# # a.input_to_grid("X",0,0)
# # a.input_to_grid("X",1,0)
# # a.input_to_grid("X",2,0)
# print(a.grid)
# a.get_game_status(ButtonState.X)
