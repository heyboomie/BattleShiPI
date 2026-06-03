import GUI

def radar(networkBoard, localBoard, localShips, w, sf):
    inRange = 0
    dmgRange = 0
    ping = None
    #write the code to draw the radar symbol
    while ping == None:
        ping = GUI.getTile(w)
        if w.checkKey() == "r":
            ping = None
            #write the code to draw the cannon symbol
            break
    if localBoard[localShips[0][0][0]][localShips[0][0][1]] < 4 and ping != None: #if the aircraft carrier is still alive
        sf.ping()
        for i in range(3): #3 rows
            for j in range(3): #3 columns
                if [int(ping[0]) - i - 1] >= 0 and [int(ping[1]) - j - 1] >= 0:
                    if networkBoard[int(ping[0]) - i - 1][int(ping[1]) - j - 1] == 1:
                        inRange += 1
                    elif networkBoard[int(ping[0]) - i - 1][int(ping[1]) - j - 1] >= 3:
                        dmgrange += 1
        msg = GUI.messageBoard(str(inRange) + " Active Boats              " + str(dmgRange) + " Destroyed Boats          ", w, prev)
        return(prev, True)
    elif localBoard[localShips[0][0][0]][localShips[0][0][1]] == 4 and ping != None:
        msg = GUI.messageBoard("Sorry Captain, Your Aircraft Carrier has been destroyed. No recon for us", w, prev)
        #finish this later:D
        return(prev, False)
    return([], False)

def localTurn(rad, myShips, myBoard, localBoard, boatBoard, prev, w, sf):

    #Takes in the current board, and boat coordiantes
    #Outputs the last move, the local board, and if a win is set

    #initalize
    validMove = False
    prev = []
    # prev = GUI.messageBoard("Your Turn, Captain", w, prev)
    boatName = {
        0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
    }
    #names of the boats
    
    while not validMove:
        move = None
        #do not progress until the move has been validated
        #A-J is the Y axis, 0-9 is the X axis
        while move == None:
            move = GUI.getTile(w)
            if w.checkKey() == "r" and rad == False:
                prev, rad = radar(localBoard, myBoard, myShips, w, sf)
                
        if localBoard[int(str(move)[0])][int(str(move)[1])] > 1:
            validMove = False
            prev = GUI.messageBoard("You have already fired at this location", w, prev)
            #make sure no duplicate moves
        else:
            validMove = True
    if localBoard[int(str(move)[0])][int(str(move)[1])] == 1:
        prev = GUI.messageBoard("Hit!", w, prev)
        sf.hit()
        localBoard[int(str(move)[0])][int(str(move)[1])] = 3
        #if theres a boat in the location that was fired upon then change it to a 'hit' tile
    else:
        prev = GUI.messageBoard("Miss!", w, prev)
        sf.miss()
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
                sf.sink()
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
                return(move, localBoard, True, prev)
                #yay!
    return(rad, move, localBoard, False, prev)

def AwayTurn(localBoard, boatBoard, inc, w, prev, sf):
    boatName = {
        0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
    }
    first = {
        "0":"A", "1":"B", "2":"C", "3":"D", "4":"E", "5":"F", "6":"G", "7":"H", "8":"I", "9":"J"
    }
    loss = False
    #print(inc)
    if localBoard[int(str(inc[0]))][int(str(inc[1]))] == 1:
        localBoard[int(inc[0])][int(inc[1])] = 3
        for i in range(len(boatBoard)):
            for j in range(len(boatBoard[i])):
                if str(inc) == str(boatBoard[i][j]):
                    prev = GUI.messageBoard("The Enemy has fired at " + first.get(str(inc[0])) + str(int(inc[1]) + 1) + " and hit your " + boatName.get(i), w, prev)
                    sf.hit()
    elif localBoard[int(inc[0])][int(inc[1])] == 0:
        localBoard[int(inc[0])][int(inc[1])] = 2
        prev = GUI.messageBoard("The Enemy has fired at " + first.get(str(inc[0])) + str(int(inc[1]) + 1) + " and missed!", w, prev)
        sf.miss()
    else:
        #print(localBoard[int(inc[0])][int(inc[1])])
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
                sf.sink()
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
