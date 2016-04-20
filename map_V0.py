class Map(object):
    """Creates map object (length, height)"""
    def __init__(self, sizeY, sizeX):
        
        self.sizeX = sizeX
        self.sizeY = sizeY

        ## create empty list
        self.grid = []
        for x in range(self.sizeX): ##append empty list sizeX times to grid
            self.grid.append([])
        for x in self.grid: ## for each empty list
            for y in range(self.sizeY): ## for the num of times perscribed by sizeY
                x.append("_") ##add char sizeY times to the sub list within x

    def isValid(self, posY, posX):
        if posY < 0 or posX < 0:
            return False
        elif posY >= self.sizeY or posX >= self.sizeX:
            return False
        else:
            return True
    
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

    def changeTile (self, posY, posX, tile="t"):
        """Change specific tile (Y, X, tile) """
        if self.isValid(posY, posX):
            self.grid[posY][posX] = tile
        else:
            print("Not a valid position on the map")
    
            
def main():
    map1 = Map(10, 10)
    
    map1.populateTiles(5)
    map1.displayMap()

    print()

    inputX = int(input("Give me an x coordinate on the map to change\n"))
    inputY = int(input("Give me an y coordinate on the map to change\n"))

    map1.changeTile(inputY, inputX, "S")
    map1.displayMap()
    

main()
