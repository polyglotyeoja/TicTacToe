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

    

a = TicTacToe()
print(a.grid)
