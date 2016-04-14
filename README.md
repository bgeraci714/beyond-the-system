# final-project
A procedurally generated space exploration game meant to serve as the final project for our programming fundamentals class.

The game can be broken down into several key components. 

1. The introductory phase.

  1a. Introducing the setting, what the point of the game is, etc. 
  
  1b. Resource gathering and possibly ship building? 
  
2. The space exploration phase
3. 
  2a. procedural generation of sections of space with different events per square per map

  2b. semi-randomized events to provide diversity of gameplay (not sure how many we want here, 15+?)
  
    * a big question here is how many events do we want to include in a single game? 
    
    **  I think we should try shooting for creating 2.5x the number of events so that you have to play
        the game at least two + times without running seeing everything 
        
    *** We might also want specific scripted events as well to contain whatever level of story 
        we're going to try to implement. 
        
  2c. survival aspects that place greater emphasis on resource management and choices in events
  
3. The ending of the game. (15-25 minutes)

  3a. You made it to Earth ("Hooray!")
  
  3b. You got lost and died in space ("Awww")
  
  3c. You landed on a paradise planet and decide to stay there (or stopped happily along the way)
  
  
INTRODUCTION

We'll need to decide how to implement the starting points of the game. 
  Just a series of text choices? 
  A small map to introduce movement and how the game will work (a tutorial of sorts)?
  How important do we want the introduction to be for the rest of the game? 

MAP MAKING

The major chunk of the work is thus in developing the code for the maps, such that they work both functionally
and visually to give the player a sense of depth. This will require some algorithmic determination of the map
if we want it to be random/semi-random. 

EVENT GENERATION

Event generation is going to take a good amount of thinking but once the code for incorporating them and their important facets
(such as what resources you get or lose based on how the event turns out, at what point you encounter it, how to determine choices, 
etc.) it should be pretty straight forward to create them (or make an event generation program). 
  
RESOURCES/KEY ITEMS/ITEMS(?)

What we resources do we want to implement/require (fuel, food, mental_health, etc.)?
What key (or regular) items do we want (maps of a galaxies? cook books? ship upgrades? robots?)

STORAGE/LOGISTICS

The next chunk is figuring out how to set up the events both in their storage and implementation. Pickling/shelving 
might work really well here so that we don't need to worry about having all the events stored in the python file itself. 
What might also prove really useful is if we can create python files with all the important classes and functions and keep 
them separate from the main game's python file. Doing something like "import all_the_classes" or "import all the functions"
might make the code cleaner and easier to debug as necessary. 

SAVE FILES
Pickling will also be helpful for creating save files or high scores (if we think they would work in the context of the game)



