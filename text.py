## Beyond the System
## A game by Blake Geraci and Ashley Hartzler
##
## Program for handling the many non-event text files/functions used in the game. 

import events

def displayIntro(pS = .2):
    import time
    introFile = open("GameIntro.txt","r")

    lines = introFile.readlines()
    printingLogo = True
    printSpeed = pS 

    for line in lines:
        if "+" in line and printingLogo == True:
            input("Press enter to continue.\n")
            printingLogo = False
        if printingLogo == True:
            print(line, end="")
            time.sleep(printSpeed)
        else:
            events.printProperly(line)
            #time.sleep(printSpeed)

    input("\nPress Enter to continue on...\n")

def displayStory():
    import time
    storyFile = open("StoryIntro.txt","r")

    lines = storyFile.readlines()
    printingTransmission = False
    printSpeed = .2 

    storyInput = input("Would you like to see the story? (y/n): \n")
    while "y" not in storyInput or "n" not in storyInput: 
        if "y" in storyInput:
            for line in lines:
                events.printProperly(line, end = "")
            input("\nPress Enter to continue on...\n")
            break
        elif "n" in storyInput:
            break
        else:
            print("Sorry, that's not a valid input.")
            storyInput = input("Would you like to see the story? (y/n): \n")

    ## The transmission used is a poem created by Carol Weston
    ## It is called "Outer Space" and can be found here:
    ## http://teachers.net/lessonplans/posts/1644.html

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


