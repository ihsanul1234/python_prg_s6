import turtle

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Background color
t = turtle.Turtle()
t.pensize(3)
t.speed(5)
t.pencolor("white")  # Text color

# Function to move without drawing
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Function to draw 'A'
def draw_A(x, y):
    move(x, y)
    t.left(75)
    t.forward(50)
    t.right(150)
    t.forward(50)
    t.backward(25)
    t.right(105)
    t.forward(20)
    t.left(105)
    
# Function to draw 'B'
def draw_B(x, y):
    move(x, y)
    t.left(90)
    t.forward(50)
    for _ in range(2):
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)

# Function to draw 'D'
def draw_D(x, y):
    move(x, y)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.circle(-25, 180)

# Function to draw 'U'
def draw_U(x, y):
    move(x, y)
    t.penup()
    t.goto(x, y + 50)
    t.pendown()
    t.right(90)
    t.forward(40)
    t.circle(10, 180)
    t.forward(40)

# Function to draw 'L'
def draw_L(x, y):
    move(x, y)
    t.left(90)
    t.forward(50)
    t.backward(50)
    t.right(90)
    t.forward(30)

# Function to draw 'S'
def draw_S(x, y):
    move(x, y)
    t.forward(25)
    t.backward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)

# Function to draw 'I'
def draw_I(x, y):
    move(x, y)
    t.forward(20)
    t.backward(10)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.backward(20)

# Function to draw 'T'
def draw_T(x, y):
    move(x, y)
    t.forward(30)
    t.backward(15)
    t.right(90)
    t.forward(50)

# Function to draw 'H'
def draw_H(x, y):
    move(x, y)
    t.left(90)
    t.forward(50)
    t.backward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.backward(50)

# Drawing the name "ABDUL BASITH"
draw_A(-300, 100)
draw_B(-250, 100)
draw_D(-200, 100)
draw_U(-150, 100)
draw_L(-100, 100)
draw_B(-50, 100)
draw_A(0, 100)
draw_S(50, 100)
draw_I(100, 100)
draw_T(150, 100)
draw_H(200, 100)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
