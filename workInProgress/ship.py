#Ship Class

class Ship(object):
    #Define init
    def __init__(self, name, biomass, HP, fuel, log, inventory):
        self.__name = name
        self.__biomass = biomass
        self.__HP = HP
        self.__fuel = fuel
        self.__log = []
        self.__inventory = []

    #Ship Getters
    def getname(self):
        return self.__name
    def getbio(self):
        return self.__biomass
    def getHP(self):
        return self.__HP
    def getfuel(self):
        return self.__fuel

    #Ship Setters
    def setname(self, newname):
        self.__name = newname
    def setbio(self, newbio):
        self.__biomass = newbio
    def setHP(self, newHP):
        self.__HP = newHP
    def setfuel(self, newfuel):
        self.__fuel = newfuel

    #Ship tostring
    def __str__(self):
        r = ""
        r += "Name: " + self.getname() + "\n"
        r += "Biomass: " + str(self.getbio()) + "\n"
        r += "HP: " + str(self.getHP()) + "\n"
        r += "Fuel: " + str(self.getfuel())
        return r
        
    #Update Log
    def updatelog(self, eventdeetz):
        self.__log.append(eventdeetz)
