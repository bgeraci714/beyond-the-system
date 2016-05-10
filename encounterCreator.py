## Beyond the System
## A game by Blake Geraci and Ashley Hartzler
##
## Program to create the Encounters for the final project

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def main():

    eventNum = int(input("What's the first unused event number (event#.txt) That you want to start with: \n"))
    stillGivingInput = True
    

    while stillGivingInput:

        
        curEventName = "event" + str(eventNum) + ".txt"
        curBlurbFile = open_file(curEventName, "w")

        curEventChoices = "event" + str(eventNum) + "_c.txt"
        curChoiceFile = open_file(curEventChoices, "w")


            ## get the description
        curBlurbFile.write(input("Give me a situation for the ship to encounter: \n") + "\n")

        numOptions = int(input("How many choices would you like available?: \n"))

        for i in range(numOptions):
            ## get the first choice for a response
            curChoiceFile.write(input("Give me your action! Try to hit space around 10-12 words: \n") + "\n")

            ## get 4 value mods
            for i in range(4):
                if i == 0:
                    curChoiceFile.write(input("What's choice's affect on fuel?: ") + "\n")
                elif i == 1:
                    curChoiceFile.write(input("What's choice's affect on oxygen?: ") + "\n")
                elif i == 2:
                    curChoiceFile.write(input("What's choice's affect on biomass?: ") + "\n")
                elif i == 3:
                    curChoiceFile.write(input("What's choice's affect on the hull's integrity?: ") + "\n")

            ## get the resolution to that choice
            curChoiceFile.write(input("What's the resolution to this choice?: \n") + "\n")
            print("\n On to the next option!! \n")
            
        curBlurbFile.close()
        curChoiceFile.close()
        

        ## see if the user wants to continue asking questions
        continueChoice = input("Would you like to supply another encounter? (y/n): ").lower()
        while continueChoice not in ('y','n'):
            print("Sorry, your choice was invalid. Try again.")
            continueChoice = input("Would you like to supply another question? (y/n): ").lower()

        if continueChoice == 'n':
            stillGivingInput = False

        ##increment the event counter. 
        eventNum += 1

main()
