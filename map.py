import ShipClass
import shelve
import text
import events

class Map(object):
    """Creates map object."""
    import events
    encounters = shelve.open("encounters.dat", "r")
    unusedEncounters = []
    usedEncounters = []
    foundEnding = False
    
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
                row.append(self.blankTile) ##add char numRow times to the sub list within row

        ## experiment
        for row in range(self.numRows): ## for each empty list
            for col in range(self.numCols): ## for the num of times perscribed by numRows
                self.grid[row][col] = " "

        self.grid[self.position[0]][self.position[1]] = self.charSym

    def displayMap(self):
        """Displays the map."""
        ## alternative method for displaying the map
        mapDisplay = ""
        mapDisplay += " "+"-" * 2 * self.numCols + "\n"
        for row in range (self.numRows):
            mapDisplay += "|"
            for col in range (self.numCols):
                mapDisplay += self.grid[row][col] + " "
            mapDisplay += "|\n"
        mapDisplay += " "+"-" * 2 * self.numCols

        print(mapDisplay)
        
    def setCharPosition(self, position = None):
        if position == None:
            position = self.position
        self.grid[position[0]][position[1]] = self.charSym

    def addBox(self, position = [1,1], length = 1):
        """Adds tiles to a set position."""
        for i in range(length):
            for k in range(length):
                if self.isValid(position):
                    self.grid[position[0]+i][position[1]+k] = "*" 
                    blockedPosition  = [position[0]+i,position[1]+k]
                    self.blockedTiles.append(blockedPosition)
            
           
    def updateUnusedEncounters(self):
        """Updates the unused encounters using the usedEncounters list."""
        Map.unusedEncounters = []
        for encounter in Map.encounters:
            if len(encounter) == 7:
                if int(encounter[5] + encounter[6]) not in Map.usedEncounters:
                    Map.unusedEncounters.append(int(encounter[5] + encounter[6]))
            elif len(encounter) == 6:
                if int(encounter[5]) not in Map.usedEncounters:
                    Map.unusedEncounters.append(int(encounter[5]))
        
    def populateTiles(self, numTiles):
        """Creates numbered tiles at random."""
        import random
        usedTileLocations = []
        tileChar = "O"
        self.updateUnusedEncounters()
        
        for tile in range(numTiles):
            
            randomCol = random.randrange(self.numCols)
            randomRow = random.randrange(self.numRows)

            ## checks to make sure we don't populate a tile containing our ship
            while [randomRow, randomCol] == self.position or [randomRow,randomCol] in usedTileLocations or [randomRow,randomCol] in self.blockedTiles:
                randomCol = random.randrange(self.numCols)
                randomRow = random.randrange(self.numRows)

            ## add to list of already used tile locations    
            usedTileLocations.append([randomRow,randomCol])

            if tile != 0:
                self.grid[randomRow][randomCol] = "?"
            else:
                self.grid[randomRow][randomCol] = "O"

            eventName = ""
            if tile != 0:
                
                eventNum = None

                ## if unusedEncounter is empty, this fills it back up
                ## should avoid any index errors with random.choice but
                ## the except covers any possible issues
                try:
                    if Map.unusedEncounters == []: 
                        Map.unusedEncounters = Map.usedEncounters[:] 
                        Map.usedEncounters = []
                        
                    eventNum = random.choice(Map.unusedEncounters)
                    
                except IndexError:
                    print("We just excepted an Index Error\n")

                
                Map.usedEncounters.append(eventNum)
                Map.unusedEncounters.remove(eventNum)    
                eventName = "event" + str(eventNum)

                ## Here for testing 
                ##print(Map.usedEncounters)
                ##print(Map.unusedEncounters)
            
            tileInfo = [tile, [randomRow, randomCol], eventName]
            self.tileList.append(tileInfo)

    def isValid(self, position):
        """Checks if a given position is valid."""
        if position[0] < 0 or position[1] < 0:
            ##print("\nYou've reached the edge of the map. You can go no farther.")
            return False
        elif position[0] >= self.numRows or position[1] >= self.numCols:
            ##print("\nYou've reached the edge of the map. You can go no farther.")
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
    
    def movement(self, ship):
        import events
        ## dictionary of move_ functions
        moves = {"w":self.move_up, "s":self.move_down, "a":self.move_left, "d":self.move_right, "i":ship.shipStatus}

        ## create list of dictionary keys for cleaner code when checking their validity
        movesList = []
        for move in moves:
            movesList.append(move)
            
        moveMenu = "\nChoose an action: \nw.Up\na.Left\ns.Down\nd.Right\ni.Display Ship Info\n"

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
        
                ## Tests for collisions
                for tile in self.tileList:
                    ## checks if tile is a door
                    if self.position == tile[1] and tile[0] == 0:
                        self.tileList.remove(tile)
                        print("\n\nYou found the portal to the next chunk of space!!")
                        self.foundDoor = True
                    ## checks if tile for an event
                    elif self.position == tile[1] and tile[0] != 0:
                        print("\n\nYou have encountered an event!!\n\n")
                        encounter = events.Event(tile[2])
                        encounter.runEvent() ##and affect the ship here.
                        if len(tile[2]) == 6:
                            ship.updateLog(int(tile[2][5]))
                        else:
                            ship.updateLog(int(tile[2][5] + tile[2][6]))
                        ship.updateResources(encounter.getResources())
                        self.tileList.remove(tile)
                        print("\n")

            else:
                self.position = originalPosition
                move = None
                print("\nSorry, you can't move there!\n")
            
            
        self.changeTile(self.position, self.charSym)
        if move != "i":
            ship.decrementFuel()
            ship.shipStatus(fuel = True, oxygen = False, biomass = False, hull = False)

    def save(self,ship):
        """Saves the current status of the log and ship."""
        import shelve

        while True:
            try:
                saveInput = input("Would you like to save? (y/n): \n")
                if saveInput.lower() == "y":
                    saveFile = shelve.open("saveFile.dat")
                    saveFile["ship"] = ship
                    saveFile["logEvents"] = ship.getLog()
                    saveFile.sync()
                    saveFile.close()
                    break
                else:
                    break
            except:
                print("Sorry that's not a valid input.\n")
                
class FinalMap (Map):
    endingFile = open("endings.txt","r")
    endings = endingFile.readlines()
    endingFile.close()
    
    def youMadeIt(self, ship):
        print("Great job. You and the " + ship.getName() + "\n")

    def populateTiles(self, ship):
        import random
        usedTileLocations = []
        
        randomCol = random.randrange(self.numCols)
        randomRow = random.randrange(self.numRows)

        while [randomRow, randomCol] == self.position or [randomRow,randomCol] in usedTileLocations or [randomRow,randomCol] in self.blockedTiles:
                randomCol = random.randrange(self.numCols)
                randomRow = random.randrange(self.numRows)

        self.grid[randomRow][randomCol] = "?"

        tileInfo = [1, [randomRow, randomCol]]
        self.tileList.append(tileInfo)
            
    def movement(self, ship):
        import events
        BAD_ENDING = 0
        NEUTRAL_ENDING = 2
        GOOD_ENDING = 4
        
        ## dictionary of move_ functions
        moves = {"w":self.move_up, "s":self.move_down, "a":self.move_left, "d":self.move_right, "i":ship.shipStatus}

        ## create list of dictionary keys for cleaner code when checking their validity
        movesList = []
        for move in moves:
            movesList.append(move)
            
        moveMenu = "\nChoose an action: \nw.Up\na.Left\ns.Down\nd.Right\ni.Display Ship Info\n"

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
        
                ## Tests for collisions
                for tile in self.tileList:
                    ## checks if tile is a door
                    if self.position == tile[1]:
                        self.tileList.remove(tile)
                        
                        if len(ship.getLog()) < 2:
                            events.printProperly(FinalMap.endings[BAD_ENDING])
                            FinalMap.foundEnding = True
                        elif len(ship.getLog()) >= 2 and (2 in ship.getLog() or 6 in ship.getLog()):
                            events.printProperly(FinalMap.endings[GOOD_ENDING])
                            FinalMap.foundEnding = True
                        else:
                            events.printProperly(FinalMap.endings[NEUTRAL_ENDING])
                            FinalMap.foundEnding = True
            else:
                self.position = originalPosition
                move = None
                print("\nSorry, you can't move there!\n")
            
        self.changeTile(self.position, self.charSym)
        if move != "i" and FinalMap.foundEnding == False:
            ship.decrementFuel()
            ship.shipStatus(fuel = True, oxygen = False, biomass = False, hull = False)
    
        
        

class Galaxy (object):
    """A Collection of Maps"""
    import ShipClass
    
    def __init__ (self, maps, ship):
        import random
        self.maps = []
        self.numMaps = maps - (int(len(ship.getLog()) / 2))
        self.minLength = 5
        self.maxLength = 14
        
        ## creates a series of maps and stores them in a list
        for i in range(self.numMaps):
            random1 = random.randint(self.minLength, self.maxLength)
            random2 = random.randint(self.minLength, self.maxLength)
            if i == self.numMaps - 1:
                mapNew = initializeFinalMap(ship,5, 5, 0)
            else:
                mapNew = initializeMap(random1, random2, 3)
                
            self.maps.append(mapNew)

    def notDeadYet(self, ship):
        if ship.getFuel() <= 0:
            return False
        elif ship.getBio() <= 0:
            return False
        elif ship.getOxygen() <= 0:
            return False
        elif ship.getHull() <= 0:
            return False
        else:
            return True
    
    def play(self, ship):
        """Standard play function for the game."""
        mapCounter = 0
        print("self.numMaps = " + str(self.numMaps))
        print("length of the log = " + str(len(ship.getLog())))
        ## allows you to iterate through the list of maps using foundDoor as a flag
        while mapCounter < self.numMaps and self.notDeadYet(ship) and not self.maps[mapCounter].foundEnding:
            runMap(self.maps[mapCounter], ship)
            if self.maps[mapCounter].foundDoor:
                mapCounter += 1
                events.printProperly("\nYou take some time to refine a little fuel (5 units worth) and stock up. Who knows what's ahead.")
                ship.increaseFuel(5)
                print("\n" + str(ship))
                self.maps[mapCounter].save(ship)
                input("Hit enter when you're ready to move on.")

        if self.notDeadYet(ship):
            print("\nYou've made it through the game! Thanks for playing!")
        elif not self.notDeadYet(ship):
            if ship.getFuel() <= 0:
                text.displayDeathOutro("fuel")
            elif ship.getBio() <= 0:
                text.displayDeathOutro("biomass")
            elif ship.getOxygen() <= 0:
                text.displayDeathOutro("oxygen")
            elif ship.getHull() <= 0:
                text.displayDeathOutro("hull")
    



def initializeMap (mapRows = 5, mapCols = 5, numTiles = 5):
    """Initializes a standard map"""
    import random
    mapNew = Map(mapRows, mapCols, ">", 0, 0, " ")
    for i in range(random.randint(0,int(mapRows * mapCols / 2))):
        randPosition = [random.randint(1,mapCols - 1), random.randint(1,mapRows - 1)]
        mapNew.addBox(randPosition)
    mapNew.populateTiles(numTiles)
    return mapNew

def initializeFinalMap (ship,mapRows = 5, mapCols = 5, numTiles = 5):
    """Initializes the final map"""
    import random
    mapNew = FinalMap(mapRows, mapCols, ">", 0, 0, " ")
    mapNew.populateTiles(ship)
    return mapNew

def runMap(mapObject, ship):
    """Couples together displaying and moving throughout the map"""
    mapObject.displayMap()
    mapObject.movement(ship)
    ##clrScreen()

def howMuchSpace():
    while True: 
        try:
            numRooms = int(input("How much space would you like to traverse?\n"))
            break
        except:
            print("That's not a number I can use!")
    return numRooms

def load():
    """Loads in the information from the save file."""
    ## opens the load file and updates the game's ship/Map with info from the file. 
    import shelve
    import time
    ship = None
    
    while True:
        try:
            loadInput = input("Would you like to load a past save file? (y/n): \n")
            if "y" in loadInput:
                print("\nLoading in your save file now...\n")
                time.sleep(1)
                loadFile = shelve.open("saveFile.dat", "r")
                
                print("Preparing your ship for space travel...\n")
                time.sleep(1)
                ship = loadFile["ship"]

                print("Loading in your ship's star log...\n")
                time.sleep(1)
                Map.usedEncounters = loadFile["logEvents"]
                
                loadFile.sync()
                loadFile.close()
                print("Load complete.")
                break
            elif "n" in loadInput:
                break
        except:
            print("Looks like you don't have a save file yet or we can't find it!\n")
            ship = None
            Map.usedEncounters = []
    print()
        
    return ship
        
def main():
    ##text.displayIntro()
    
    ship = load()
    if ship == None:
        ship = ShipClass.Ship(input("What would you like to name your ship:\n"))
    print(ship)
    
    numSpace = howMuchSpace()

    galaxy = Galaxy(numSpace, ship)
    galaxy.play(ship)

        
main()
