class Map(object):
    """Creates map object."""
    import events
    import ShipClass

    def __init__(self, numRows, numCols, charSym = "S", startRow = 0, startCol = 0, blankTile = "_"):
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

        self.grid[self.position[0]][self.position[1]] = self.charSym

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
            
            self.grid[randomRow][randomCol] = str(tile)
            
            tileInfo = [tile, [randomRow, randomCol], ["example", 2]]
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
    
    def movement(self):   ## I want to pass the ship to movement. 
        import events
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
                    ## checks if tile is a door
                    if self.position == tile[1] and tile[0] == 0:
                        self.tileList.remove(tile)
                        print("\n\nYou found the portal to the next chunk of space!!")
                        print("Sadly, the portal isn't active yet...\n")
                        self.foundDoor = True
                    ## checks if tile for an event
                    elif self.position == tile[1] and tile[0] != 0:
                        print("\n\nYou have encountered an event!!\n\n")
                        testing = events.Event(tile[2][0], tile[2][1])
                        testing.runEvent() ##and affect the ship here. 
                        print("\n")

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
            mapNew = initializeMap(random1, random2, 2)
            self.maps.append(mapNew)
            
    def play(self):
        mapCounter = 0
        while mapCounter < self.numMaps:
            runMap(self.maps[mapCounter])
            if self.maps[mapCounter].foundDoor:
                mapCounter += 1

def initializeMap (mapRows = 5, mapCols = 5, numTiles = 5):
    mapNew = Map(mapRows, mapCols, "^", 0, 0, " ")
    mapNew.populateTiles(numTiles)
    return mapNew
    

def runMap(mapObject, numMoves = 1):
    for i in range(numMoves):
        mapObject.displayMap()
        mapObject.movement()

def getRoomNumber():
    while True: 
        try:
            numRooms = int(input("How many rooms would you like to traverse?\n"))
            break
        except:
            print("That's not a number I can use!")
    return numRooms

        
def main():
    numRooms = getRoomNumber()

    dungeon = Dungeon(numRooms)
    dungeon.play()

        
main()
