# replace place in grid based on input
def grid(a, b):
    for i in range(1, 10):
        for j in range(1, 10):
            if(i==a):
                if(j == b):
                    print("*", end=" ")
            while not(i==a and j==b):
                print("#", end=" ")
                break
        print("\n", end="")

#----------------------------------------------------
import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("LogInLand")

#player class with constructor (DO IT)
class player:
    def __init__(self) -> None:
        self.u = turtle.Turtle()
        pass
    name = "Unknown"
    password = "Unkown"
    journey = 0
    self = turtle.Turtle()
    self.shape("square")
    self.color("red")
    y = self.ycor()
    x = self.xcor()
    
    def up():
        y = player.self.ycor()
        y += 5
        player.self.sety(y)

    def down():
        y = player.self.ycor()
        y -= 5
        player.self.sety(y)

    def left():
        x = player.self.xcor()
        x -= 5
        player.self.setx(x)

    def right():
        x = player.self.xcor()
        x += 5
        player.self.setx(x)

    up(y)
    down(y)
    left(x)
    right(x)



user = turtle.Turtle()
user.shape("square")
user.color("black")
user.forward(100)
user.speed(0)
    
check = turtle.Turtle()
check.setposition(100, 100)
check.shape("square")
check.color("blue")
check.penup()


#check if there is a collision between turtles
def collision(a, b):
    col = False
    if (abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10):
        col = True
    return col

#user movement

p1 = player()

wn.listen()
wn.onkeypress(p1.up(), "w")
wn.onkeypress(p1.down(), "s")
wn.onkeypress(p1.right(), "d")
wn.onkeypress(p1.left(), "a")


    

while True:
    wn.update()
    print(p1.xcor())

    p1
    #dubegging collision
    if collision(user, check): 
        print("collided") 
        check.color("red")
    else:
        check.color("blue")

#-----------------------------------------------------

if collision(user, checkpointa):
    print("collided")
    checkpointa.color("red")
else:
    checkpointa.color("blue")
    
#hit password
if collision(user, checkpointb):
    print("collided")
    checkpointb.color("red")
else:
    checkpointb.color("blue")

#hit submit
if collision(user, checkpointc):
    print("collided")
    checkpointc.color("red")
else:
    checkpointc.color("blue")


#--------------------------------------------

import random

#--------------------

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}{|:"<>?-=[];1234567890'
a = random.choice(characters)
print(a)
