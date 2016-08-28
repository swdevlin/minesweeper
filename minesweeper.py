EASY = 1
MEDIUM = 2
HARD = 3

class minesweeper:
  def __init__(self, type):
    if type == EASY:
      self.rows = 9
      self.columns = 9
      self.board = [0] * 81
    elif type == MEDIUM:
      self.rows = 16
      self.columns = 16
      self.board = [0] * 256
    elif type == HARD:
      self.rows = 16
      self.columns = 30
      self.board = [0] * 480
