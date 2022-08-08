import turtle #gamebase
import time #introduce time to dormamu
import random   #introduce "random efect"
import functions

#values to use more in advance
delay= 0.1 #time variable
score=0 #set sore to start
highScore=0 #set up or higer score
head=turtle.Turtle() #from the module now we can use head as a turtle
mouse=turtle.Turtle() #now we define the other item mouse to be and object too
screen=turtle.Screen()#basically define the screen
board=turtle.Turtle() #create other item for the puntuation
tail=turtle.Turtle() #the tail is here
tailC = [] #creating empty list for the tail container

# creating the screen


screen.title("snake game by Kyle")
screen.bgcolor ("white")
screen.tracer(0) #no updates the screen
screen.setup(width=600, height=600)

#snake head

functions.item(head,0,"square","black",0,0);
head.direction="stop"

#snake mouse boiii(open folder function and use item)
functions.item(mouse,0,"circle","red",0,100);

# board (opens folder functions and use item)
functions.item(board,0,"square","black",0,250);
board.hideturtle() #hide this
board.write("Score: 0  High Score: 0", align="center", font=("timesnewroman", 25, "normal"))

#movements (open folders function and use comands)
functions.goUp(head)
functions.goDown(head)
functions.goLeft(head)
functions.goRight(head)
functions.move(head)

#controls (open functions and use keybindings)
functions.runkeyboard(screen,"w","d","a","d")

#loop

while True:
    screen.update()

    #colisions with the walls
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
     # Hide the list
        for parts in tailC:
            parts.goto(1000, 1000)
        #clear it
        parts.clear()
        #score reset
        score = 0
        #delay reset
        delay = 0.1
        board.clear()
        board.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("timesnewroman", 25, "normal"))
     #colision with the mouse
    if head.distance(mouse) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mouse.goto(x,y)
    #tail
    functions.item1(tail,0,"square","red")
    tailC.append(tail)# add at the end of tail list the item tail
    #short the delay
    delay-=0.001
    #score increase
    score+= 10
    if score>highScore:
        hightScore=score
    
    board.clear()
    board.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("timesnewroman", 25, "normal"))
    # Move the end segments first in reverse order
    for index in range(len(tailC)-1, 0, -1):
        x = tailC[index-1].xcor()
        y = tailC[index-1].ycor()
        tailC[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(tailC) > 0:
        x = head.xcor()
        y = head.ycor()
        tailC[0].goto(x,y)

    functions.move(head);  

    # Check for head collision with the body segments
    for parts in tailC:
        if parts.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for parts in tailC:
                parts.goto(1000, 1000)
        
            # Clear the segments list
            tailC.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            board.clear()
            board.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("timesnewroma", 25, "normal"))

    time.sleep(delay)

wn.mainloop()

