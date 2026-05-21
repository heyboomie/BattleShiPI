from graphics import *
import os

def screenInit(mode):

    window = "BattleShiPI " + mode
    #name the window to the right name
    win = GraphWin(window, 1280, 720)
    #HD screen baby
    win.setBackground(color_rgb(30,53,175))
    folder = os.path.dirname(os.path.abspath(__file__))
    os.chdir(folder)
    #make sure the images load

    return(win)

def boardOrder(boatMap):
    for i in range(len(boatMap)):
        direction = int(boatMap[i][1]) - int(boatMap[i][0])
         # +1 is E, -1 is W, +10 N, -10S 
        if direction < 0:
            (boatMap[i]).reverse() 
    return(boatMap)

def close(w):   
    w.close()

def boardDraw(map, boats,w):

    topLeftX, topLeftY = 190, 85
    #topleft most tile position
    waterMap = []
    markMap = []
    boatName = {
        0:"Carrier", 1:"Battle", 2:"Cruiser", 3:"Sub", 4:"Destroyer"
    }
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 2:
                mark = Image(Point((topLeftX + 61*j), (topLeftY + 61*i)), "Miss.gif")
                mark.draw(w)
                markMap.append(map)
            elif map[i][j] == 3:
                mark = Image(Point((topLeftX + 61*j), (topLeftY + 61*i)), "Hit.gif")
                mark.draw(w)
                markMap.append(map)
            elif map[i][j] == 4:    
                for u in range(len(boats)):
                    for v in range(len(boats[u])):
                        if (str(i)+str(j)) == str(boats[u][v]):
                            image = boatName.get(u) + str(v) +".png"
                            mark = Image(Point((topLeftX + 61*j), (topLeftY + 61*i)), image)
                            mark.draw(w)
                            markMap.append(map)
            else:
                tile = Image(Point((topLeftX + 61*j), (topLeftY + 61*i)), "Water.gif")
                tile.draw(w)
                waterMap.append(tile)     
    return(waterMap, markMap)
            
#temp test code
#w = screenInit("Host")
#boatMap = boardOrder((['00', '01', '02', '03', '04'], ['10', '11', '12', '13'], ['22', '21', '20'], ['30', '31', '32'], ['41', '40']))
#print("a")
#print(os.getcwd())
#while True:
#    if w.checkKey() == "q":
#        close(w)
#    water, board = boardDraw(([4, 4, 4, 4, 4, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), boatMap, w)

    
