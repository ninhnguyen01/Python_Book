# Turtle Graphics: Determining the State of the Turtle (Title)

# Reading

import turtle

# Determining the Turtle's Location (section)

# turtle.xcor =         # Enter a value for xcor and ycor after removing
# turtle.ycor =         # comment 

if turtle.xcor() > 249 or turtle.ycor() > 349:
    turtle.goto(0, 0)

# Determining the Turtle's Heading (section)
turtle.heading() # Enter a value here
if turtle.heading() >= 90 and turtle.heading() <= 270:
    turtle.heading(180)

# Determining Whether the Pen Is Down (section)
turtle.isdown()
if turtle.isdown():
    turtle.penup()
if (not(turtle.isdown)):
    turtle.pendown()

# Determining Whether the Turtle is Visible (section)
turtle.isvisible()
if turtle.isvisible():
    turtle.hideturtle()

# Determining the Current Color  (section)
turtle.pencolor() # Enter a value here
if turtle.pencolor == 'red':
    turtle.pencolor('blue')

turtle.fillcolor() # Enter a value here 
if turtle.fillcolor == 'blue':
    turtle.fillcolor('white')

turtle.bgcolor()
if turtle.fillcolor == 'white':
    turtle.fillcolor('gray')

# Determining the Pen Size (section)
turtle.pensize() # Enter a value here
if turtle.pensize() < 3:
    turtle.pensize(3)

# Determining the Turtle's Animation Speed (section)
turtle.speed() # Enter a value here

if turtle.speed() > 0:
    turtle.speed(0)
if turtle.speed() == 0:
    turtle.pencolor('red')
elif turtle.speed() > 5:
    turtle.pencolor('blue')
else:
    turtle.pencolor('green')

# Hit the Target Game (Spotlight)
import turtle
turtle.showturtle()

# Named constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1 

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

# Setup the window 
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

# Draw the target
turtle.hideturtle
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the Turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = float(input("Enter the project's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if(turtle.xcor() >= TARGET_LLEFT_X and 
   turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and 
   turtle.ycor() >= TARGET_LLEFT_Y and
   turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
   print('Target hit!')
else:
    print('You missed the target.')

# End

# Checkpoint

# 3.22 How do you get the turtle's x and y coordinates?
# A: turtle.xcor and turtle.ycor

# 3.23 How would you determine whether the turtle's pen is up?
# A: not((turtle.isdown))

# 3.24 How do you get the turtle's current heading?
# A. turtle.heading()

# 3.25 How do you determine whether the turtle is visible?
# A: turtle.isvisible

# 3.26 How do you determine the turtle's pen color? How do you determine 
# the current fill color? How do you determine the current background color
# of the turtle's graphic window?
# A: turtle.pencolor() , turtle.fillcolor() , turtle.bgcolor()

# 3.27 How do you determine the current pen size?
# A: turtle.pensize()

# 3.28 How do you determine the turtle's current animation speed?
# A: turle.speed()

# End