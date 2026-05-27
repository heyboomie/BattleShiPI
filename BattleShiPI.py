#main game file
import boardInit, GUI, localTurn, networkConfig, time, sys, sfx

def setup(): #sets up the game window and server connection
    #print("a")
    mode = None
    sfx = sfx.sfx()
    w = GUI.screenInit()
    while mode == None:
        mode = GUI.modeSelect(w)
        if mode == 0: #server
            me = networkConfig.Server()
            ip, port = me.ownName()
            
            info = GUI.showIP(ip, port, w)
            #print("here")
            me.create()
        elif mode == 1:
            ip, port, info = GUI.inputIP(w)
            #print(ip, " ", port)
            me = networkConfig.Client(str(ip), int(port))
        GUI.clear(info)
    return(me, mode, w, sfx)

def main():
    #print("Game Start")
    #initalize variables
    move = None #where are you shooting
    inc = "" #where are you being shot 
    localBoard = [] #The board your boats are on
    networkBoard = [] #The board youre shooting at
    localShips = [] #Where your ships are
    shipString = None #temp variable to condense ship
    networkShips = [] #Where the ships youre shooting at are stored
    hits = [] #a list of where you have been shot
    fired = [] #a list of where you have shot
    won = False #did you win?
    loss = False #did you lose?
    tileImages = []
    boatImages = []
    textImages = []
    bckgImages = []
    #gameloop
    me, mode, w, sfx = setup()
    #sets up the game

    #draw the background 
    bckgImages = GUI.bckgrDraw(localShips, w)
    shipString, tileImages = boardInit.boardInit(w)
    localBoard, localShips = boardInit.convert(shipString)
    #once the bots are selected then redraw the board to show their location
    GUI.clear(bckgImages)
    bckgImages = GUI.bckgrDraw(localShips, w)
    boatImages = GUI.boatVitals(localShips, localBoard, w)
    #exchange board info with the other player
    networkBoard, networkShips = boardInit.convert(me.tmBoard(shipString))
    #clear the board
    GUI.clear(tileImages)
    #redraw the board with the new marker
    tileImages = GUI.boardDraw(networkBoard, w)

    #if youre a client, do an extra recieve first
    if mode == 1:
        #where am i getting hit?
        while inc == "":
            inc = me.rcTurn()
        #add that to the log
        hits.append(inc)
        #game logic about getting hit
        localBoard, loss, msg = localTurn.AwayTurn(localBoard, localShips, inc, w, textImages)
        #clear any text
        textImages = []
        #update the text
        textImages.append(msg)
        #clear the ships
        GUI.clear(boatImages)
        #redraw the ships, make any updates if needed
        boatImages = GUI.boatVitals(localShips, localBoard, w)

    while (not won) and (not loss): #if the game is neither lost nor won
        #make ur move
        move, networkBoard, won = localTurn.localTurn(networkBoard, networkShips, textImages, w)
        #send the shell off
        me.tmTurn(move)
        #add that to the log
        fired.append(move)
        #clear the board
        GUI.clear(tileImages)
        #redraw the board with the new marker
        tileImages = GUI.boardDraw(networkBoard, w)

        #where am i getting hit?
        inc = ""
        while inc == "":
            inc = me.rcTurn()
        print(inc + "!!!")
        #add that to the log
        hits.append(inc)
        #game logic about getting hit
        localBoard, loss, msg = localTurn.AwayTurn(localBoard, localShips, inc, w, textImages)
        #clear any text
        textImages = []
        #update the text
        textImages.append(msg)
        #clear the ships
        GUI.clear(boatImages)
        #redraw the ships, make any updates if needed
        boatImages = GUI.boatVitals(localBoard, localShips, w)

    if won == True:
        GUI.messageBoard("Congratulations Captain, You have defeated the Enemy Navy", w, [])
    else: 
        GUI.messageBoard("Sorry Captain, You have been defeated by the Enemy Navy", w, [])

    t = time.time()
    with open("GameFile" + t + ".txt", "w") as f:
        f.write(fired, "\n", hits)
        f.close()

    time.sleep(15)
    sys.exit(0)   

main()
