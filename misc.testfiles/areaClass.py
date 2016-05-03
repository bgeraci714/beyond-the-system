##Eric Teall

## Create a simple adventure game using objects, where a player can
## travel between various connected locations

class Area(object):
    
    def __init__(self, combat):

        self.__combat__ = combat
        self.__generateDescrip__()
        #self.__generateExit__()

    def checkCombat(self):

        if self.__combat__ == True:
            self.__combatDescrip__ = "Occupying " + self.__name__ + " are " + str(self.__enemNum__ ) + ' ' + self.__enemType__ + '. They look up at you, and attack.'
            return True

        else:

            self.__enemNum__ = 0
            self.__enemType__ = "None"
            self.__combatDescrip__ = "There is nothing of interest here."
            
            return False

    def __generateDescrip__(self):

        import random
        
        adject1 = ['dank', 'dark', 'desolate', 'blasted', 'hot', 'silent', 'freezing', 'ruined', 'moldy']
        adject2 = ['church', 'swamp', 'dungeon', 'street', 'woods', 'graveyard', 'temple']
        adject3 = ['William\'s', 'Echo', 'Murmur', 'Oopsville', 'The Royal', 'Beggar\'s', 'Slipskin', 'Adjunct\s', 'Earlking', 'Terresque', 'Lich Lord\'s'] 
        
        randAdj1 = random.choice(adject1)
        randAdj2 = random.choice(adject2)
        randAdj3 = random.choice(adject3)

        self.__name__ = randAdj3 + ' ' + randAdj2.title()

        descrip1 = self.__name__ + ' is a ' + randAdj1 + 'place.'
        descrip2 = 'You enter a ' + randAdj1 + ' place. ' + self.__name__ + ' is written on a sign posted into the ground.'
        descrip3 = 'After some time, you emerge into ' + self.__name__ + '. There is a rustle in the ' + randAdj1 + ' space.'

        descripList = [descrip1, descrip2, descrip3]
        
        self.__descrip__ = random.choice(descripList)

        if self.__combat__ == True:
            
            enemList = ['skeletons', 'demons', 'feral hounds', 'gargoyles', 'goblins', 'cultists']
            enemAdj = ['bloody', 'enraged', 'rampaging', 'skulking', 'terrifying', 'hipster']

            self.__enemNum__ = random.randrange(2,10)
            self.__enemType__ = random.choice(enemAdj) + ' ' + random.choice(enemList)

            self.__combatDescrip__ = "Occupying " + self.__name__ + " are " + str(self.__enemNum__ ) + ' ' + self.__enemType__ + '. They look up at you, and attack.'

        else:

            self.__enemNum__ = 0
            self.__enemType__ = "None"
            self.__combatDescrip__ = "There is nothing of interest here."

    def enemType(self):

        return self.__enemType__

    def enemNum(self):

        return self.__enemNum__

    def getName(self):

        return self.__name__

    def setCombat(self, someBool = False):

        self.__combat__ = someBool
        self.checkCombat()

    def areaDescrip(self):

        return self.__descrip__ + '\n' + self.__combatDescrip__

    
        

        
            

            
        
