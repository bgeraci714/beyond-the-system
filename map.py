class Map(object):
    """Creates map object (length, height)"""
    def __init__(self, sizeY, sizeX, charSym = "S", startPosY = 9, startPosX = 5):
        
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.charSym = charSym
        self.position = [startPosY,startPosX]

        ## create empty list
        self.grid = []
        for x in range(self.sizeX): ##append empty list sizeX times to grid
            self.grid.append([])
        for x in self.grid: ## for each empty list
            for y in range(self.sizeY): ## for the num of times perscribed by sizeY
                x.append("_") ##add char sizeY times to the sub list within x
                
    def charPosition(self, position = None):
        if position == None:
            position = self.position
        self.grid[position[0]][position[1]] = self.charSym
    
    def displayMap(self):
        for x in range (self.sizeX):
            for y in range (self.sizeY):
                print(self.grid[x][y], end=" ")
            print()
            
    def populateTiles(self, numTiles):
        """Creates numbered tiles at random."""
        import random
        
        for tile in range(numTiles):
            randomX = random.randrange(self.sizeX)
            randomY = random.randrange(self.sizeY)
            self.grid[randomX][randomY] = str(tile)

    def isValid(self, position):
        if position[0] < 0 or position[1] < 0:
            return False
        elif position[0] >= self.sizeY or position[1] >= self.sizeX:
            return False
        else:
            return True

    def changeTile(self, position, tile="t"):
        """Change specific tile (position[Y,X], tile character) """
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
        moves = {"1":self.move_up, "2":self.move_down, "3":self.move_left, "4":self.move_right}

        ## create list of dictionary keys for cleaner code when checking their validity
        movesList = []
        for move in moves:
            movesList.append(move)
            
        moveMenu = "\nChoose a movement: \n1.Up\n2.Down\n3.Left\n4.Right\n"

        ## clears out original tile and replaces it with a blank
        self.changeTile(self.position, "_")

        validMove = False 
        move = None

        while not validMove:
            ## might move this outside of movement method to provide ways of ending movement/more options
            while move not in movesList:
                move = str(input(moveMenu))
            ## Uses functions stored in dictionary.
            moves[move]()
            if self.isValid(self.position):
                validMove = True
            else:
                ## undo invalid move
                if move == "1":
                    moves["2"]()
                elif move == "2":
                    moves["1"]()
                elif move == "3":
                    moves["4"]()
                elif move == "4":
                    moves["3"]()
                else:
                    print("An error occurred\ns")
                ## return move back to None type
                move = None
        self.changeTile(self.position, self.charSym)
       
            
def main():
    map1 = Map(10, 10, "^")
    map1.charPosition()
    map1.populateTiles(5)
    map1.displayMap()

    print()

    ## tester program with inputting a specific tile in at a specific spot and for the movement. 
    map1.changeTile([2,2], "t")
    for i in range(10):
        map1.movement()
        map1.displayMap()
    

main()
