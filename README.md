# minesweeper

* ~~figure out the minesweeper rules~~
* ~~create board code~~
* ~~code to handle player board~~
* ~~server~~
* ~~web to create a new game~~
* ~~web to toggle a grid~~
* ~~web to submit a final board~~
* ~~Resume game~~
* ~~Warn if game id is not correct~~

## Diary

**2016-08-28**

Rules used are from here: http://www.wikihow.com/Play-Minesweeper

Surprised that an array does not have a len method

Range is [min,max). It took a little while to figure that out. Handy, but weird.

4 hours in, game engine nearing completion. Still need to work on flagging/unflagging cells and check to see if answer is correct.

**2016-08-29**

Storing flags in a list. I don't think I need to use a matrix for them, and I don't want to replace the state of the player board incase someone flags a cell and then finds out the cell has no mine.

I am not sure if my returns codes should be an enum or not. Still pondering that.

True and False needing to be upper case is annoying

I think the engine is done; 5 hours time to code. Code coverage is at 99%.

Now for the UI.

**2016-08-30**

UI is done. Yay for Google fonts.

I wanted to keep right click working in order to inspect the UI. To plant a flag you use ctrl + mouse click

Time for the UI was 8 hours.

ReST API in Django don't match my mental model. node.js/Express does a great
job of mapping code to ReST interfaces. From my limited exposure I feel like
Django is more about heavy backend processes than pure ReST API calls. I did
find a reference to a Django plug-in that makes ReST APIs cleaner. But it
seemed really tied to the ORM, and would have meant learning something else
new so I decided to pass for this exercise.

I had a problem with permissions when POSTing to a url. I used ```@csrf_exempt```
instead of fighting with the Django permission model. Obviously, with production
code, I would get the permission model to work.

When you click on a cell with a bomb the game state on the server is not
updated to reflect that. So if you refresh the browser and enter the 
last game you played, you can resume without having blown up. I am 
sure that's a feature. :blush: There should be a better interface for
resuming a game. Maybe list past games, or at least show the maximum game number.

## General Notes

Python seems simple enough; library support appears to be excellent. Django was easy
enough to dive into. Apps and Projects had me scratching my head for a few minutes.

I did a premature optimization by storing the boards as arrays instead of matrices. 
I gambled that the ORM would handle mapping that to a DB field but would have
problems with a matrix. Turns out that was not the case. I ended up having to 
create JSON strings of the boards and storing those. If I am doing that, they could
be matrices. But, I am late in to my allotted time so I am going with what I have.

I could not figure out a clean way of using multiple inheritance to combine model 
and my Minesweeper class. If there is no good way to do that, I guess Django expects
all storable objects to inherit off Model. I thought about making my Minesweeper class
inherit from Model, but I would have the same problem of lists and matrices. I did
ponder using a string to hold the assorted boards. But turns out one can't replace
a character in a string using [], one needs to splice and dice. I was not keen on
that so I left the code as I work it.

I overloaded the save method to create JSON strings of the Minesweeper data and
assign them to the Model fields. I could not find a way to do the reverse: trigger
a function after an object is loaded from the database. Because of that, I added
a fromDB method with converts the JSON fields to lists and then updates the
Minesweeper object. Again, not elegant, but it works.
