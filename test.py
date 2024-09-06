import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_state(self):
        self.assertEqual(self.game.current_player, 'X')
        self.assertFalse(self.game.game_over)
        self.assertEqual(self.game.board, [['', '', ''], ['', '', ''], ['', '', '']])

    def test_play(self):
        self.game.play(0, 0)
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')

    def test_winner(self):
        self.game.play(0, 0)
        self.game.play(1, 0)
        self.game.play(0, 1)
        self.game.play(1, 1)
        self.game.play(0, 2)
        self.assertTrue(self.game.game_over)

if __name__ == '__main__':
    unittest.main()
