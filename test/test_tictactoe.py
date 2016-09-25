import unittest
import sys
from TicTacToe import *
from types import MethodType
from nose import with_setup

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe()

    def test_canary(self):
        self.assertTrue(True)

    def test_change_button(self):
        self.tictactoe.grid[2][0] = ButtonState.X
        self.assertEqual(ButtonState.X, self.tictactoe.grid[2][0])

    def test_win_by_column(self):
        self.tictactoe.grid[0][0] = ButtonState.X
        self.tictactoe.grid[1][0] = ButtonState.X
        self.tictactoe.grid[2][0] = ButtonState.X
        self.assertEqual(GameStatus.Won, self.tictactoe.get_game_status("X"))



if __name__ == '__main__':
    unittest.main()
