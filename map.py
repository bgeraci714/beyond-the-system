class Map(object):
    """Creates map object (rows, cols, charSymbol, starting row, starting column)"""
    tileList = []

    def __init__(self, numRows, numCols, charSym = "S", startRow = 9, startCol = 5, blankTile = "_"):
        self.numCols = numCols
        self.numRows = numRows
        self.charSym = charSym
        self.position = [startRow,startCol]
        self.blankTile = blankTile

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
        
    def setCharPosition(self, position = None):
        if position == None:
            position = self.position
        self.grid[position[0]][position[1]] = self.charSym
    
    def displayMap(self):
        print (" "+"W" * 2 * self.numCols)
        for row in range (self.numRows):
            print("|", end="")
            for col in range (self.numCols):
                print(self.grid[row][col], end=" ")
            print("|")
        print (" "+"W" * 2 * self.numCols)           
    def populateTiles(self, numTiles):
        """Creates numbered tiles at random."""
        import random
        usedTileLocations = []
        
        for tile in range(numTiles):
            
            randomCol = random.randrange(self.numCols)
            randomRow = random.randrange(self.numRows)

            ## checks to make sure we don't populate a tile containing our ship
            while [randomRow, randomCol] == self.position or [randomRow,randomCol] in usedTileLocations:
                randomCol = random.randrange(self.numCols)
                randomRow = random.randrange(self.numRows)

            ## add to list of already used tile locations    
            usedTileLocations.append([randomRow,randomCol])
            
            self.grid[randomRow][randomCol] = str(tile)
            
            tileInfo = [tile, [randomRow, randomCol]]
            Map.tileList.append(tileInfo)

    def isValid(self, position):
        if position[0] < 0 or position[1] < 0:
            return False
        elif position[0] >= self.numRows or position[1] >= self.numCols:
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
                for tile in Map.tileList:
                    if self.position == tile[1]:
                        Map.tileList.pop(Map.tileList.index(tile))
                        ## testing to see if we can interact with the tile list as intended
                        print("You hit tile number " + str(tile[0]) + "!")
            elif not self.isValid(self.position):
                print(originalPosition)
                self.position = originalPosition
                move = None
            else:
                printf("An error occurred!")
            
        self.changeTile(self.position, self.charSym)
       
            
def main():
    map1 = Map(10,10, "^", 5, 5, ".")
    map1.setCharPosition()
    map1.populateTiles(5)
    map1.displayMap()
    #print(Map.tileList)

    print()

    ## tester program with inputting a specific tile in at a specific spot and for the movement. 
    
    ## map1.changeTile([2,3], "T")
    for i in range(10):
        map1.movement()
        map1.displayMap()
        
    

main()
