class Map(object):
    """Creates map object (length, height)"""
    def __init__(self, sizeY, sizeX, charSym = "S", startPosY = 0, startPosX = 0):
        
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.charSym = charSym
        self.position = [startPosY,startPosX]
        self.charY = startPosY
        self.charX = startPosX

        ## create empty list
        self.grid = []
        for x in range(self.sizeX): ##append empty list sizeX times to grid
            self.grid.append([])
        for x in self.grid: ## for each empty list
            for y in range(self.sizeY): ## for the num of times perscribed by sizeY
                x.append("_") ##add char sizeY times to the sub list within x
    
    def displayMap(self):
        for x in range (self.sizeX):
            for y in range (self.sizeY):
                print(self.grid[x][y], end=" ")
            print()
            
    def populateTiles(self, numTiles):
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
        """Change specific tile (Y, X, tile) """
        if self.isValid(position):
            self.grid[position[0]][position[1]] = tile
        else:
            print("Not a valid position on the map")
            
    

    ## move functions
    def move_up(self):
        self.position[0] -= 1
        #return self.position

    def move_down(self):
        self.position[0] += 1
        #return self.position

    def move_left(self):
        self.position[1] -= 1
        #return self.position

    def move_right(self):
        self.position[1] += 1
        #return self.position

    def movement(self):
        ##{"1":"Up", "2":"Right","3":"Left","4":"Down"}
        moves = {}
        moves = {"1":self.move_up(), "2":self.move_right(), "3":self.move_left(), "4":self.move_down()}
        movesList = []
        for move in moves:
            movesList.append(move)

        print(moves["5"])
        tempMoveMenu = "Choose a movement: \n\t1.Up\n\t2.Right\n\t3.Left\n\t4.Down\n"

        validMove = False 

        move = None
        while not validMove: 
            while move not in movesList:
                move = input(tempMoveMenu)
            moves[move]
            print(self.position)
            print(moves)
            if self.isValid(self.position):
                validMove = True

        self.changeTile(self.position, self.charSym)
       
            
def main():
    map1 = Map(10, 10)
    
    map1.populateTiles(5)
    #map1.displayMap()

    print()

    '''
    inputYX = [0,0]
    inputYX[1] = int(input("Give me an x coordinate on the map to change\n"))
    inputYX[0] = int(input("Give me an y coordinate on the map to change\n"))
    '''
    map1.changeTile([0,0], "S")
    map1.movement()
    
    map1.displayMap()
    

main()
