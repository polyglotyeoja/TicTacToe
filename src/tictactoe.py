class TicTacToe():
    gridsize = (3,3)
    x, y = gridsize
    self.coordinates = set(product(range(x), range(y)))


a = TicTacToe()
print(a.coordinates)
