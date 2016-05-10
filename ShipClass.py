class Ship(object):
    """The general ship class that will be used throughout the game."""
    ## Define init
    def __init__(self, name = "Ship", biomass = 20, hull = 100, fuel = 70):
        self.__name = name
        self.__biomass = biomass
        self.__hull = hull
        self.__fuel = fuel
        self.__oxygen = 100
        self.__log = []
        
    ## Ship Getters
    def getName(self):
        return self.__name
    def getBio(self):
        return self.__biomass
    def getHull(self):
        return self.__hull
    def getFuel(self):
        return self.__fuel
    def getOxygen(self):
        return self.__oxygen

    ## Useful methods for changing the fuel
    def decrementFuel(self):
        self.__fuel -= 1
    def increaseFuel(self, newFuel):
        self.__fuel += newFuel

    def setHull(self, newHull):
        self.__hull = newHull

    def shipStatus(self, fuel = True, oxygen = True, biomass = True, hull = True):
        print()
        if oxygen == False and biomass == False:
            print("Fuel: \t" + str(self.getFuel()))
        elif fuel == True:
            print("Fuel: \t\t" + str(self.getFuel()))
        if oxygen == True:
            print("Oxygen: \t" + str(self.getOxygen()))
        if biomass == True:
            print("Biomass: \t" + str(self.getBio()))
        if hull == True:
            print("Hull: \t\t" + str(self.getHull()))
        
    def updateResources (self, resourceChanges):
        ## for reference: resourceChanges = ['fuel', 'oxygen', 'biomass', 'hull integrity']
        ## creates constants for more clear access
        FUEL = 0
        OXYGEN = 1
        BIOMASS = 2
        HULL = 3
        
        self.__fuel += resourceChanges[FUEL]
        self.__oxygen += resourceChanges[OXYGEN]
        self.__biomass += resourceChanges[BIOMASS]
        self.__hull += resourceChanges[HULL]

    ## Ship tostring
    def __str__(self):
        r = ""
        r += "Name: \t\t" + self.getName() + "\n"
        r += "Fuel: \t\t" + str(self.getFuel()) + "\n"
        r += "Oxygen: \t" + str(self.getOxygen()) + "\n"
        r += "Biomass: \t" + str(self.getBio()) + "\n"
        r += "Hull: \t\t" + str(self.getHull()) + "\n"
        
        return r
        
    ## Update Log
    def updateLog(self, eventNum):
        self.__log.append(eventNum)

    def getLog(self):
        return self.__log
