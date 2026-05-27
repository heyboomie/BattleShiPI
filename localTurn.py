import GUI

def localTurn(localBoard, boatBoard, prev, w):

    #Takes in the current board, and boat coordiantes
    #Outputs the last move, the local board, and if a win is set

    #initalize
    validMove = False
    prev = []
    prev = GUI.messageBoard("Your Turn, Captain", w, prev)
    boatName = {
        0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
    }
    #names of the boats
    
    while not validMove:
        #do not progress until the move has been validated
        #A-J is the Y axis, 0-9 is the X axis
        move = GUI.getTile(w)

        if localBoard[int(str(move)[0])][int(str(move)[1])] > 1:
            validMove = False
            prev = GUI.messageBoard("You have already fired at this location", w, prev)
            #make sure no duplicate moves
        else:
            validMove = True
    if localBoard[int(str(move)[0])][int(str(move)[1])] == 1:
        prev = GUI.messageBoard("Hit!", w, prev)
        localBoard[int(str(move)[0])][int(str(move)[1])] = 3
        #if theres a boat in the location that was fired upon then change it to a 'hit' tile
    else:
        prev = GUI.messageBoard("Miss!", w, prev)
        localBoard[int(str(move)[0])][int(str(move)[1])] = 2
        #if theres no boat, then, theres no boat
    # 0 is unknown, 1 is a boat (which would be hidden to the player), 2 is a miss, 3 is a hit, 4 is a destroyed ship


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
                #if all segments in a given boat are destroyed put the message out
                prev = GUI.messageBoard("You have destroyed the Enemy's " + boatName.get(i), w, prev)
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
                GUI.clear(prev)
                return(move, localBoard, True)
                #yay!
    GUI.clear(prev)
    return(move, localBoard, False)

def AwayTurn(localBoard, boatBoard, inc, w, prev):
    boatName = {
        0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
    }
    first = {
        "0":"A", "1":"B", "2":"C", "3":"D", "4":"E", "5":"F", "6":"G", "7":"H", "8":"I", "9":"J"
    }
    loss = False
    print(inc)
    if localBoard[int(str(inc[0]))][int(str(inc[1]))] == 1:
        localBoard[int(inc[0])][int(inc[1])] = 3
        for i in range(len(boatBoard)):
            for j in range(len(boatBoard[i])):
                if str(inc) == str(boatBoard[i][j]):
                    prev = GUI.messageBoard("The Enemy has fired at " + first.get(str(inc[0])) + str(inc[1]) + " and hit your " + boatName.get(i), w, prev)
    elif localBoard[int(inc[0])][int(inc[1])] == 0:
        localBoard[int(inc[0])][int(inc[1])] = 2
        prev = GUI.messageBoard("The Enemy has fired at " + first.get(str(inc[0])) + str(inc[1]) + " and missed!", w, prev)
    else:
        prev = GUI.messageBoard("Mismatched Gamestate, please restart your game", w, prev)

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
                #if all segments in a given boat are destroyed put the message out
                prev = GUI.messageBoard("The Enemy has destroyed your " + boatName.get(i), w, prev)
                #figure out how to write text to the screen then do that
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
                #yay!
    
    return(localBoard, loss, prev)
