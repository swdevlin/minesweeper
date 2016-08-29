import unittest
import minesweeper

class TestMinesweeper(unittest.TestCase):
  def test_easy(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    self.assertEqual(len(board.board), 81)
    self.assertEqual(board.rows, 9)
    self.assertEqual(board.columns, 9)

  def test_easy_has_10(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    count = 0
    for r in range(0, board.rows):
      for c in range(0, board.columns):
        if board.board[r*board.columns + c]:
          count = count + 1
    self.assertEqual(count, 10)
    
  def test_init_allunknown(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    count = 0
    for r in range(0, board.rows):
      for c in range(0, board.columns):
        if board.playerBoard[r*board.columns + c] == '?':
          count = count + 1
    self.assertEqual(count, board.rows*board.columns)

    board = minesweeper.minesweeper(minesweeper.MEDIUM)
    count = 0
    for r in range(0, board.rows):
      for c in range(0, board.columns):
        if board.playerBoard[r*board.columns + c] == '?':
          count = count + 1
    self.assertEqual(count, board.rows*board.columns)

    board = minesweeper.minesweeper(minesweeper.HARD)
    count = 0
    for r in range(0, board.rows):
      for c in range(0, board.columns):
        if board.playerBoard[r*board.columns + c] == '?':
          count = count + 1
    self.assertEqual(count, board.rows*board.columns)
    
  def test_medium(self):
    board = minesweeper.minesweeper(minesweeper.MEDIUM)
    self.assertEqual(len(board.board), 256)
    self.assertEqual(board.rows, 16)
    self.assertEqual(board.columns, 16)
    
  def test_medium_has_40(self):
    board = minesweeper.minesweeper(minesweeper.MEDIUM)
    count = 0
    for r in range(0, board.rows):
      for c in range(0, board.columns):
        if board.board[r*board.columns + c]:
          count = count + 1
    self.assertEqual(count, 40)
    
  def test_hard(self):
    board = minesweeper.minesweeper(minesweeper.HARD)
    self.assertEqual(len(board.board), 480)
    self.assertEqual(board.rows, 16)
    self.assertEqual(board.columns, 30)
    
  def test_hard_has_99(self):
    board = minesweeper.minesweeper(minesweeper.HARD)
    count = 0
    for r in range(0, board.rows):
      for c in range(0, board.columns):
        if board.board[r*board.columns + c]:
          count = count + 1
    self.assertEqual(count, 99)
    
  def test_click_mine(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    board.board[3] = True
    hitMine = board.click(0,3)
    self.assertEqual(hitMine, minesweeper.HIT)

    board.board[3] = False
    hitMine = board.click(0,3)
    self.assertEqual(hitMine, minesweeper.MISS)
    
if __name__ == '__main__':
  unittest.main()
