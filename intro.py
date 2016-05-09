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

