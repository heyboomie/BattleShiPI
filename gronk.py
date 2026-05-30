from random import randrange

#maybe i should make a gronk class, oh well. too late

def validate(validPos, boatPoints, validShip, bow, direction):
            """the validate funciton from boardInit striped of G/AUI parts"""
            lengths = [5, 4, 3, 3, 2]
            match(direction):
                case 0: #up
                    if int(bow[0]) >= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0]) - i)) + str(bow[1]) in boatPoints:
                                validPos = False
                                bow = None
                                
                                break
                                    #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        validPos = False
                        bow = None

                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(int(bow[0]) - i)) + str(bow[1]))
                        validShip += 1
                        validPos = False
                        bow = None


                        #reset for next loop
                case 2: #down
                    if int(bow[0]) <= (10 - lengths[validShip]):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0]) + i)) + str(bow[1]) in boatPoints:
                               
                                validPos = False
                                bow = None
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                       
                        validPos = False
                        bow = None

                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(int(bow[0]) + i)) + str(bow[1]))
                        validShip += 1
                        validPos = False
                        bow = None
                       
  

                        #reset for next loop
                case 1: #right
                    if int(bow[1]) <= (10 - lengths[validShip]):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0])) + str(int(bow[1]) + i)) in boatPoints:
                                
                                validPos = False
                                bow = None
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                        
                        validPos = False
                        bow = None


                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str(int(bow[0])) + str(int(bow[1]) + i)))
                        validShip += 1
                        validPos = False
                        bow = None
                       

                        #reset for next loop
                case 3: #left
                    if int(bow[1]) >= (lengths[validShip] - 1):
                        for i in range(lengths[validShip]):
                            if (str(int(bow[0])) + str(int(bow[1]) - i)) in boatPoints:
                               
                                validPos = False
                                bow = None
                                break
                                #this looks stupid but it does manage to skip everything and restart the loop
                    else:
                       
                        validPos = False
                        bow = None

                    if validPos == True:
                        
                        for i in range(lengths[validShip]):
                            boatPoints.append((str((bow[0]))) + str(int(bow[1]) - i))
                        validShip += 1
                        validPos = False
                        bow = None
                        
            return(bow, boatPoints, validShip)

def setup():
    '''This is just the random boat selection and conversion stripped of its G/AUI parts'''

    validShip = 0
    boatPoints = []
    boatMap = ''
    while validShip < 5:
            bow = None
            bow = str(randrange(10)) + str(randrange(10))
            direction = int(randrange(4))
            if bow != None:
                bow, boatPoints, validShip = validate(True, boatPoints, validShip, bow, direction)

    for i in range(len(boatPoints)):
            boatMap += boatPoints[i]

     
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

def local(board):
    '''super secret, palantir-based algorhythm to shoot ur boats'''
    valid = False
    while valid == False:
        letter = randrange(10)
        number = randrange(10)
        shot = str(letter) + str(number)
        if board[letter][number] > 1:
            valid = False
            #make sure no duplicate moves
        else:
            valid = True
    return(shot)


def away(inc, localBoard, boatBoard):
    '''guess whattttt. Yeah recycled code. The human way! This is the function for when you shoot the clanker'''
    loss = False
    if localBoard[int(str(inc[0]))][int(str(inc[1]))] == 1:
        localBoard[int(inc[0])][int(inc[1])] = 3
    elif localBoard[int(inc[0])][int(inc[1])] == 0:
        localBoard[int(inc[0])][int(inc[1])] = 2

    for i in range(5):
        #check all 5 boats
        k = 0
        #damaged segment counter
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            if localBoard[int(boatBoard[i][j][0])][int(boatBoard[i][j][1])] == 3:
                k += 1
                #inc damaged segment counter if a segment is damaged
            if k == len(boatBoard[i]):
                for l in range(len(boatBoard[i])):
                    #again go to each segment of the destroyed boat and turn it into a destroyed tile so its not retriggered
                    localBoard[int(boatBoard[i][l][0])][int(boatBoard[i][l][1])] = 4
    k = 0
    for i in range(5):
        #check all 5 boats   
        #damaged segment counter
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            if localBoard[int(boatBoard[i][j][0])][int(boatBoard[i][j][1])] == 4:
                k += 1
            if k == 17:
                loss = True
                #this is a gronk loss, so like player win
    
    return(localBoard, loss)