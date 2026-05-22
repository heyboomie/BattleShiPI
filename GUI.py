from graphics import *
import os
from time import sleep, time

def screenInit(mode):

    window = "BattleShiPI " + mode
    #name the window to the right name
    w = GraphWin(window, 1280, 720)
    #HD screen baby
    w.setBackground(color_rgb(30,53,175))
    folder = os.path.dirname(os.path.abspath(__file__))
    os.chdir(folder)
    #make sure the images load

    return(w)

def boardOrder(boatMap):
    for i in range(len(boatMap)):
        direction = int(boatMap[i][1]) - int(boatMap[i][0])
         # +1 is E, -1 is W, +10 N, -10S 
        if direction < 0:
            (boatMap[i]).reverse() 
    return(boatMap)

def close(w):   
    w.close()

def textFormatMed(text, x, y, w):
    t = Text(Point(x, y), text)
    t.setSize(25)
    t.setTextColor(color_rgb(240,240,240))
    t.setFace("helvetica")
    t.setStyle("italic")
    t.draw(w)
    return(t)

def textFormatSml(text, x, y, w):
    t = Text(Point(x, y), text)
    t.setSize(12)
    t.setTextColor(color_rgb(240,240,240))
    t.setFace("helvetica")
    t.setStyle("bold")
    t.draw(w)
    return(t)

def boardDraw(map,w):

    topLeftX, topLeftY = 185, 85
    #topleft of this tile is (160, 55)
    #topleft most tile position
    imageMap = []
    boatName = {
        0:"Carrier", 1:"Battle", 2:"Cruiser", 3:"Sub", 4:"Destroyer"
    }
    common = ["Water.gif", "Water.gif", "Miss.gif", "Hit.gif", "Hit.gif"]
    for i in range(len(map)):
        for j in range(len(map[i])):
            #if map[i][j] == 4:    
            #    for u in range(len(boats)):
            #        for v in range(len(boats[u])):
            #            if (str(i)+str(j)) == str(boats[u][v]):
            #                for x in range(len(boats)):
            #                    direction = abs(int(boats[x][1]) - int(boats[x][0]))
            #                    if direction == 10:
            #                       header = "u"
            #                    else:
            #                        header = "h"
                             #+1 is E, -1 is W, +10 N, -10S 
                                #check which image set you use
                            #image = header + boatName.get(u) + str(v) +".gif"q
                            #uncomment when files updated
            #                image = boatName.get(u) + str(v) +".gif"
                            #use this for testing
            #               mark = Image(Point((topLeftX + 61*j), (topLeftY + 61*i)), image)
            #                mark.draw(w)
            #                imageMap.append(mark)
            
            tile = Image(Point((topLeftX + 61*j), (topLeftY + 61*i)), common[map[i][j]])
            tile.draw(w)
            imageMap.append(tile) 
    #this draws the main board
    #it will not draw boats, even if they are destroyed, idk why i thought i would add that 
    #     
    return(imageMap)
     
def boatVitals(boats, w):
    boatX, boatY = 900, 115
    boatName = {
        0:"Carrier", 1:"Battle", 2:"Cruiser", 3:"Sub", 4:"Destroyer"
    }
    lst = []
    for i in range(len(boats)):
        for j in range(len(boats[i])):
            if boats[i][j] == 1:
                pre = "d"
            else:
                pre = ''
            image = pre + boatName.get(i) + str(j) +".gif"
            mark = Image(Point((boatX + 61*j), (boatY + 91*i)), image)
            mark.draw(w)
            lst.append(mark)
    return(lst)

def bckgrDraw(boatMap, w):
    Letters = {
        0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J"
        }
    Nums = {
        0:"1", 1:"2", 2:"3", 3:"4", 4:"5", 5:"6", 6:"7", 7:"8", 8:"9", 9:"10"
    }
    difBlue = color_rgb(75,85,180)
    textMap = []
    topLeftX, topLeftY = 185, 85
    boatX, boatY = 900, 115
    boardBG = Rectangle(Point(topLeftX - 80, topLeftY - 80), Point(topLeftX + 61*9 + 80, topLeftY + 61*9 + 80))
    textMap.append(boardBG)
    boardBG.setFill(difBlue)
    boardBG.draw(w)
    for i in range(len(boatMap)):
        vitalBG = Rectangle(Point(boatX - 40, boatY - 55), Point(boatX + 61*(len(boatMap[i]) - 1) + 40, boatY + 91*i + 40))
        textMap.append(vitalBG)
        vitalBG.setFill(difBlue)
        vitalBG.setOutline(difBlue)
        vitalBG.draw(w)

    for i in range(10):
          textMap.append(textFormatMed(Letters.get(i), (topLeftX - 50), (topLeftY + 61*i), w))
          textMap.append(textFormatMed(Nums.get(i), (topLeftX + 61*i), (topLeftY - 50), w))
    for i in range(len(boatMap)):
        for j in range(len(boatMap[i])):
            textMap.append(textFormatSml(((Letters.get(int(boatMap[i][j][0]))) + (Nums.get(int(boatMap[i][j][1])))), (boatX + 61*j), (boatY + 91*i - 40), w))
    
    inc = Rectangle(Point(boatX - 40, boatY + 91*4.75), Point(boatX + 61*4 + 40, boatY + 91*6.25))
    textMap.append(inc)
    inc.setFill(difBlue)
    inc.setOutline(difBlue)
    inc.draw(w)
    spot = Rectangle(Point(boatX + 61*2, boatY + 91*5), Point(boatX + 61*4 + 20, boatY + 91*6))
    textMap.append(spot)
    spot.setFill(color_rgb(30,53,175))
    spot.setOutline(color_rgb(30,53,175))
    spot.draw(w)

    textMap.append(textFormatMed("Incoming", boatX + 40, boatY + 91*5 + 20, w))
    textMap.append(textFormatMed("Shots", boatX + 40, boatY + 91*5 + 65, w))

    return(textMap)

def clear(board, w):
    for tile in board:
        tile.undraw()

#temp test code
w = screenInit("Host")
# boatMap = boardOrder((['00', '01', '02', '03', '04'], ['10', '11', '12', '13'], ['22', '21', '20'], ['30', '31', '32'], ['41', '40']))
# boatHealth = [[0,0,0,0,0],[1,1,1,1],[0,0,0],[0,0,0],[0,0]]
# board = [] #keep track of the board objects so we can delete them later
# team = []
# text = []
# print("a")
# print(os.getcwd())
# text = text + (bckgrDraw(boatMap, w))
# board = board + (boardDraw(([4, 4, 4, 4, 4, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), w))
# team = team + (boatVitals(boatHealth, w))

# while True:
#     if w.checkKey() == "d":
#         clear(board, w)
#         board = []
#         a = time()
#         board = board + (boardDraw(([4, 4, 4, 4, 4, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), w))
#         print(time() - a)
#     if w.checkKey() == "t":
#         clear(team, w)
#         team = []
#         a = time()
#         team = team + (boatVitals(boatHealth, w))
#         print(time() - a)
#     if w.checkKey() == "w":
#         clear(text, w)
#         text = []
#         a = time()
#         text = text + (bckgrDraw(boatMap, w))
#         print(time() - a)
#     if w.checkKey() == "q":
#         close(w)
