## Creates the .dat.db file that we need for the 

import shelve

def importFile (fileName):
    ## changes file names to the correct ones for each file
    fileNameT = "encounters\\" + fileName + ".txt"
    fileNameC = "encounters\\" + fileName + "_c.txt"

    ## import the description file
    file = open(fileNameT, "r")
    blurbText = []
    blurbText = file.readline()
    file.close()

    ## imports the choice file
    file = open(fileNameC, "r")
    choiceText = []
    choiceText = file.readlines()
    file.close()

    ## meant for something later, if we decide to add a link
    ## to another event, 7 will let us do so. 
    if len(choiceText) % 6 == 0:
        numOptions = len(choiceText) / 6
    elif len(choiceText) % 7 == 0:
        numOptions = len(choiceText) / 7

    ## creates the encounter list 
    encounter = []
    encounter.append(int(numOptions))
    encounter.append(blurbText)
    encounter.append(choiceText)

    return encounter

def main():
    shelf = shelve.open("encounters.dat")

    for i in range(1,100):
        try:
            ## creates an iterable shelf object that we can access later
            if i < 10:
                eventName = "event" + str(i)
            else:
                eventName = "event" + str(i)
            event = importFile(eventName)
            shelf[eventName] = event
            shelf.sync()
        except:
            break

    ## if this doesn't work properly or an event has improper spacing,
    ## 0.0 will show up, showing you which one you need to fix.

    print(len(shelf))
    shelf.close()


main()
