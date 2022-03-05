# Turtle Graphics: Using Loops to Draw Designs (Title)

# Reading 

# Square
import turtle

turtle.showturtle()

for x in range (4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()

# Octagon
import turtle
turtle.showturtle()

for x in range (8):
    turtle.forward(100)
    turtle.right(45)

turtle.done()

# Concentric Circles
import turtle
turtle.showturtle()
# Named Constants
NUM_CIRCLES = 20
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0
# Setup the turtle.
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()
# Set the radius of the first circle.
radius = STARTING_RADIUS
# Draw the circles.
for count in range (NUM_CIRCLES):
    # Draw the circle.
    turtle.circle(radius)
    # Get the coordinates for the next circle.
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET
    # Calculate the radius for the next circle.
    radius = radius + OFFSET
    # Position the turtle for the next circle.
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.done()

# This program draws a design using repeated circles.
import turtle
turtle.showturtle()
# Named constants
NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0
# Set the animation Speed.
turtle.speed(ANIMATION_SPEED)
# Draw 36 circles, with the turtle tilted by 10 degrees after
# each circle is drawn.
for x in range (NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()

# This program draws a design using repeated lines.
import turtle
turtle.showturtle()
# Named Constants
START_X = -200
START_Y = 0
NUM_LINES = 36
LINE_LENGTH = 400
ANGLE = 170
ANIMATION_SPEED = 0
# Move the turtle to its initial position.
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X,START_Y)
turtle.pendown()
# Set the animation speed.
turtle.speed(ANIMATION_SPEED)
# Draw 36 lines with the turtle tilted by 170 degrees after each
# line is drawn.
for x in range (NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)

turtle.done()

# End