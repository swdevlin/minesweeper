from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from game.models import Game
import json
import sys

def index(request):
  template = loader.get_template('game/index.html')
  context = {}
  return HttpResponse(template.render(context, request))
 
def new_game(request):
  template = loader.get_template('game/new.html')
  context = {}
  return HttpResponse(template.render(context, request))
  
@csrf_exempt
def click_cell(request, game_id):
  try:
    row = request.POST['row']
    col = request.POST['col']
    game = Game.objects.get(id=int(game_id))
    game.fromDB()
    result = game.game.click(int(row), int(col))
    game.save()
    return HttpResponse(json.dumps({'result': result, 'board': game.game.playerBoard}))
  except:
    print(sys.exc_info()[0])
    return HttpReponseBadRequest('game id, row, or col not valid')

@csrf_exempt
def create_game(request):
  try:
    diff = request.POST['difficulty']
    if diff == 'easy':
      game = Game.createEasy()
    elif diff == 'standard':
      game = Game.createStandard()
    elif diff == 'standard':
      game = Game.createHard()
    else:
      return HttpReponseBadRequest('difficulty can only be easy, standard, or hard')
    game.save()
    return HttpResponse(json.dumps({'id': game.id, 'rows': game.game.rows, 'columns': game.game.columns, 'flags': game.game.flags, 'board': game.game.playerBoard, 'mines': game.game.numberOfMines()}))
  except:
    return HttpResponse(-2)

def resume_game(request, game_id):
  template = loader.get_template('game/board.html')
  context = {}
  return HttpResponse(template.render(context, request))

@csrf_exempt
def flag_cell(request, game_id):
  try:
    row = request.POST['row']
    col = request.POST['col']
    game = Game.objects.get(id=int(game_id))
    game.fromDB()
    result = game.game.plantFlag(int(row), int(col))
    game.save()
    return HttpResponse(json.dumps({'board': game.game.playerBoard, 'flags': game.game.flags}))
  except:
    print(sys.exc_info()[0])
    return HttpReponseBadRequest('game id, row, or col not valid')

@csrf_exempt
def unflag_cell(request, game_id):
  try:
    row = request.POST['row']
    col = request.POST['col']
    game = Game.objects.get(id=int(game_id))
    game.fromDB()
    result = game.game.removeFlag(int(row), int(col))
    game.save()
    return HttpResponse(json.dumps({'board': game.game.playerBoard, 'flags': game.game.flags}))
  except:
    print(sys.exc_info()[0])
    return HttpReponseBadRequest('game id, row, or col not valid')

  