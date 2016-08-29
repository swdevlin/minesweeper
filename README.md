# minesweeper

* ~~figure out the minesweeper rules~~
* ~~create board code~~
* code to handle player board
* server
* web to create a new game
* web to toggle a grid
* web to submit a final board

## Diary

**2016-08-28**

Rules used are from here: http://www.wikihow.com/Play-Minesweeper

Surprised that an array does not have a len method

Range is [) . It took a little while to figure that out. Handy, but weird.

4 hours in, game engine nearing completion. Still need to work on flagging/unflagging cells and check to see if answer is correct.

**2016-08-29**

Storing flags in a list. I don't think I need to use a matrix for them, and I don't want to replace the state of the player board incase someone flags a cell and then finds out the cell has no mine.

I am not sure if my returns codes should be an enum or not. Still pondering that.

True and False needing to be upper case is annoying

I think the engine is done; 5 hours time to code. Code coverage is at 99%.

Now for the UI.
