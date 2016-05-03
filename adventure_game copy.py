## Blake Geraci
## Chapter 9: Challenge 4
## Create a simple adventure game where a player can travel between
## various connected locations. 

title = "\n\t\tWelcome to the room traversal adventure game!"
intro = """
It is your goal to make it from the first room to the last.
We've recently moved out so there's not a whole lot left to see. 
You have as many steps as you need so take your time and enjoy
exploring the empty rooms. Every room is a different size with
different dimensions so who knows what shapes you'll run in to.


"""
outro = """
Looks like you've opened your final door.
I hope you had a nice time looking around.
Come again soon!

-- Sincerely,

Home Owners
"""

class Map(object):
    """Creates map object."""
    

    def __init__(self, numRows, numCols, charSym = "S", startRow = 9, startCol = 5, blankTile = "_"):
        self.numCols = numCols
        self.numRows = numRows
        self.charSym = charSym
        self.position = [startRow,startCol]
        self.blankTile = blankTile
        self.foundDoor = False
        self.tileList = []
        self.blockedTiles = []

        ## create empty list
        self.grid = []
        for row in range(self.numRows): ##append empty list numCols times to grid
            self.grid.append([])
        for row in self.grid: ## for each empty list
            for col in range(self.numCols): ## for the num of times perscribed by numRows
                row.append(self.blankTile) ##add char sizeY times to the sub list within row

        ## experiment
        for row in range(self.numRows): ## for each empty list
            for col in range(self.numCols): ## for the num of times perscribed by numRows
                self.grid[row][col] = " "

    def displayMap(self):
        print (" "+"-" * 2 * self.numCols)
        for row in range (self.numRows):
            print("|", end="")
            for col in range (self.numCols):
                print(self.grid[row][col], end=" ")
            print("|")
        print (" "+"-" * 2 * self.numCols)
        
    def setCharPosition(self, position = None):
        if position == None:
            position = self.position
        self.grid[position[0]][position[1]] = self.charSym

    def addBox(self, position = [1,1], length = 2):
        for i in range(length):
            for k in range(length):
                self.grid[position[0]+i][position[1]+k] = "#"
                blockedPosition  = [position[0]+i,position[1]+k]
                self.blockedTiles.append(blockedPosition)
            
        i = 0
        if length > 1:
            for i in range(length):
                self.grid[position[0]+i][position[1]+1] = "#"
                blockedPosition = [position[0]+i,position[1]+1]
                self.blockedTiles.append(blockedPosition)
            
        
    
        
    def populateTiles(self, numTiles):
        """Creates numbered tiles at random."""
        import random
        usedTileLocations = []
        tileChar = "O"
        
        for tile in range(numTiles):
            
            randomCol = random.randrange(self.numCols)
            randomRow = random.randrange(self.numRows)

            ## checks to make sure we don't populate a tile containing our ship
            while [randomRow, randomCol] == self.position or [randomRow,randomCol] in usedTileLocations or [randomRow,randomCol] in self.blockedTiles:
                randomCol = random.randrange(self.numCols)
                randomRow = random.randrange(self.numRows)

            ## add to list of already used tile locations    
            usedTileLocations.append([randomRow,randomCol])
            
            self.grid[randomRow][randomCol] = str(tileChar)
            
            tileInfo = [tile, [randomRow, randomCol]]
            self.tileList.append(tileInfo)

    def isValid(self, position):
        if position[0] < 0 or position[1] < 0:
            return False
        elif position[0] >= self.numRows or position[1] >= self.numCols:
            return False
        elif position in self.blockedTiles:
            return False
        else:
            return True

    def changeTile(self, position, tile="t"):
        """Change specific tile (position[row,col], tile character) """
        if self.isValid(position):
            self.grid[int(position[0])][int(position[1])] = tile
        else:
            print("Not a valid position on the map")
            
    

    ## move functions
    def move_up(self):
        self.position[0] -= 1
        self.charSym = "^"

    def move_down(self):
        self.position[0] += 1
        self.charSym = "v"

    def move_left(self):
        self.position[1] -= 1
        self.charSym = "<"

    def move_right(self):
        self.position[1] += 1
        self.charSym = ">"

    def movement(self):
        ## dictionary of move_ functions
        moves = {"w":self.move_up, "s":self.move_down, "a":self.move_left, "d":self.move_right}

        ## create list of dictionary keys for cleaner code when checking their validity
        movesList = []
        for move in moves:
            movesList.append(move)
            
        moveMenu = "\nChoose a movement: \nw.Up\na.Left\ns.Down\nd.Right\n"

        ## clears out original tile and replaces it with a blank
        
        self.changeTile(self.position, self.blankTile)
        
        
        validMove = False 
        move = None

        while not validMove:
            originalPosition = self.position[:]
            ## might move this outside of movement method to provide ways of ending movement/more options
            while move not in movesList:
                move = str(input(moveMenu))
            ## Uses functions stored in dictionary.
            moves[move]()
            if self.isValid(self.position):
                validMove = True
        
                ## COLLISION TESTING!!! MIGHT WANT TO MAKE A SEPARATE FUNCTION
                for tile in self.tileList:
                    if self.position == tile[1]:
                        self.tileList.remove(tile)
                        print("You found the door!!\n")
                        self.foundDoor = True

            elif not self.isValid(self.position):
                self.position = originalPosition
                move = None
            else:
                printf("An error occurred!")
            
        self.changeTile(self.position, self.charSym)
       
class Dungeon (object):
    """A Collection of Maps"""
    
    def __init__ (self, maps):
        import random
        self.maps = []
        self.numMaps = maps
        self.minLength = 5
        self.maxLength = 8

        for i in range(maps):
            random1 = random.randint(self.minLength, self.maxLength)
            random2 = random.randint(self.minLength, self.maxLength)
            mapNew = Map(random1,random2, "^", 0, 0, " ")
            mapNew.setCharPosition()
            for i in range(2):
                #print(i)
                boxSpot = [1, 2]
                mapNew.addBox(boxSpot, 2)
            mapNew.populateTiles(1)
            self.maps.append(mapNew)
    def play(self):
        
        mapCounter = 0
        while mapCounter < self.numMaps:
            self.maps[mapCounter].displayMap()
            self.maps[mapCounter].movement()
            if self.maps[mapCounter].foundDoor:
                mapCounter += 1

def getRoomNumber():
    while True: 
        try:
            numRooms = int(input("How many rooms would you like to traverse?\n"))
            break
        except:
            print("That's not a number I can use!")
    return numRooms

def main():

    print(title)
    print(intro)

    numRooms = getRoomNumber()

    dungeon = Dungeon(numRooms)
    dungeon.play()
        

        
    print(outro)

main()
