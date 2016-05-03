class Ship(object):
    """The general ship class that will be used throughout the game."""
    ## Define init
    def __init__(self, name = "Ship", biomass = 10, hull = 100, fuel = 30):
        self.__name = name
        self.__biomass = biomass
        self.__hull = hull
        self.__fuel = fuel
        self.__oxygen = 100
        self.__log = []
        self.__inventory = []

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

    ## Ship Setters
    def setname(self, newname):
        self.__name = newname
    def setbio(self, newbio):
        self.__biomass = newbio
    def setHull(self, newHull):
        self.__hull = newHull
    def setfuel(self, newfuel):
        self.__fuel = newfuel

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
    def updatelog(self, eventdeetz):
        self.__log.append(eventdeetz)

##ship = Ship("Gurren Lagann")
##print(ship)
##resourceChanges = [1, -2, 0, 10]
##ship.updateResources(resourceChanges)

##print(ship)
