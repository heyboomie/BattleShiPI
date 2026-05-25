#main game file
import boardInit, GUI, localTurn, networkConfig

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
            me.create()
        elif mode == 1:
            ip, port, info = GUI.inputIP(w)
            me = networkConfig.Client()
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
    #gameloop
    me, mode, info, w = setup()
    GUI.bckgrDraw(networkShips, w)
    shipString = boardInit.boardInit(w)
    localBoard, localShips = boardInit.convert(shipString)
    
    networkBoard, networkShips = boardInit.convert(me.tmBoard(shipString))

    if mode == 1:
        inc = me.rcTurn()
        hits.append(inc)
        localBoard, loss = localTurn.AwayTurn(localBoard, localShips, inc)
        GUI.clear(boatImages)
        boatImages = GUI.boatVitals(localBoard, localShips, w)

    while (not won) and (not loss):
        move, networkBoard, won = localTurn.localTurn(networkBoard, networkShips)
        me.tmTurn(move)
        fired.append(move)
        GUI.clear(tileImages)
        tileImages = GUI.boardDraw(networkBoard, w)

        inc = me.rcTurn()
        hits.append(inc)
        localBoard, loss = localTurn.AwayTurn(localBoard, localShips, inc)
        GUI.clear(boatImages)
        boatImages = GUI.boatVitals(localBoard, localShips, w)

    if won == True:
        

main()
