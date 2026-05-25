from graphics import *
import os
from time import sleep, time

#if i made this all a class it would have been a lottt nicer, however its kinda too late for that

def screenInit():

    window = "BattleShiPI "
    #name the window to the right name
    w = GraphWin(window, 1280, 720)
    #HD screen baby
    w.setBackground(color_rgb(30,53,175))
    folder = os.path.dirname(os.path.abspath(__file__)) + "\img"
    os.chdir(folder)
    #make sure the images load

    return(w)

def clear(board):
    for tile in board:
        tile.undraw()

def messageBoard(text, w, prev):
    clear(prev)
    lst = []
    board = Rectangle(Point(1020, 440), Point(1260, 514))
    board.setWidth(10)
    board.setFill(color_rgb(0,0,0))
    board.setOutline(color_rgb(75,85,180))
    board.draw(w)
    lst.append(board)
    if len(text) < 29:
        t = textFormatSml(text, 1140, 477, w)
        lst.append(t)
    else:
        t1 = text[:len(text) // 2]
        t2 = text[len(text) // 2:]
        tobj1 = textFormatSml(t1, 1140, 467, w)
        tobj2 = textFormatSml(t2, 1140, 487, w)
        lst.append(tobj1)
        lst.append(tobj2)
    
    return(lst)

def boardOrder(boatMap):
    for i in range(len(boatMap)):
        direction = int(boatMap[i][1]) - int(boatMap[i][0])
         # +1 is E, -1 is W, +10 N, -10S 
        if direction < 0:
            (boatMap[i]).reverse() 
    return(boatMap)

def close(w):   
    w.close()

def textFormatLrg(text, x, y, w):
    t = Text(Point(x, y), text)
    t.setSize(36)
    t.setTextColor(color_rgb(240,240,240))
    t.setFace("helvetica")
    t.setStyle("italic")
    t.setStyle("bold")
    t.draw(w)
    return(t)

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

def modeSelect(w):
    screen = []
    t = textFormatLrg("Please select if your RPi is acting as the: ", 640, 240, w)
    screen.append(t)
    b1 = Rectangle(Point(400-100, 300), Point(400+100, 400))
    b1.setWidth(10)
    b1.setFill(color_rgb(0,0,0))
    b1.setOutline(color_rgb(75,85,180))
    b1.draw(w)
    screen.append(b1)
    b2 = Rectangle(Point(880-100, 300), Point(880+100, 400))
    b2.setWidth(10)
    b2.setFill(color_rgb(0,0,0))
    b2.setOutline(color_rgb(75,85,180))
    b2.draw(w)
    screen.append(b2)
    t1 = textFormatLrg("Host", 400, 350, w)
    screen.append(t1)
    t2 = textFormatLrg("Client", 880, 350, w)
    screen.append(t2)
    mode = None
    while mode == None:
        click = w.getMouse()
        print(click)
        if (click.getX() > 400-100) and (click.getX() < 400+100) and (click.getY() > 300) and (click.getY() < 400):
            mode = 0
        elif (click.getX() > 880-100) and (click.getX() < 880+100) and (click.getY() > 300) and (click.getY() < 400):
            mode = 1
        print(mode)
    clear(screen)
    return(mode)

def showIP(IP, Host, w):
    return(textFormatLrg("IP :" + IP + " Host: " + Host, 1280/2, 720/2, w))

def inputIP(w):
    width = 125 #+/-
    height = 25 #+/-
    ipRect = Rectangle(Point(720-width, 300-height), Point(720+width, 300 + height)) 

def boardDraw(map,w):

    topLeftX, topLeftY = 185, 85
    #topleft of this tile is (160, 55)
    #topleft most tile position
    imageMap = []
    common = ["Water.gif", "Water.gif", "Miss.gif", "Hit.gif", "Hit.gif"]
    for i in range(len(map)):
        for j in range(len(map[i])):
            tile = Image(Point((topLeftX + 61*j), (topLeftY + 61*i)), common[map[i][j]])
            tile.draw(w)
            imageMap.append(tile) 
    #this draws the main board
    #it will not draw boats, even if they are destroyed, idk why i thought i would add that 
    #     
    return(imageMap)
     
def boatVitals(boatBoard, localBoard, w):
    boatX, boatY = 900, 115
    boatName = {
        0:"Carrier", 1:"Battle", 2:"Cruiser", 3:"Sub", 4:"Destroyer"
    }
    lst = []
    for i in range(5):
        #check all 5 boats
        k = 0
        #damaged segment counter
        for j in range(len(boatBoard[i])):
            #check each segment of each boat
            if localBoard[int(boatBoard[i][j][0])][int(boatBoard[i][j][1])] >= 3:
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

def blueprint(bow, dir, l, prev, w):
    difBlue = color_rgb(135,175,255)
    white = color_rgb(240, 240, 240)
    bow = str(bow)
    X = int(bow[1])
    Y = int(bow[0])
    if dir > 1:
        if dir == 2:
            Y = int(bow[0]) + int((l)) - 1
        elif dir == 3:
            X = int(bow[1]) - int((l)) + 1
        dir -= 2
    
    dirMap = [[0, -61], [61, 0]]
    clear(prev)
    topLeftX, topLeftY = 190, 85 #might be wrong
    bp = Rectangle(Point(topLeftX - 15 + 61*X, topLeftY + 15 + 61*Y), Point((topLeftX + 15 + (l-1)*(dirMap[dir][0]) + 61*X), (topLeftY - 15 + (l-1)*(dirMap[dir][1]) + 61*Y)))
    bp.setFill(difBlue)
    bp.setOutline(white)
    bp.draw(w)
    return(bp)

def getTile(w):
    tlX = 160
    tlY = 55
    tl = w.getMouse()
    if tl != None:
        if (tl.getX() > tlX) and (tl.getX() < tlX + 610) and (tl.getY() > tlY) and (tl.getY() < tlY + 610):
            tile = (str((tl.getY() - tlY) // 61)[0] + str((tl.getX() - tlX) // 61)[0])
            return(tile)

def boatPlace(pos, points, w):
    clear(pos)
    lst = []
    boatX, boatY = 190, 85
    for i in range(len(points)):
        gear = Image(Point(boatX + 61*int(points[i][1]), boatY + 61*int(points[i][0])), "building.gif")
        gear.draw(w)
        lst.append(gear)
    return(lst)
# temp test code
# w = screenInit()
# boatMap = []
# boatMap = boardOrder((['00', '01', '02', '03', '04'], ['10', '11', '12', '13'], ['22', '21', '20'], ['30', '31', '32'], ['41', '40']))
# # boatHealth = [[0,0,0,0,0],[1,1,1,1],[0,0,0],[0,0,0],[0,0]]
# board = [] #keep track of the board objects so we can delete them later
# team = []
# text = []
# print("a")
# print(os.getcwd())
# text = text + (bckgrDraw(boatMap, w))
# board = board + (boardDraw(([4, 4, 4, 4, 4, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), w))
# team = team + (boatVitals(boatMap,([4, 4, 4, 4, 4, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), w))
# bp = Image(Point(910 + 61*3, 130 + 61*8), "Hit.gif")
# bp.draw(w)
# modeSelect(w)
# bckgrDraw(boatMap, w)
# while True:
#     getTile(w)
    # if w.checkKey() == "d":

    #      clear(board)
    #      board = []
    #      a = time()
    #      board = board + (boardDraw(([4, 4, 4, 4, 4, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), w))
    #      print(time() - a)
    # if w.checkKey() == "t":
    #      clear(team)
    #      team = []
    #      a = time()
    #      team = team + (boatVitals(boatMap,([4, 4, 4, 4, 4, 0, 0, 0, 0, 0], [4, 4, 4, 4, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), w))
    #      print(time() - a)
    # if w.checkKey() == "w":
    #      clear(text)
    #      text = []
    #      a = time()
    #      text = text + (bckgrDraw(boatMap, w))
    #      b, t = messageBoard("You have destroyed the enemy Aircraft Carrier", w)
    #      text.append(t)
    #      board.append(b)
    #      print(time() - a)
    # if w.checkKey() == "b":
    #     a = time()
    #     bp = blueprint("05", 3, 5, bp, w)
    #     print(time() - a)
    #     hit = textFormatLrg("A10", 910 + 61*3, 130 + 61*8, w)
#     #messageBoard("a", w)
    # if w.checkKey() == "q":
    #     close(w)
