var game
var gamesUrl = '/game/games'
var ctrlIsDown = false
var size = 22
var elapsedTime = 0
var timer
var boardWidth = 0

function windowResized() {
  if (boardWidth === 0)
    return
  var width = $('#gameboard').width()
  var diff = (width-boardWidth)/2
  if (Math.abs(diff) >= 1) {
    $('.cell').each(function(index) {
      var cell = $(this)
      var p = cell.position()
      var l = p.left + diff
      cell.css({left: l+'px'})
    })
    boardWidth = width
  }
}

$(document).keydown(function(event){
  if (event.which=="17")
    ctrlIsDown = true;
});

$(document).keyup(function(){
  ctrlIsDown = false;
});

function minesRemaining() {
  var r = game.mines - game.flags.length
  if (r < 10)
    return '0' + r
  else
    return r
}

function hiddenCells() {
  var count = 0
  for (var i=0; i< game.board.length; i++)
    if (game.board[i] === '?')
      count++
  return count
}

function incrementTime() {
  elapsedTime++
  var zeros = ''
  if (elapsedTime < 10)
    zeros = '000'
  else if (elapsedTime < 100)
    zeros = '00'
  else if (elapsedTime < 1000)
    zeros = '0'
  $('#footer-right').html(zeros + elapsedTime)
}

function createdBoard(data) {
  game = JSON.parse(data)
  $('#gameboard').height(game.rows*size+size)
  $('#footer').collapse()
  renderBoard()
  elapsedTime = 0
  timer = setInterval(incrementTime, 1000)
}

$(document).ready(function() {
  $('#easy').click(function() {
    $.post(gamesUrl, {difficulty: 'easy'}, createdBoard)
  })
  $('#standard').click(function() {
    $.post(gamesUrl, {difficulty: 'standard'}, createdBoard)
  })
  $('#hard').click(function() {
    $.post(gamesUrl, {difficulty: 'hard'}, createdBoard)
  })
})

function findClickableCells() {
  var cells=$('.unknown')
  return cells
}

function plantFlag(row, col) {
  var index = row*game.columns + col
  var handler = $.inArray(index, game.flags) >= 0 ? 'unflag_cell' : 'flag_cell'
  var cell = {row: row, col: col}
  $.post('/game/game/' + game.id + '/' + handler, cell, function(data) {
    data = JSON.parse(data)
    game.board = data.board
    game.flags = data.flags
    renderBoard()
  })
}

function clickCell(row, col) {
  $.post('/game/game/' + game.id + '/click_cell', {row: row, col: col}, function(data) {
    data = JSON.parse(data)
    if (data.result) {
      game.board = data.board
      renderBoard()
    } else {
      var cells = findClickableCells()
      cells.off('click')
      cells.css('cursor', 'auto');
      clearInterval(timer)
      $('#footer').css('background-color', '#f2dede')
      $('#message').html('You lose').addClass('text-danger').show()
    }
  })
}

function cellClicked() {
  var cell = $(this)
  var row = parseInt(cell.attr('data-row'))         
  var col = parseInt(cell.attr('data-col'))
  var index = row*game.columns + col
  if (game.board[index] !== '?')
    return
  if (ctrlIsDown)
    plantFlag(row, col)
  else
    clickCell(row, col)
}

function renderBoard() {
  var grid=''
  var r,c
  var rOffset = 0
  var cOffset = 0
  var width = $('#gameboard').width()
  var cellWidth = size * game.columns
  var colStart = (width - cellWidth)/2
  for (r=0; r < game.rows; r++) {
    cOffset = colStart
    for (c=0; c < game.columns; c++) {
      var index = r*game.columns + c
      var state
      var symbol
      if ($.inArray(index, game.flags) >=0) {
        symbol = '⚑'
        state = 'unknown flag'
      } else if (game.board[index] == '?') {
        symbol = ' '
        state = 'unknown'
      } else if (game.board[index] == ' ') {
        state = 'empty'
        symbol = ' '
      } else {
        state = 'C' + game.board[index] + ' number'
        symbol = game.board[index]
      }
      grid+='<div class="cell ' + state + '" data-row="' + r + '" data-col="' + c + '" style="position:absolute; top:' + rOffset + 'px; left:' + cOffset + 'px;">' + symbol + '</div>'
      cOffset+=size
    } 
    rOffset += size
  }
  boardWidth = width
  $('#gameboard').html(grid)
  $('#footer-left').html(minesRemaining() + ' mines')
  if (hiddenCells() === game.mines) {
    clearInterval(timer)
    $('#footer').css('background-color', '#dff0d8')
    $('#message').html('You win').addClass('text-success').show()
  } else {
    var cells = findClickableCells()
    cells.css('cursor', 'pointer');        
    cells.click(cellClicked)
  } 
}
