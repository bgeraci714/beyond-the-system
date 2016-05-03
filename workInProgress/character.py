def characterBuilder():

    lowMod = 0.5
    medMod = 1.0 
    highMod = 2.5
    
    player = {}
    player["name"] = "NONE"
    player["ship name"] = "NONE"
    player["class"] = "NONE"
    player["inv"] = []
    player["name"] = input("Enter your character name: ")
    player["ship name"] = input("Enter your character gender: ")
    
    classMenu = '''
    ***************************
    a) Puddle Jumper     - high agility, low health
    b) Star Cruiser      - high health, low agility
    c) Dreadknot         - low everything....
    d) Salvage Vessel    - high attack, low agility
    ***************************
    SELECT YOUR CLASS: (A,B,C,D):
    '''
    selection = input(classMenu).lower()
    while(selection not in ("a","b","c","d")):
        selection = input(classMenu).lower()

    if(selection == "a"):
        player["class"] = "Puddle Jumper"
        player["biomass"] *= medMod
        player["fuel"] *= highMod
        player["HP"] *= lowMod
        player["inv"].append("other")
        player["inv"].append("other")
    elif(selection == "b"):
        player["class"] = "Star Cruiser"
        player["biomass"] *= medMod
        player["fuel"] *= lowMod
        player["HP"] *= highMod
        player["inv"].append("other")
        player["inv"].append("other")
    elif(selection == "c"):
        player["class"] = "Frater"
        player["biomass"] *= lowMod
        player["fuel"] *= lowMod
        player["HP"] *= lowMod
        player["inv"].append("other")
        player["inv"].append("other")
    elif(selection == "d"):
        player["class"] = "Friget"
        player["biomass"] *= highMod
        player["fuel"] *= lowMod
        player["HP"] *= medMod
        player["inv"].append("other")   
        player["inv"].append("other")
    else:
        print("something went wrong.")

    print("Welcome, " + player.get("name") + " the " + player.get("gender") + " " + player.get("class"))
    print("Your stats:\nAttack: "+str(player.get("atk"))+"\nAgility: "+str(player.get("agi"))+"\nHP: "+str(player.get("hp")))
    return player
