def localTurn(localBoard, boatBoard):
    #Takes in the current board, and boat coordiantes
    #Outputs the last move, the local board, and if a win is set

    #initalize
    validMove = False
    validLetters = {
        "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9
        }
    validNum = {
        "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9
    }
    #look okay, i know its 0-9 not 1-10, but its WAY easier to code this, if i go to a GUI i will go back to 1-10 visually
    boatName = {
        0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
    }
    #names of the boats
    
    while not validMove:
        #do not progress until the move has been validated
        #A-J is the Y axis, 0-9 is the X axis
        move = input("Input your move: ") #if i move to a visual approach I will use a click system which will not require this code, but for the MVP this will have to do
        
        if len(move) != 2:
            #check the move is in a valid form to prevent trying to index a part of the string that doesnt exist
            #also prevents like A33 or whatever
            print("Please type moves in Letter Number from A-J, 0-9 (ex. B0, J6)")
        elif (validLetters.get(move[0].lower()) != None) and (validNum.get(move[1]) != None):
            #make sure each letter is right
            validMove = True
        else:
            print("Please type moves in Letter Number from A-J, 0-9 (ex. B0, J6)")

        if localBoard[validLetters.get(move[0].lower())][validNum.get(move[1])] > 1:
            validMove = False
            print("You have already fired into that zone")
            #make sure no duplicate moves
            #note t future me, standarize the form they get put in, so a6 and A6 arent counted as different
            #i guess I could also check the tile too thats probalby easier
    coordinate = move[0].upper() + move[1]
    #convert the move into a coordinate that cna be used with the matrix
    print("!!: ", coordinate)
    if localBoard[validLetters.get(move[0].lower())][validNum.get(move[1])] == 1:
        print("hit!")
        localBoard[validLetters.get(move[0].lower())][validNum.get(move[1])] = 3
        #if theres a boat in the location that was fired upon then change it to a 'hit' tile
    else:
        print("miss.")
        localBoard[validLetters.get(move[0].lower())][validNum.get(move[1])] = 2
        #if theres no boat, then, theres no boat
    # 0 is unknown, 1 is a boat (which would be hidden to the player), 2 is a miss, 3 is a hit, 4 is a destroyed ship
    print("check", move)

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
                print("You destroyed your enemies", boatName.get(i))
                for l in range(len(boatBoard[i])):
                    #again go to each segment of the destroyed boat and turn it into a destroyed tile so its not retriggered
                    localBoard[int(boatBoard[i][l][0])][int(boatBoard[i][l][1])] = 4
    for i in range(5):
        #check all 5 boats
        k = 0
        #damaged segment counter
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            if localBoard[int(boatBoard[i][j][0])][int(boatBoard[i][j][1])] == 4:
                k += 1
            if k == 17:
                print("You win!")
                return(coordinate, localBoard, True)
                #yay!
    for i in range(10):
        print(localBoard[i])
    #print board for testing purposes
    return(coordinate, localBoard, False)
