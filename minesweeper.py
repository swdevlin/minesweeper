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
    self.board = [False] * cells
    self.setupMines(type)

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
        mines = mines - 1

  def click(self, r, c):
    if (self.board[r*self.columns+c]):
      return HIT
    else:
      return MISS