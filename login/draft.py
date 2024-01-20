import turtle

class player:
    name = "Unknown"
    password = "Unkown"
    journey = 0
    u = turtle.Turtle()
    u.shape("square")
    u.color("red")
    
    def up():
        y = player.u.ycor()
        y += 5
        player.u.sety(y)

    def down():
        y = player.u.ycor()
        y -= 5
        player.u.sety(y)

    def left():
        x = player.u.xcor()
        x -= 5
        player.u.setx(x)

    def right():
        x = player.u.xcor()
        x += 5
        player.u.setx(x)



user = turtle.Turtle()
user.shape("square")
user.color("black")