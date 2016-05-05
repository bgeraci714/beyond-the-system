import shelve

def importFile (fileName):
    fileNameT = fileName + ".txt"
    fileNameC = fileName + "_c.txt"

    ## import the description file
    file = open(fileNameT, "r")
    blurbText = []
    blurbText = file.readlines()
    file.close()

    file = open(fileNameC, "r")
    choiceText = []
    choiceText = file.readlines()
    file.close()

    if len(choiceText) % 6 == 0:
        numOptions = len(choiceText) / 6
    elif len(choiceText) % 7 == 0:
        numOptions = len(choiceText) / 7
    
    encounter = []
    encounter.append(numOptions)
    encounter.append(blurbText)
    encounter.append(choiceText)

    return encounter

shelf = shelve.open("encounters.dat")

for i in range(1,20):
    try:
        eventName = "event" + str(i)
        event = importFile(eventName)
        shelf[eventName] = event
        shelf.sync()
    except:
        break

for i in range(1,20):
    try:
        eventName = "event" + str(i)
        print(shelf[eventName])
    except:
        break
    
shelf.close()
