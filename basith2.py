import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Function to draw a circle
def draw_circle(color, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw turtle body and head
draw_circle("green", 0, 0, 50)  # Body
draw_circle("green", 0, 80, 25)  # Head

# Draw legs
draw_circle("green", -60, 40, 20)  # Left Front Leg
draw_circle("green", 60, 40, 20)   # Right Front Leg
draw_circle("green", -60, -40, 20) # Left Back Leg
draw_circle("green", 60, -40, 20)  # Right Back Leg

# Draw tail
draw_circle("green", 0, -60, 15)  # Tail

# Draw eyes
draw_circle("white", -10, 90, 5)  # Left Eye
draw_circle("white", 10, 90, 5)   # Right Eye

t.hideturtle()
turtle.done()
