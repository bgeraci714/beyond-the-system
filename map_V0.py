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
        self.grid[posY][posX] = tile
    
            
def main():
    map1 = Map(10, 10)
    
    map1.populateTiles(5)
    map1.displayMap()

    print()

    map1.changeTile(0, 3, "E")
    map1.displayMap()
    

main()
