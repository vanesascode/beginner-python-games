import turtle

# One player vs Computer:

wn = turtle.Screen()
wn.title("Pong by vanesascode")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# The "tracer()" method is used to control the animation of the turtle window. - The parameter "0" passed to the method turns off the animation.  - This means that any turtle movement or drawing will be displayed instantly on the screen, without any delay or animation effect.  - This can be useful for faster rendering of complex graphics or for creating static images.

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = (
    turtle.Turtle()
)  # 1. "turtle" is a built-in Python module that provides a graphics environment for creating shapes and animations. 2. "Turtle()" is a constructor method of the turtle module that creates a new turtle object. 3. The line of code assigns the new turtle object to a variable named "paddle_a". This variable can then be used to manipulate the turtle object, such as changing its position, size, and color.
paddle_a.speed(
    0
)  # The speed of animation. It sets the speed to the maximum possible speed.
paddle_a.shape("square")  # by default 20px by 20xp
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()  # it won't draw any lines when the object moves
paddle_b.goto(+350, 0)

# Balls

ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("green")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.2  # maybe you need to move the value for your computer's speed
ball1.dy = -0.2
# dx= horizontal speed/ dy= vertical speed - every time our ball moves it moves by two pixels so since X is positive it's going to move to the right - and since Y is positive it's going to move up


ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("yellow")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.2
ball2.dy = -0.2

ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("blue")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = -0.3
ball3.dy = 0.2

ball4 = turtle.Turtle()
ball4.speed(0)
ball4.shape("square")
ball4.color("red")
ball4.penup()
ball4.goto(0, 0)
ball4.dx = 0.1
ball4.dy = -0.2

balls = [ball1, ball2, ball3, ball4]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player: 0 Computer: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()  # it returns the y coordinate and we assign it to "y"
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # it tells the program to listen for keyboard input
wn.onkeypress(
    paddle_a_up, "w"
)  # when player pressed "W" the function "paddle_a_up" is called.
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop:
while True:
    wn.update()  # every time the loop runs, it updates the screen.

    for ball in balls:
        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # everytime there is a loop, we get the position of the ball (ycor/xcor) and set it (setx/sety) two pixels horizontal and vertically

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  # it turns the number negative - it reverses the direction

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()  # This clears the screen so the score doesn't rewrite on itself
            pen.write(
                f"Player: {score_a} Computer: {score_b}",
                align="center",
                font=("Courier", 24, "normal"),
            )

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write(
                "Player: {} Computer: {}".format(score_a, score_b),
                align="center",
                font=("Courier", 24, "normal"),
            )

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50
        ):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50
        ):
            ball.setx(-340)
            ball.dx *= -1
