# import turtle package
import turtle
import random
import string


# Graphic screen
class screen():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("LogInLand")

#player
class Player:
  def __init__(self, name, password, distance):
    self.name = name
    self.password = password
    self.distance = distance

#initialize first player
p1 = Player("Unknown", "", 0)

#user trace
user = turtle.Turtle()
user.shape("circle")
user.color("black")
user.penup()

background = "E:\midterm\login\ground.gif"
image = "E:\midterm\login\dog.gif"
ima = "E:\midterm\login\d.gif"
imb = "E:\midterm\login\emerald.gif"
imc = "E:\midterm\login\exit.gif"
food = "E:\midterm\login\carrot.gif"
screen().wn.addshape(image)
screen().wn.addshape(food)
screen().wn.addshape(ima)
screen().wn.addshape(imb)
screen().wn.addshape(imc)
screen().wn.bgpic(background)
user.shape(image)


#first checkpoint
checkpointa = turtle.Turtle()
checkpointa.shape("square")
checkpointa.color("green")
checkpointa.penup()
checkpointa.setposition(100, 100)
checkpointa.shape(ima)

#second checkpoint
checkpointb = turtle.Turtle()
checkpointb.shape("square")
checkpointb.color("gold")
checkpointb.penup()
checkpointb.setposition(-200, -300)
checkpointb.shape(imb)

#third checkpoint
checkpointc = turtle.Turtle()
checkpointc.shape("square")
checkpointc.color("purple")
checkpointc.penup()
checkpointc.setposition(400, 200)
checkpointc.shape(imc)



# Collision of objects function
def collision(a, b):
    col = False
    if (abs(a.xcor() - b.xcor()) < 50 and abs(a.ycor() - b.ycor()) < 50):
        col = True
    return col

# Directions of Movement
def up():
    y = user.ycor()
    y += 10
    user.sety(y)
    p1.distance += 10


def down():
    y = user.ycor()
    y -= 10
    user.sety(y)
    p1.distance += 10


def left():
    x = user.xcor()
    x -= 10
    user.setx(x)
    p1.distance += 10


def right():
    x = user.xcor()
    x += 10
    user.setx(x)
    p1.distance += 10
# This code is contributed
# by Deepanshu Rustagi.

# # BEGIN SNAKE -------------+---+--+-----------+++--------+--+--+--

#moves pointer to next letter
def snake():
    print("You can start eating carrots")
    pointer.setposition(x, y)

# code for random spawning of letters for password
x = random.randint(-300, 300)
y = random.randint(-300, 300)
print(x, y)

# Generate random characters for spawn

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}{|:"<>?-=[];1234567890'
a = random.choice(characters)

# turtle that moves to the next letter
pointer = turtle.Turtle()
pointer.penup()
print(pointer.xcor(), "POINTER")
pointer.setposition(x, y)
pointer.shape(food)



# if the user hits the turtle text, the text is appended to the password.

if collision(user, pointer): 
    print("hit")

# because the turtle only moves after the user hit it, the pass is increased. 
# then the turtle moves to another place and the user will go again.
# the game stops when the user goes back to the 2nd checkpoint
# exit program and print the name and username

def exit():
    print("name: ", p1.name, "\npassword: ", p1.password, "\nHow much did you run: ", p1.distance)
    turtle.bye()

# END SNAKE -------------+---+--+-----------+++--------+--+--+--



# --- Main function with the main loop
def main():
    
    screen()
    screen.wn.onkeypress(up, "w")
    screen.wn.onkeypress(down, "s")
    screen.wn.onkeypress(right, "d")
    screen.wn.onkeypress(left, "a")

    if collision(user, checkpointb): 
        print("PRESS G TO EAT CARROTS") 

    #counterB
    cC = 0
    cB = 0

    #initialize input to be accessed only once
    input= "nnn"

    #update screen
    
    while True:
        
        screen.wn.update()
        screen.wn.listen()

        # generate New Character every time
        a = random.choice(characters)

        # COnstantly generate new coordingates
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)

        #--- actions for collisions
        # A checkpoint, introduce username
        if collision(user, checkpointa): 
            checkpointa.color("red")
            checkpointb.circle(5)
            if(input == "nnn"):
                input = turtle.textinput("Username", "type your name")
                p1.name = input
        else:
            checkpointa.color("blue")

        # B checkpoint, play snake for password
        if collision(user, checkpointb): 
            checkpointb.color("red")
            if(cC == 0):
                checkpointc.circle(5)
            print("Press G until text appears")
            if(screen().wn.onkeypress(snake, "g")):
                print("You can start eating carrots")
            cB = 1
            if(cB == 1):
                pointer.circle(5)
        else:
            checkpointb.color("blue")

        #C checkpoint, exit porgram and create profile
        if collision(user, checkpointc): 
            checkpointc.color("red")
            if(cC > 10):
                exit()
            else:
                print("Ypur need to eat more")
        else:
            checkpointc.color("blue")

        # Snake pointer letter. 
        
        if(cB == 1):
            if collision(user, pointer): 
                p1.password = p1.password + a
                pointer.color("red")
                counter = 0
                if(counter == 0):
                    pointer.setposition(y, x)
                cC += 1
            else:
                pointer.color("blue")
        
        #the methods and the objects need to be outside of the loop otherwise they will get created every second
main()
