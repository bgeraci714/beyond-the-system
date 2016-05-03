#importing files

import map1, character, ship, event

def main():

    characterBuilder()#make the character
    #ship(s)
    ship1 = Ship("Puddle Jumper", "biomass", 45, "log", "inventory")
    ship2 = Ship("Ship 2", "biomass", 45, "log", "inventory")
    ship3 = Ship("Ship 3", "biomass", 45, "log", "inventory")
    ship4 = Ship("Ship 4", "biomass", 45, "log", "inventory")
    

#main functiondef main():
    map1 = Map(5,5, "^", 0, 0, " ")
    map1.setCharPosition()
    map1.populateTiles(5)
    map1.displayMap()
    #print(Map.tileList)

    print()

    ## tester program with inputting a specific tile in at a specific spot and for the movement. 
    
    ## map1.changeTile([2,3], "T")
    for i in range(100):
        map1.movement()
        map1.displayMap()
    if mapTile == "T":#run event
        #event = Event("name", "numChoice")
        #Event()?
    elif:
        mapTile == #invalid tile/calision
        print("You have crashed.")
        #fuel goes down
        #if crash = true
        ship1.append("", "", 44, "", "")
        #elif other ships...
        #else fuel is found
        ship1.append("", "", 45, "", "")
    else:
        print("Choose your next destination")
        ship.append#fuel goes down

    #End Game
    #if player reaches endTile:
        #print("Congrats you won")

        #elif fuel == 0:
            #print("Game over")
        #elif biomass == 0:
            #print("Game over")
        
            

main()
