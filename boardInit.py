
import GUI, random
from time import sleep
from random import random, randrange

def validate(validPos, boatPoints, validShip, msg, bow, direction, gears, w, sf):
            boatName = {
                0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
            }
            boat = str(boatName.get(validShip))
            lengths = [5, 4, 3, 3, 2]
            match(direction):
                case 0: #up
                    if int(bow[0]) >= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0]) - i)) + str(bow[1]) in boatPoints:
                                GUI.clear(msg)
                                msg = GUI.messageBoard("Boat overlap detected, please pick a new spot", w, msg)
                                validPos = False
                                bow = None
                                break
                                    #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        msg = GUI.messageBoard(boat +" outside of game board.", w, msg)
                        validPos = False
                        bow = None

                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(int(bow[0]) - i)) + str(bow[1]))
                        validShip += 1
                        validPos = False
                        bow = None
                        msg = GUI.messageBoard(boat +" placed successfully", w, msg)
                        sf.build()
                        gears = GUI.boatPlace(gears, boatPoints, w)


                        #reset for next loop
                case 2: #down
                    if int(bow[0]) <= (10 - lengths[validShip]):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0]) + i)) + str(bow[1]) in boatPoints:
                                GUI.clear(msg)
                                msg = GUI.messageBoard("Boat overlap detected, please pick a new spot", w, msg)
                                validPos = False
                                bow = None
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        GUI.clear(msg)
                        msg = GUI.messageBoard(boat +" outside of game board.", w, msg)
                        validPos = False
                        bow = None

                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(int(bow[0]) + i)) + str(bow[1]))
                        validShip += 1
                        validPos = False
                        bow = None
                        msg = GUI.messageBoard(boat +" placed successfully", w, msg)
                        sf.build()
                        gears = GUI.boatPlace(gears, boatPoints, w)
  

                        #reset for next loop
                case 1: #right
                    if int(bow[1]) <= (10 - lengths[validShip]):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0])) + str(int(bow[1]) + i)) in boatPoints:
                                GUI.clear(msg)
                                msg = GUI.messageBoard("Boat overlap detected, please pick a new spot", w, msg)
                                validPos = False
                                bow = None
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        GUI.clear(msg)
                        msg = GUI.messageBoard(boat +" outside of game board.", w, msg)
                        validPos = False
                        bow = None


                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(int(bow[0])) + str(int(bow[1]) + i)))
                        validShip += 1
                        validPos = False
                        bow = None
                        msg = GUI.messageBoard(boat +" placed successfully", w, msg)
                        sf.build()
                        gears = GUI.boatPlace(gears, boatPoints, w)

                        #reset for next loop
                case 3: #left
                    if int(bow[1]) >= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0])) + str(int(bow[1]) - i)) in boatPoints:
                                GUI.clear(msg)
                                msg = GUI.messageBoard("Boat overlap detected, please pick a new spot", w, msg)
                                validPos = False
                                bow = None
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        GUI.clear(msg)
                        msg = GUI.messageBoard(boat +" outside of game board", w, msg)
                        validPos = False
                        bow = None

                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str((bow[0]))) + str(int(bow[1]) - i))
                        validShip += 1
                        validPos = False
                        bow = None
                        msg = GUI.messageBoard(boat +" placed successfully", w, msg)
                        sf.build()
                        gears = GUI.boatPlace(gears, boatPoints, w)
                        
            return(bow, gears, msg, boatPoints, validShip, validPos)

def feelinLucky(msg, w, sf):
            validShip = 0
            boatPoints = []
            gears = []
            msg = GUI.messageBoard("Picking Boat Position Randomly, Captain", w, msg)
            sleep(2)
            while validShip < 5:
                        bow = None
                        bow = str(randrange(10)) + str(randrange(10))
                        direction = int(randrange(4))
                        if bow != None:
                            bow, gears, msg, boatPoints, validShip, ValidPos = validate(True, boatPoints, validShip, msg, bow, direction, gears, w, sf)
                            sleep(2*random())
            return(boatPoints, msg, gears)           

def boardInit(w, sf):
    
    validShip = 0
    validPos = False
    
    #like, i know i used this in other places and i could import it, but this is more self contained also im lazy
    boatPoints = []
    boatMap = ''
    #where there the boats are, it will get turned into a string but for the time being

    lengths = [5, 4, 3, 3, 2]
    #probably an easier way but whatever

    direction = 0
    bow = None
    prev = []
    msg = []
    gears = []
    tiles = GUI.boardDraw([[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]], w)
    while validShip < 5:
        
        #do not progress until the positon has been validated
        while bow == None:
            bow = GUI.getTile(w)
            if bow != None:
                prev = [GUI.blueprint(bow, direction, lengths[validShip], prev, w)]
        key = w.checkKey()
            #("bing")
        
        if key == "Escape":
            bow = None
            GUI.clear(prev)
        if bow != None:
            #make sure each letter is right
                validPos = True  
        if key == "r" and bow != None:
            direction += 1
            if direction == 4:
                direction = 0
            #print(bow)
            prev = [GUI.blueprint(bow, direction, lengths[validShip], prev, w)]
        if key == "space" and boatPoints == []:
                    GUI.clear(prev)
                    prev = []
                    boatPoints, msg, gears = feelinLucky(msg, w, sf)
                    break
        if key == 'Return' and validPos == True and bow != None:
            bow, gears, msg, boatPoints, validShip, validPos = validate(validPos, boatPoints, validShip, msg, bow, direction, gears, w, sf)
                        #reset for next loop        
            #print(boatPoints)
            GUI.clear(prev)
            prev = []
    for i in range(len(boatPoints)):
            boatMap += boatPoints[i]
    GUI.clear(gears)
    GUI.clear(msg)
    return(boatMap, tiles)

def convert(boatMap):
    #put in the opponents boat map to generate the two matricies required to handle game logic 
    #can also be used with your boat map to handle local boat attacks
    boatBoard = [[0,0,0,0,0], [0,0,0,0], [0,0,0], [0,0,0], [0,0]]
    ocean = [[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]
    k = 0
    for i in range(5):
        #check all 5 boats
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            boatBoard[i][j] = str((str(boatMap[k]) + str(boatMap[k+1])))
            #print(k)
            #print(boatBoard[i][j])
            if k <= 30:
                k += 2
    for i in range(5):
        #check all 5 boats
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            ocean[int(boatBoard[i][j][0])][int(boatBoard[i][j][1])] = 1
    return(ocean, boatBoard)
