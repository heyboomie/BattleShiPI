#main game file
import boardInit, GUI, localTurn, networkConfig, sfx, os, gronk
from sys import exit
from time import sleep, time
from random import random

def fileWrite(h, f, lS, nS, dir):
    first = {
        "0":"A", "1":"B", "2":"C", "3":"D", "4":"E", "5":"F", "6":"G", "7":"H", "8":"I", "9":"J"
    }
    boatName = {
        0:"Aircraft Carrier", 1:"Battleship", 2:"Cruiser", 3:"Submarine", 4:"Destroyer"
    }
    t = time()
    fired = []
    hits = []
    localShips = []
    networkShips = [] 
    for i in range(len(f)):
        pos = str(first.get((f[i])[0])) + str(int(f[i][1]) + 1)
        fired.append(pos)
    for i in range(len(h)):
        pos = str(first.get((h[i])[0])) + str(int(h[i][1]) + 1)
        hits.append(pos)
    for i in range(len(lS)):
        localShips.append(boatName.get(i))
        for j in range(len(lS[i])):
            pos = (first.get(str(lS[i][j])[0])) + str(int(str(lS[i][j])[1]) + 1)
            localShips.append(pos)
    for i in range(len(nS)):
        networkShips.append(boatName.get(i))
        for j in range(len(nS[i])):
            pos = (first.get(str(nS[i][j])[0])) + str(int(str(nS[i][j])[1]) + 1)
            networkShips.append(pos)
    os.chdir(dir)
    with open("GameFile" + str(t) + ".txt", "w") as f:
        f.write("Filename is seconds since Unix Epoch at game end" + "\n" + "Your Moves:  " + str(fired) + "\n" + "Enemy Moves: " + str(hits) + '\n' + "Your Ship Locations:  " + str(localShips) + "\n" + "Enemy Ship Locations: " + str(networkShips)) 
        f.close()

def setup(sf): #sets up the game window and server connection
    #print("a")
    mode = None
    me = None

    w = GUI.screenInit()
    while mode == None:
        mode = GUI.modeSelect(w)
        if mode == 0: #server
            me = networkConfig.Server()
            ip, port = me.ownName()
            sf.ping()
            info = GUI.showIP(ip, port, w)
            #print("here")
            me.create()
        elif mode == 1:
            ip, port, info = GUI.inputIP(w)
            sf = sfx.sfx()
            if ip.lower().strip() == "gronk":
                break
            #print(ip, " ", port)
            me = networkConfig.Client(str(ip), int(port))
    GUI.clear(info)
    return(me, mode, w)

def main(re, me, mode, w):
    dir = os.path.dirname(os.path.abspath(__file__))
    sf = sfx.sfx()
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
    if re == False:
        me, mode, w = setup(sf)
    #sets up the game

    #draw the background 
    bckgImages = GUI.bckgrDraw(localShips, w)
    shipString, tileImages = boardInit.boardInit(w, sf)
    localBoard, localShips = boardInit.convert(shipString)
    #once the bots are selected then redraw the board to show their location
    GUI.clear(bckgImages)
    bckgImages = GUI.bckgrDraw(localShips, w)
    boatImages = GUI.boatVitals(localShips, localBoard, w)
    #exchange board info with the other player
    if me != None:
        networkBoard, networkShips = boardInit.convert(me.tmBoard(shipString))
    else:
        networkBoard, networkShips = gronk.setup()
    #clear the board
    GUI.clear(tileImages)
    #redraw the board with the new marker
    tileImages = GUI.boardDraw(networkBoard, w)

    #if youre a client, do an extra recieve first
    if mode == 1:
        #where am i getting hit?
        inc = ''
        while inc == "":
            if (me != None):
                inc = me.rcTurn()
            else:
                inc = gronk.local(localBoard)
        
        #add that to the log
        hits.append(inc)
        #game logic about getting hit
        localBoard, loss, msg = localTurn.AwayTurn(localBoard, localShips, inc, w, textImages, sf)
        #clear any text
        textImages = msg
        #update the text
        #clear the ships
        GUI.clear(boatImages)
        #redraw the ships, make any updates if needed
        boatImages = GUI.boatVitals(localShips, localBoard, w)
    if mode == 0:
        textImages = GUI.messageBoard("Your First Move, Captain", w, textImages)

    while not loss: #if the game is not lost 
        
        #make ur move
        move, networkBoard, won, textImages = localTurn.localTurn(networkBoard, networkShips, textImages, w, sf)
        #send the shell off
        if (me != None):
            me.tmTurn(move)
        else:
            networkBoard, won = gronk.away(move, networkBoard, networkShips)
        
        #add that to the log
        fired.append(move)
        #clear the board
        GUI.clear(tileImages)
        #redraw the board with the new marker
        tileImages = GUI.boardDraw(networkBoard, w)
        #print("eot")
        if won == True:
            break
        #where am i getting hit?
        inc = ''
        while inc == "":
            if (me != None):
                inc = me.rcTurn()
            else:
                sleep(10*random())
                inc = gronk.local(localBoard)
        #add that to the log
        hits.append(inc)
        #game logic about getting hit
        localBoard, loss, msg = localTurn.AwayTurn(localBoard, localShips, inc, w, textImages, sf)
        #clear any text
        textImages = msg
        #update the text
        #clear the ships
        GUI.clear(boatImages)
        #redraw the ships, make any updates if needed
        boatImages = GUI.boatVitals(localShips, localBoard, w)
    if won == True:
        GUI.messageBoard("Congratulations Captain, You have defeated the Enemy Navy", w, [])
        sf.win()
    else: 
        GUI.messageBoard("Sorry Captain, You have been defeated by the Enemy Navy", w, [])
        sf.loss()
    sleep(5)
    
    fileWrite(hits, fired, localShips, networkShips, dir)
    textImages = GUI.messageBoard("Hit enter to play again, hit any other key to quit", w, textImages)
    again = w.getKey()
    if again == "Return":
        GUI.clear(textImages)
        msg = GUI.messageBoard("Restarting", w, textImages)
        sleep(3)
        return(True, me, mode, w, sf)
    else:
        GUI.clear(textImages)
        msg = GUI.messageBoard("Quitting", w, textImages)
        sleep(10)
        exit(0)

re = False
me = None
mode = None
w = None
sf = None
while True:
    folder = os.path.dirname(os.path.abspath(__file__)) + "\img"
    os.chdir(folder)
    re, me, mode, w, sf = main(re, me, mode, w, sf)
