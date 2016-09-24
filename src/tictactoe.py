from itertools import product
import random

class ButtonState(object):
    X = "X"
    O = "O"
    empty = "0"

class TicTacToe():
    def __init__(self):
        gridsize = (3,3)
        x, y = gridsize
        self.coordinates = set(product(range(x), range(y)))
        self.grid = [[ButtonState.empty for i in range(x)] for j in range(y)]

    def input_to_grid(self,value,row, column):
        self.grid[row][column] = value;
        return self.grid

    def get_game_status(self,user):
        #check the columns, diagonals, rows with a counter
        row_counter = 0
        col_counter = 0
        if(user == "X"):
            search_value = "X"
            for i in range(3):
                for j in range(3):
                    if(self.grid[i][j] == search_value):
                        row_counter+=1
                    if(self.grid[j][i] == search_value):
                        col_counter+=1
                if((row_counter != 3 )and (col_counter != 3)):
                    print('row count: ', row_counter)
                    print('col count: ',col_counter)
                row_counter = 0
                col_counter = 0









a = TicTacToe()
a.input_to_grid("X",0,0)
a.input_to_grid("X",2,1)
a.input_to_grid("X",2,2)
a.get_game_status(ButtonState.X)
