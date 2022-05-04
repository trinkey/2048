import turtle
import random
board = [[], [], [], []]
av = []
h = 0
if True:
    scr = turtle.Screen()._root
    scr.iconbitmap("2048/2048.ico")
    scr = turtle.Screen()
    scr.setup(1080, 1080)
    scr.bgcolor("#000000")
    scr.addshape("2048/0.gif")
    scr.addshape("2048/2.gif")
    scr.addshape("2048/4.gif")
    scr.addshape("2048/8.gif")
    scr.addshape("2048/16.gif")
    scr.addshape("2048/32.gif")
    scr.addshape("2048/64.gif")
    scr.addshape("2048/128.gif")
    scr.addshape("2048/256.gif")
    scr.addshape("2048/512.gif")
    scr.addshape("2048/1024.gif")
    scr.addshape("2048/2048.gif")
    scr.addshape("2048/4096.gif")
    scr.addshape("2048/8192.gif")
    scr.addshape("2048/16384.gif")
    scr.addshape("2048/32768.gif")
    scr.addshape("2048/65536.gif")
    scr.addshape("2048/131072.gif")
    scr.title("2048 - The fun tile matching math game!")
    t0 = turtle.Turtle()
    t0.shape("2048/0.gif")
    t0.pu()
    t0.speed(0)
    t0.goto(-392, 392)
    t1 = turtle.Turtle()
    t1.shape("2048/0.gif")
    t1.pu()
    t1.speed(0)
    t1.goto(-130, 392)
    t2 = turtle.Turtle()
    t2.shape("2048/0.gif")
    t2.pu()
    t2.speed(0)
    t2.goto(130, 392)
    t3 = turtle.Turtle()
    t3.shape("2048/0.gif")
    t3.pu()
    t3.speed(0)
    t3.goto(392, 392)
    t4 = turtle.Turtle()
    t4.shape("2048/0.gif")
    t4.pu()
    t4.speed(0)
    t4.goto(-392, 130)
    t5 = turtle.Turtle()
    t5.shape("2048/0.gif")
    t5.pu()
    t5.speed(0)
    t5.goto(-130, 130)
    t6 = turtle.Turtle()
    t6.shape("2048/0.gif")
    t6.pu()
    t6.speed(0)
    t6.goto(130, 130)
    t7 = turtle.Turtle()
    t7.shape("2048/0.gif")
    t7.pu()
    t7.speed(0)
    t7.goto(392, 130)
    t8 = turtle.Turtle()
    t8.shape("2048/0.gif")
    t8.pu()
    t8.speed(0)
    t8.goto(-392, -130)
    t9 = turtle.Turtle()
    t9.shape("2048/0.gif")
    t9.pu()
    t9.speed(0)
    t9.goto(-130, -130)
    t10 = turtle.Turtle()
    t10.shape("2048/0.gif")
    t10.pu()
    t10.speed(0)
    t10.goto(130, -130)
    t11 = turtle.Turtle()
    t11.shape("2048/0.gif")
    t11.pu()
    t11.speed(0)
    t11.goto(392, -130)
    t12 = turtle.Turtle()
    t12.shape("2048/0.gif")
    t12.pu()
    t12.speed(0)
    t12.goto(-392, -392)
    t13 = turtle.Turtle()
    t13.shape("2048/0.gif")
    t13.pu()
    t13.speed(0)
    t13.goto(-130, -392)
    t14 = turtle.Turtle()
    t14.shape("2048/0.gif")
    t14.pu()
    t14.speed(0)
    t14.goto(130, -392)
    t15 = turtle.Turtle()
    t15.shape("2048/0.gif")
    t15.pu()
    t15.speed(0)
    t15.goto(392, -392)
    scr.bgpic("2048/board.gif")
    scr.bgcolor("#F1BB35")
def updateFromTXT():
    global board, av, score, hs, started, updateIcons
    lines = open("2048/board.txt").read().split(" ")
    started = int(lines[0])
    x = 1
    for i in range(4):
        for o in range(4):
            board[i].append(int(lines[x]))
            x += 1
    score = int(lines[17])
    hs = int(lines[18])
    updateIcons()
    x = 0
    for i in range(4):
        for o in range(4):
            if board[i][o] == 0:
                av.append(x)
                x += 1
def resetGame():
    global hs, updateFromTXT
    f = open("2048/board.txt", "w")
    f.write("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 " + str(hs))
    f.close()
    updateFromTXT()
def updateTXT():
    global started, board, score, hs
    f = open("2048/board.txt", "w")
    m = str(started) + " " + str(board[0][0]) + " " + str(board[0][1]) + " " + str(board[0][2]) + " " + str(board[0][3]) + " " + str(board[1][0]) + " " + str(board[1][1]) + " " + str(board[1][2]) + " " + str(board[1][3]) + " " + str(board[2][0]) + " " + str(board[2][1]) + " " + str(board[2][2]) + " " + str(board[2][3]) + " " + str(board[3][0]) + " " + str(board[3][1]) + " " + str(board[3][2]) + " " + str(board[3][3]) + " " + str(score) + " " + str(hs)
    f.write(m)
def updateIcons():
    global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, board, scr
    # Credit for the checks goes to Bob the AI#2318 on discord
    # Thanks!
    t0.shape(f"2048/{board[0][0]}.gif")
    t1.shape(f"2048/{board[0][1]}.gif")
    t2.shape(f"2048/{board[0][2]}.gif")
    t3.shape(f"2048/{board[0][3]}.gif")
    t4.shape(f"2048/{board[1][0]}.gif")
    t5.shape(f"2048/{board[1][1]}.gif")
    t6.shape(f"2048/{board[1][2]}.gif")
    t7.shape(f"2048/{board[1][3]}.gif")
    t8.shape(f"2048/{board[2][0]}.gif")
    t9.shape(f"2048/{board[2][1]}.gif")
    t10.shape(f"2048/{board[2][2]}.gif")
    t11.shape(f"2048/{board[2][3]}.gif")
    t12.shape(f"2048/{board[3][0]}.gif")
    t13.shape(f"2048/{board[3][1]}.gif")
    t14.shape(f"2048/{board[3][2]}.gif")
    t15.shape(f"2048/{board[3][3]}.gif")
    scr.update()
def lose():
    global scr, t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, score, hs, updateTXT, resetGame
    t0.hideturtle()
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
    t5.hideturtle()
    t6.hideturtle()
    t7.hideturtle()
    t8.hideturtle()
    t9.hideturtle()
    t10.hideturtle()
    t11.hideturtle()
    t12.hideturtle()
    t13.hideturtle()
    t14.hideturtle()
    t15.hideturtle()
    scr.bgpic("nopic")
    turtle.write("You lose D:", align = "center", font = ["Arial", 50, "normal"])
    turtle.hideturtle()
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor() - 50)
    l = "Score: " + str(score)
    turtle.write(l, align = "center", font = ["Arial", 25, "normal"])
    turtle.goto(turtle.xcor(), turtle.ycor() - 30)
    if hs < score:
        hs = score
    l = "High score: " + str(hs)
    turtle.write(l, align = "center", font = ["Arial", 25, "normal"])
    turtle.goto(turtle.xcor(), turtle.ycor() - 25)
    turtle.write("Press space to close, and re-run the file to play again!", align = "center", font = ["Arial", 10, "normal"])
    resetGame()
def placeRandomTile():
    global av, board, lose, updateAV
    updateAV()
    m = -1
    if len(av) == 0:
        lose()
    else:
        m = av[random.randint(0,len(av) - 1)]
        av.remove(m)
        if random.randint(0,9) == 0:
            p = 4
        else:
            p = 2
        if m < 4:
            board[0][m] = p
        elif m < 8:
            board[1][m - 4] = p
        elif m < 12:
            board[2][m - 8] = p
        else:
            board[3][m - 12] = p
def die():
    global scr
    scr.bye()
def updateAV():
    global av, board
    av = []
    x = 0
    for i in range(4):
        for o in range(4):
            if board[i][o] == 0:
                av.append(x)
                x += 1
def defaultOnMove():
    global updateTXT, placeRandomTile, started, updateIcons
    placeRandomTile()
    started = 1
    updateTXT()
    updateIcons()
def checks(t0, t1, t2, t3, t4, t5, t6, t7):
    global board, score, defaultOnMove
    nt = 0
    if board[t1][t5] != 0:
        if board[t0][t4] == 0:
            board[t0][t4] = board[t1][t5]
            board[t1][t5] = 0
            nt += 1
    if board[t2][t6] != 0:
        if board[t0][t4] == 0:
            board[t0][t4] = board[t2][t6]
            board[t2][t6] = 0
            nt += 1
        elif board[t1][t5] == 0:
            board[t1][t5] = board[t2][t6]
            board[t2][t6] = 0
            nt += 1
    if board[t3][t7] != 0:
        if board[t0][t4] == 0:
            board[t0][t4] = board[t3][t7]
            board[t3][t7] = 0
            nt += 1
        elif board[t1][t5] == 0:
            board[t1][t5] = board[t3][t7]
            board[t3][t7] = 0
            nt += 1
        elif board[t2][t6] == 0:
            board[t2][t6] = board[t3][t7]
            board[t3][t7] = 0
            nt += 1
    if board[t0][t4] == board[t1][t5] and board[t0][t4] != 0:
        board[t0][t4] *= 2
        board[t1][t5] = board[t2][t6]
        board[t2][t6] = board[t3][t7]
        board[t3][t7] = 0
        nt += 1
        score += board[t0][t4]
    if board[t1][t5] == board[t2][t6] and board[t1][t5] != 0:
        board[t1][t5] *= 2
        board[t2][t6] = board[t3][t7]
        board[t3][t7] = 0
        nt += 1
        score += board[t1][t5]
    if board[t2][t6] == board[t3][t7] and board[t2][t6] != 0:
        board[t2][t6] *= 2
        board[t3][t7] = 0
        nt += 1
        score += board[t2][t6]
    if t0 == 3 or t4 == 3:
        if nt != 0:
            defaultOnMove()
def goUp():
    global checks
    for i in range(4):
        checks(0, 1, 2, 3, i, i, i, i)
def goDown():
    global checks
    for i in range(4):
        checks(3, 2, 1, 0, i, i, i, i)
def goLeft():
    global checks
    for i in range(4):
        checks(i, i, i, i, 0, 1, 2, 3)
def goRight():
    global score
    nt = 0
    for i in range(4):
        checks(i, i, i, i, 3, 2, 1, 0)
def newGame():
    global placeRandomTile
    placeRandomTile()
    placeRandomTile()
scr.onkey(goUp, "Up")
scr.onkey(goDown, "Down")
scr.onkey(goLeft, "Left")
scr.onkey(goRight, "Right")
scr.onkey(goUp, "w")
scr.onkey(goDown, "s")
scr.onkey(goRight, "a")
scr.onkey(goLeft, "d")
scr.onkey(die, "space")
scr.listen()
updateFromTXT()
if started == 0:
    newGame()
updateIcons()
scr.mainloop()
