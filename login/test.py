from asyncore import loop
from tkinter.messagebox import YES
import turtle
import random
import string



wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("LogInLand")

class screen():
    wnn = turtle.Screen()
    wnn.bgcolor("light blue")
    wnn.title("LogInLandSnake")

class Player:
  def __init__(self, name, password, distance):
    self.name = name
    self.password = password
    self.distance = distance

p1 = Player("Unknown", "none", 0)

user = turtle.Turtle()
user.shape("square")
user.color("black")

image = "E:\midterm\login\Squirrel.gif"
wn.addshape(image)
user.shape(image)


check = turtle.Turtle()
check.shape("square")
check.color("blue")
check.penup()
check.setposition(100, 100)



#check if there is a collision between turtles
def collision(a, b):
    col = False
    if (abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10):
        col = True
    return col

#user movementw
def up():
    y = user.ycor()
    y += 5
    user.sety(y)

def down():
    y = user.ycor()
    y -= 5
    user.sety(y)

def left():
    x = user.xcor()
    x -= 5
    user.setx(x)

def right():
    x = user.xcor()
    x += 5
    user.setx(x)


wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(right, "d")
wn.onkeypress(left, "a")

#counter
input= "nnn"

#test


# BEGIN SNAKE -------------+---+--+-----------+++--------+--+--+--

#moves pointer to next
counterEnterB = 0

def snake():
    print("helloSEEEEEEEMEEEEEEEEEEEEEEHEREEEEEEEEEEE")
    pointer.setposition(x, y)


# code for random coodinates
x = random.randint(-300, 300)
y = random.randint(-300, 300)
print(x, y)

# Generate random characters for spawn

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}{|:"<>?-=[];1234567890'
a = random.choice(characters)
print(a)

# turtle that moves to the next letter
pointer = turtle.Turtle()
pointer.penup()
pointer.write(a)
print(pointer.xcor(), "POINTER")
pointer.setposition(x, y)

# the pointer moves to another random position. 
# the coutner is on 1 because the user didn't hit the counter yet.
# if the user hits the counter, the counter turns to 0, 
# the letter is added to the password
# if the counter is 1, the pointer is static, if it's 0, the pointer moves.
# when the pointer reaches the new set position, the counter is 1 again  
counter = 1


# Password Creation

password = ""

# if the user hits the turtle text, the text is appended to the password.



# because the turtle only moves after the user hit it, the pass is increased. 
# then the turtle moves to another place and the user will go again.
# the game stops when the user goes back to the 2nd checkpoint
# exit program and print the name and username


# END SNAKE -------------+---+--+-----------+++--------+--+--+--

# --- Main function with the main loop


    #dubegging collision
while True:
        wn.listen()
        wn.update()
        
        a = random.choice(characters)
        #debugging to see if the random function works
        print(a)
        print(p1.name)
        print(p1.distance)

        #user collides with the checkpoint
        if collision(user, check): 
            print("collided") 
            check.color("red")
            screen().wnn = turtle.Screen()
            wn.onkeypress(snake, "g")
            if(input == "nnn"):
                input = turtle.textinput("title", "promt")
                p1.name = input #set name of user through the input after checkpoint a has been hit
        else:
            check.color("blue")

        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        
        counter = 1
        if collision(user, pointer): 

            password = password + a
            print("hit", password)
            pointer.color("red")
            counter = 0
            if(counter == 0):
                pointer.setposition(y, x)
            
        else:
            pointer.color("blue")






