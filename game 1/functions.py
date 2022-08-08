import turtle

def runkeyboard(inicial,up,down,left,right):
    inicial.listen()
    inicial.onkeypress(goUp, up)
    inicial.onkeypress(goDown, down)
    inicial.onkeypress(goLeft, left)
    inicial.onkeypress(goRight, right)
    return  #run the function idiot

def item(name,speed,shape,color,g1,g2):
    name.speed(speed)
    name.shape(shape)
    name.color(color)
    name.penup()
    name.goto(g1,g2)
    return
def item1(name,speed,shape,color):
    name.speed(speed)
    name.shape(shape)
    name.color(color)
    name.penup()
    return

def goUp(name):
    if name.direction != "down":
        name.direction = "up"
    return

def goDown(name):
    if name.direction != "up":
        name.direction = "down"
    return
def goLeft(name):
    if name.direction != "right":
        name.direction = "left"
    return
def goRight(name):
    if name.direction != "left":
        name.direction = "right"
    return
def move(name):
    if name.direction == "up":
        y = name.ycor()
        name.sety(y + 20)
    
    if name.direction == "down":
        y = name.ycor()
        name.sety(y - 20)

    if name.direction == "left":
        x = name.xcor()
        name.setx(x - 20)

    if name.direction == "right":
        x = name.xcor()
        name.setx(x + 20) 
    return