#main game file
import boardInit, GUI, localTurn, networkConfig, time, sys

def setup(): #sets up the game window and server connection
    print("a")
    mode = None
    w = GUI.screenInit()
    while mode == None:
        mode = GUI.modeSelect(w)
        if mode == 0: #server
            me = networkConfig.Server()
            ip, port = me.ownName()
            info = GUI.showIP(ip, port, w)
            print("here")
            me.create()
        elif mode == 1:
            ip, port, info = GUI.inputIP(w)
            me = networkConfig.Client(str(ip), int(port))
        GUI.clear(info)
    return(me, mode, info, w)

def main():
    print("Game Start")
    #initalize variables
    move = None #where are you shooting
    inc = None #where are you being shot 
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
    me, mode, w = setup()
    bckgImages = GUI.bckgrDraw(networkShips, w)
    shipString = boardInit.boardInit(w)
    localBoard, localShips = boardInit.convert(shipString)
    
    networkBoard, networkShips = boardInit.convert(me.tmBoard(shipString))
    GUI.clear(bckgImages)
    bckgImages = GUI.bckgrDraw(networkShips, w)

    if mode == 1:
        inc = me.rcTurn()
        hits.append(inc)
        localBoard, loss, msg = localTurn.AwayTurn(localBoard, localShips, inc, w, textImages)
        textImages = []
        textImages.append(msg)
        GUI.clear(boatImages)
        boatImages = GUI.boatVitals(localBoard, localShips, w)

    while (not won) and (not loss):
        move, networkBoard, won = localTurn.localTurn(networkBoard, networkShips, textImages, w)
        me.tmTurn(move)
        fired.append(move)
        GUI.clear(tileImages)
        tileImages = GUI.boardDraw(networkBoard, w)

        inc = me.rcTurn()
        hits.append(inc)
        localBoard, loss, msg = localTurn.AwayTurn(localBoard, localShips, inc, w, textImages)
        textImages = []
        textImages.append(msg)
        GUI.clear(boatImages)
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
