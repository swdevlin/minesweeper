from django.db import models
from minesweeper import minesweeper
import json

class Game(models.Model):
  rows = models.IntegerField(default=9)
  columns = models.IntegerField(default=9)
  difficulty = models.IntegerField(default=minesweeper.EASY)
  board = models.TextField()
  flags = models.TextField()
  playerBoard = models.TextField()
  startedAt = models.DateTimeField(auto_now_add=True)

  @classmethod
  def createEasy(cls):
    return cls.create(minesweeper.EASY)

  @classmethod
  def createStandard(cls):
    return cls.create(minesweeper.MEDIUM)

  @classmethod
  def createHard(cls):
    return cls.create(minesweeper.HARD)

  @classmethod
  def create(cls, diff):
    g = cls(difficulty=diff)
    g.game = minesweeper.Minesweeper(diff)
    return g

  def save(self, *args, **kwargs):
    self.rows = self.game.rows
    self.columns = self.game.columns
    self.board = json.dumps(self.game.board)
    self.playerBoard = json.dumps(self.game.playerBoard)
    self.flags = json.dumps(self.game.flags)    
    super(Game, self).save(args, kwargs)
    
  def fromDB(self):
    self.game = minesweeper.Minesweeper(self.difficulty)
    self.game.rows = self.rows
    self.game.columns = self.columns
    self.game.board = json.loads(self.board)
    self.game.playerBoard = json.loads(self.playerBoard)
    self.game.flags = json.loads(self.flags)
