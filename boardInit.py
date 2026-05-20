def boardInit():
    
    validShip = 0
    validPos = False
    validDir = False
    validLetters = {
        "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9
        }
    validNum = {
        "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9
    }
    boatName = {
        0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
    }
    
    #like, i know i used this in other places and i could import it, but this is more self contained also im lazy
    boatPoints = []
    boatMap = ''
    #where there the boats are, it will get turned into a string but for the time being
    lengths = [5, 4, 3, 3, 2]
    compass = {
        "n":"North", "s":"South", "e":"East", "w":"West"
    }
    #probably an easier way but whatever
    
    while validShip < 5:

        while not validPos:
            #do not progress until the positon has been validated
            #A-J is the Y axis, 0-9 is the X axis
            bow = input("Input the bow of your " + boatName.get(validShip) + ": ") #if i move to a visual approach I will use a click system which will not require this code, but for the MVP this will have to do
            if len(bow) != 2:
            #check the move is in a valid form to prevent trying to index a part of the string that doesnt exist
            #also prevents like A33 or whatever
                print("Please type moves in Letter Number from A-J, 0-9 (ex. B0, J6)")
            elif (validLetters.get(bow[0].lower()) != None) and (validNum.get(bow[1]) != None):
            #make sure each letter is right
                validPos = True
            else:
                print("Please type moves in Letter Number from A-J, 0-9 (ex. B0, J6)")

        while not validDir:
            text = str(boatName.get(validShip))
            #idk why it got mad at me for this
            direction = input("Pick the direction you want the " + text + " to face (N, S, E, W): ").strip().lower()
            match(direction):
                case "n": #up
                    if validLetters.get(bow[0].lower()) >= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(validLetters.get(bow[0].lower()) - i) + str(validNum.get(bow[1]))) in boatPoints:
                                print("Boat overlap detected, please pick a new spot")
                                validPos = False
                                validDir = True
                                validShip -= 1
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        print(boatName.get(validShip) +" outside of game board.")
                        validPos = False
                        validDir = False
                        validShip -= 1
                        break

                    if validPos == True:
                        validDir = True
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(validLetters.get(bow[0].lower()) - i) + str(validNum.get(bow[1]))))
                case "s": #down
                    if validLetters.get(bow[0].lower()) <= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(validLetters.get(bow[0].lower()) + i) + str(validNum.get(bow[1]))) in boatPoints:
                                print("Boat overlap detected, please pick a new spot")
                                validPos = False
                                validDir = True
                                validShip -= 1
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        print(boatName.get(validShip) +" outside of game board.")
                        validPos = False
                        validDir = False
                        validShip -= 1
                        break

                    if validPos == True:
                        validDir = True
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(validLetters.get(bow[0].lower()) + i) + str(validNum.get(bow[1]))))
                case "e": #right
                    if validNum.get(bow[1]) <= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(validLetters.get(bow[0].lower())) + str(validNum.get(bow[1]) + i)) in boatPoints:
                                print("Boat overlap detected, please pick a new spot")
                                validPos = False
                                validDir = True
                                validShip -= 1
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        print(boatName.get(validShip) +" outside of game board.")
                        validPos = False
                        validDir = False
                        validShip -= 1
                        break

                    if validPos == True:
                        validDir = True
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(validLetters.get(bow[0].lower())) + str(validNum.get(bow[1]) + i)))
                case "w": #left
                    if validNum.get(bow[1]) >= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(validLetters.get(bow[0].lower())) + str(validNum.get(bow[1]) - i)) in boatPoints:
                                print("Boat overlap detected, please pick a new spot")
                                validPos = False
                                validDir = True
                                validShip -= 1
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        print(boatName.get(validShip) +" outside of game board.")
                        validPos = False
                        validDir = False
                        validShip -= 1
                        break

                    if validPos == True:
                        validDir = True
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(validLetters.get(bow[0].lower())) + str(validNum.get(bow[1]) - i)))
                case _:
                    print("Please pick one for the 4 Cardinal Directions N (up), S (down), E (right), W (Left)")
        
        while True:
            confirm = input(("Are you okay with " + boatName.get(validShip) + " being positioned with the bow at " + bow + " with the rest of the ship facing " + compass.get(direction)) + "? (y/n):  ".strip().lower())
            match(confirm):
                case 'y':
                    print("Continuing")
                    break
                case 'n':
                    print("Clearing")
                    print(validShip)
                    del boatPoints[-((lengths[validShip])):]
                    print(boatPoints)
                    validShip -= 1
                    break
                case _:
                    print("either y or n")
        
        validShip += 1
        validPos = False
        validDir = False
        #reset for next loop

    for i in range(len(boatPoints)):
            boatMap += boatPoints[i]
    return(boatMap)

def convert(boatMap):
    #put in the opponents boat map to generate the two matricies required to handle game logic 
    #can also be used with your boat map to handle local boat attacks
    boatBoard = [0,0,0,0,0], [0,0,0,0], [0,0,0], [0,0,0], [0,0]
    ocean = [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]
    k = 0
    for i in range(5):
        #check all 5 boats
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            boatBoard[i][j] = str((str(boatMap[k]) + str(boatMap[k+1])))
            k += 2
    for i in range(5):
        #check all 5 boats
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            ocean[int(boatBoard[i][j][0])][int(boatBoard[i][j][1])] = 1
    return(ocean, boatBoard)
