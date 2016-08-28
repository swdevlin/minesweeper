import unittest
import minesweeper

class TestMinesweeper(unittest.TestCase):
  def test_easy(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    self.assertEqual(len(board.board), 81)
    self.assertEqual(board.rows, 9)
    self.assertEqual(board.columns, 9)
    
  def test_medium(self):
    board = minesweeper.minesweeper(minesweeper.MEDIUM)
    self.assertEqual(len(board.board), 256)
    self.assertEqual(board.rows, 16)
    self.assertEqual(board.columns, 16)
    
  def test_hard(self):
    board = minesweeper.minesweeper(minesweeper.HARD)
    self.assertEqual(len(board.board), 480)
    self.assertEqual(board.rows, 16)
    self.assertEqual(board.columns, 30)
    
if __name__ == '__main__':
  unittest.main()
