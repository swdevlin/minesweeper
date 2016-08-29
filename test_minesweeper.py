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
        if board.cell(r,c) == '?':
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

  def test_click_mine_hitmiss(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    board.board[3] = True
    hitMine = board.click(0,3)
    self.assertEqual(hitMine, minesweeper.HIT)

    board.board[3] = False
    hitMine = board.click(0,3)
    self.assertEqual(hitMine, minesweeper.MISS)

  def test_clear(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    board.clear()
    count = 0
    for r in range(0, board.rows):
      for c in range(0, board.columns):
        if board.board[r*board.columns + c]:
          count = count + 1
    self.assertEqual(count, 0)
  
  def test_click_mine_cell_blank(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    board.clear()
    hitMine = board.click(0,3)
    self.assertEqual(board.cell(0,3), ' ')
    
  def test_adjacentMines(self):
    board = minesweeper.minesweeper(minesweeper.HARD)
    board.clear()
    mines = board.adjacentMines(1,1)
    self.assertEqual(mines, 0)
    mines = board.adjacentMines(0,0)
    self.assertEqual(mines, 0)
    mines = board.adjacentMines(0,board.columns-1)
    self.assertEqual(mines, 0)
    mines = board.adjacentMines(board.rows-1,0)
    self.assertEqual(mines, 0)
    mines = board.adjacentMines(board.rows-1,board.columns-1)
    self.assertEqual(mines, 0)

    board.board[0] = True # 0,0 
    mines = board.adjacentMines(1,1)
    self.assertEqual(mines, 1)
    mines = board.adjacentMines(0,1)
    self.assertEqual(mines, 1)
    mines = board.adjacentMines(1,0)
    self.assertEqual(mines, 1)
    mines = board.adjacentMines(2,2)
    self.assertEqual(mines, 0)

    board.board[1] = True # 0,1
    mines = board.adjacentMines(1,1)
    self.assertEqual(mines, 2)
    # cell's own mine does not count for adjacency
    mines = board.adjacentMines(0,1)
    self.assertEqual(mines, 1)

    board.board[2] = True # 0,2
    board.board[board.columns] = True # 1,0
    board.board[board.columns+1] = True # 1,1
    board.board[board.columns+2] = True # 1,2
    board.board[2*board.columns] = True # 2,0
    board.board[2*board.columns+1] = True # 2,1
    board.board[2*board.columns+2] = True # 2,2
    mines = board.adjacentMines(1,1)
    self.assertEqual(mines, 8)
    
  def test_click_reveal(self):
    board = minesweeper.minesweeper(minesweeper.EASY)
    board.clear()
    '''
    000100000
    000100000
    000100000
    111100000
    000000000
    000000000
    000000000
    000000000
    000000000
    '''
    board.board[ 0+3] = True
    board.board[ 9+3] = True
    board.board[18+3] = True
    board.board[27+0] = True
    board.board[27+1] = True
    board.board[27+2] = True
    board.board[27+3] = True

    hitMine = board.click(1,1)
    self.assertEqual(hitMine, minesweeper.MISS)
    self.assertEqual(board.cell(0,0), ' ')
    self.assertEqual(board.cell(0,1), ' ')
    self.assertEqual(board.cell(0,2), '2')
    self.assertEqual(board.cell(0,3), '?')
    self.assertEqual(board.cell(1,0), ' ')
    self.assertEqual(board.cell(1,1), ' ')
    self.assertEqual(board.cell(1,2), '3')
    self.assertEqual(board.cell(1,3), '?')
    self.assertEqual(board.cell(2,0), '2')
    self.assertEqual(board.cell(2,1), '3')
    self.assertEqual(board.cell(2,2), '5')
    self.assertEqual(board.cell(3,3), '?')
    self.assertEqual(board.cell(3,0), '?')
    self.assertEqual(board.cell(3,1), '?')
    self.assertEqual(board.cell(3,2), '?')
    self.assertEqual(board.cell(3,3), '?')
    
if __name__ == '__main__':
  unittest.main()
