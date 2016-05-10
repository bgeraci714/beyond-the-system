import events

def displayIntro(pS = .2):
    import time
    introFile = open("GameIntro.txt","r")

    lines = introFile.readlines()
    printingLogo = True
    printSpeed = pS 

    for line in lines:
        if "+" in line and printingLogo == True:
            input()
            printingLogo = False
        if printingLogo == True:
            print(line, end="")
            time.sleep(printSpeed)
        else:
            print(line)
            time.sleep(printSpeed)

    input("Press Enter to continue on...\n")

def displayDeathOutro(causeOfDeath):
    FUEL = 0
    OXYGEN = 2
    BIOMASS = 4
    HULL = 6
    
    deathFile = open("DeathOutros.txt","r")
    outros = deathFile.readlines()
    if "fuel" == causeOfDeath:
        events.printProperly(outros[FUEL])
    elif "oxygen" == causeOfDeath:
        events.printProperly(outros[OXYGEN])
    elif "biomass" == causeOfDeath:
        events.printProperly(outros[BIOMASS])
    elif "hull" == causeOfDeath:
        events.printProperly(outros[HULL])
    else:
        print("An error occurred!")


