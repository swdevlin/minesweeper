import random
EASY = 1
MEDIUM = 2
HARD = 3

HIT = False
MISS = True

class minesweeper:
  def __init__(self, type):
    if type == EASY:
      self.rows = 9
      self.columns = 9
    elif type == MEDIUM:
      self.rows = 16
      self.columns = 16
    elif type == HARD:
      self.rows = 16
      self.columns = 30
    cells = self.rows * self.columns
    self.playerBoard = ['?'] * cells
    self.clear()
    self.setupMines(type)

  def cell(self,r,c):
    return self.playerBoard[r * self.columns + c]
    
  def clear(self):
    cells = self.rows * self.columns
    self.board = [False] * cells
  
  def setupMines(self, type):
    for i in range(0,len(self.board)-1):
      self.board[i] = False
    if type == EASY:
      mines = 10
    elif type == MEDIUM:
      mines = 40
    elif type == HARD:
      mines = 99
      
    while mines > 0:
      x = random.randint(0, self.rows-1)
      y = random.randint(0, self.columns-1)
      index = x * self.columns + y
      if not self.board[index]:
        self.board[index] = True
        mines -= 1

  def adjacentMines(self,row,col):
    count=0
    for r in range(-1,2):
      for c in range(-1,2):
        if not (r==c and r == 0):
          if r + row >= 0 and r+row < self.rows:
            if c+col >=0 and c+col < self.columns:
              if self.board[(r+row)*self.columns+c+col]:
                count += 1
    return count

  def reveal(self, row, col, visited):
    mines = self.adjacentMines(row,col)
    visited.append(row*self.columns+col)
    if mines > 0:
      self.playerBoard[row*self.columns+col] = str(mines)
    else:
      self.playerBoard[row*self.columns+col] = ' '
      for r in range(row-1,row+2):
        if r >= 0 and r < self.rows:
          for c in range(col-1,col+2):
            if c >= 0 and c < self.columns:
              index = r*self.columns + c
              if not index in visited:
                self.reveal(r,c,visited)

  def click(self, r, c):
    if (self.board[r*self.columns+c]):
      return HIT
    else:
      visited = []
      self.reveal(r,c,visited)
      return MISS