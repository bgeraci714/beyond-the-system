## Events

class Event (object):

    ## To create an event, simply supply it with a name.
    ## Default number of available choices for every event is four.

    ## out of program, this class will read two files, one will be the event.txt
    ## this will hold the story information

    ## the second filetype should be named event_c.txt
    ## veiw the readme.txt for full instructions on formatting.

    def __init__ (self, name, numChoices = 4):

        self.__name__ = name
        self.__options__= numChoices
        self.__fileHandle__()

        ## These won't get values untill the event is run
        ## It's good to set them up here to avoid errors in
        ## getters and setters
        
        self.__fuel__ = 0
        self.__oxy__ = 0
        self.__bio__ = 0
        self.__hull__ = 0


    def __fileHandle__(self):

        filename = self.__name__ + ".txt"

        c_file = self.__name__ + "_c.txt"

        try:
            
            logFile = open(filename, "r")
            
            self.__blurb__ = logFile.readlines()

            logFile.close()

        except IOError:
            print("File Not Found")


        try:
            choiceFile = open(c_file, "r")

            ##Create a dynamic list to store results of every action.

            self.__optionList__ = []

            for i in range(self.__options__):
                ## Break each block into usuable parts
                ## not using readlines because I need to convert to int

                availAction = choiceFile.readline()
                fuelDIF = int(choiceFile.readline())
                oxyDIF = int(choiceFile.readline())
                bioDIF = int(choiceFile.readline())
                hullDIF = int(choiceFile.readline())
                resolution = choiceFile.readline()

                ##Store usuable parts in a list

                curOption = [availAction, fuelDIF, oxyDIF, bioDIF, hullDIF, resolution]           

                ##adds this list to the full list of options

                self.__optionList__.append(curOption)

            choiceFile.close()

        except IOError:
            print("File Not Found")

    def runEvent(self):
        import time
         
        for i in  range(len(self.__blurb__)):
            for letter in self.__blurb__[i]:
                print(letter, end="")
                time.sleep(.01)
        print()
        
        select = self.__options__ +1


        while select > (self.__options__):

            print(" ")
            print("Captain, these are your options: ")
            print(" ")
            
            for x in range(self.__options__):


                ## Read the first option of every list
                
                print( x, ")", end = "")
                for letter in self.__optionList__[x][0]:
                    print(str(letter), end="")
                    time.sleep(.01)
                print() 


            try:
                
                tempSelect = int(input(''))
                select = tempSelect
                
            except ValueError:

                print("ERROR")

        results = self.__optionList__[select]

        ## Reads the resolving action of the selection, then removes it.
        
        print(' ')
        print(str(results.pop()))

        ## Now, we no longer need the first section of the list
        ## Remove it and we have a nice neat list of numbers.

        results.pop(0)

        self.resourceUpdate(results)

    def checkChange(self, someInt, someString):

        if someInt > 0:
            passString = "The ship has gained " + str(someInt) + ' ' + someString + '.'

        elif someInt < 0:

            ## convert someInt to a positive for grammar
            
            passString = "The ship has lost " + str(abs(someInt)) + ' ' + someString + '.'

        else:

            passString = "Levels of " + someString + " remain stable."


        return passString

    def resourceUpdate(self, resourceList):

        
        ## Remember, the order of the list is:
        
        resourceIndex = ['fuel', 'oxygen', 'biomass', 'hull integrity']

        self.__resourceList__ = resourceList

        for i in range(len(resourceList)):

            print(self.checkChange(resourceList[i],resourceIndex[i]))

    def getResources(self):
        return self.__resourceList__


## These lines were for testing
##example = Event('example', 2)
##example.runEvent()
##resources = example.getResources()
##print(resources)

        
    
