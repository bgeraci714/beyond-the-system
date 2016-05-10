## File that handles reading in events and printing them properly.

import shelve
import shelveMaker
        
class Event (object):
    
    ## Default number of available choices for every event is four.
    ## out of program, this class will read two files, one will be the event#.txt
    ## this will hold the story information

    ## the second filetype should be named event#_c.txt
    ## veiw the readme.txt for full instructions on formatting.

    def __init__ (self, name):
        encountersFile = shelve.open("encounters.dat", "r")
        self.__name__ = name
        self.__options__= encountersFile[name][0]
        self.__blurb__ = encountersFile[name][1]
        
        self.__fuel__ = 0
        self.__oxy__ = 0
        self.__bio__ = 0
        self.__hull__ = 0

        self.__optionList__ = []

        for i in range(self.__options__):
            LINES_PER_CHOICE = 6
            
            ## Breaks each block into usuable parts
            availAction = encountersFile[name][2][0 + (i * LINES_PER_CHOICE)]
            fuelDIF = int(encountersFile[name][2][1 + (i * LINES_PER_CHOICE)])
            oxyDIF = int(encountersFile[name][2][2 + (i * LINES_PER_CHOICE)])
            bioDIF = int(encountersFile[name][2][3 + (i * LINES_PER_CHOICE)])
            hullDIF = int(encountersFile[name][2][4 + (i * LINES_PER_CHOICE)])
            resolution = encountersFile[name][2][5 + (i * LINES_PER_CHOICE)]

            ## Store usuable parts in a list

            curOption = [availAction, fuelDIF, oxyDIF, bioDIF, hullDIF, resolution]           

            ## Adds this list to the full list of options

            self.__optionList__.append(curOption)

    def runEvent(self):
        import time

        printProperly(self.__blurb__)
           
        ## offset for the selection so it will continue until selection is less
        ## than the number of options available (2 options, 0 or 1 are choices)
        select = self.__options__ +1


        while select > (self.__options__):

            print(" ")
            printProperly("Captain, these are your options: ")
            print(" ")
            
            for x in range(self.__options__):
                
                linePos = 0

                ## Read the first option of every list
                
                print( str(x) + ") ", end = "")
                ## [x][0] represents the description of the choice
                printProperly(self.__optionList__[x][0])

            try:
                ## gets the input to be checked against self.__option__ + 1
                tempSelect = int(input(''))
                select = tempSelect
                
            except ValueError:

                print("ERROR")

        results = self.__optionList__[select]

        ## Reads the resolving action of the selection, then removes it.
        
        print(' ')
        resultsPopped = results.pop()
        printProperly(str(resultsPopped))
        #print(str(results.pop()))

        ## Now, we no longer need the first section of the list
        ## Remove it and we have a nice neat list of numbers.

        results.pop(0)

        self.resourceUpdate(results)

        input("\nPress enter to continue on.")

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
            printProperly(self.checkChange(resourceList[i],resourceIndex[i]))

    def getResources(self):
        return self.__resourceList__

def printProperly(text, printSpeed = 0.0,end = "\n"):
    """Prints 66 characters then starts looking to make a new line."""
    
    import time
    linePos = 0
    for letter in text:
        if letter == "$":
            print("\n")
            linePos = 0
        else:
            print(letter, end="")
            time.sleep(printSpeed)
            linePos += 1
        
        ## probably had a long, don't want weird spacing if we did!
        if linePos >= 77:
            linePos = 0
        ## creates a new line once we hit a space after char position 67
        elif linePos > 67 and letter == " ":
            print()
            linePos = 0
            
    print(str(end), end="")
