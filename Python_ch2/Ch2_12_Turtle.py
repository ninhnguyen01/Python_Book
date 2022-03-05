# Introduction to Turtle Graphics (Title)

# Reading 

import turtle
turtle.showturtle()

import turtle
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

import turtle
turtle.forward(100)
turtle.left(120)
turtle.forward(150)

import turtle
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(50)

import turtle
turtle.forward(50) 
turtle.setheading(90) # Turtle's heading
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(100)

import turtle
turtle.setheading()
turtle.setheading(180)
turtle.heading()

import turtle
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.penup()
turtle.forward(50)

import turtle
turtle.circle(100) # drawing circle

import turtle
turtle.dot() # drawing dot
turtle.forward(50)
turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)

import turtle
turtle.pensize(5) #pensize
turtle.circle(100)

import turtle
turtle.pencolor('red')
turtle.circle(100)

import turtle
turtle.bgcolor('gray') # background color
turtle.pencolor('red')
turtle.circle(100)

# Three turtle reset command (section)
# turtle.reset
# turtle.clear()
# turtle.clearscreen()

# graphic window size 
# turtle.setup(width,height)
import turtle
turtle.setup(640,480) 

import turtle
turtle.goto(0,100)
turtle.goto(-100,0)
turtle.goto(0,0)

import turtle
turtle.goto(100,150)
turtle.pos() # turtle current position

import turtle
turtle.goto(100,150)
turtle.xcor() # x-coordinate
turtle.ycor() # y-coordinate

import turtle
turtle.speed(0) # turtle animation speed (instant)
turtle.circle(100)

import turtle
turtle.speed(1) # turtle animation speed (slow)
turtle.circle(100)

import turtle
turtle.speed() # turtle current speed

turtle.hideturtle()
turtle.showturtle()

import turtle
turtle.write('Hello World') # turtle write 

import turtle
turtle.setup(300.300)
turtle.penup()
turtle.hideturtle()
turtle.goto(-120,120)
turtle.write("Top Left")
turtle.goto(70,-120)
turtle.write("Bottom Right")

import turtle
turtle.hideturtle() 
turtle.begin_fill() # filling shapes
turtle.circle(100)
turtle.end_fill()


import turtle
turtle.hideturtle()
turtle.fillcolor('red') # change fill color 
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# drawing blue square
import turtle
turtle.hideturtle()
turtle.fillcolor('blue') 
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

# not enclose but shape filled like drawn line
import turtle
turtle.hideturtle
turtle.begin_fill() 
turtle.goto(120,120)
turtle.goto(200,-100)
turtle.end_fill()

# General format of a 'turtle.numinput' command (section)
# variable = turtle.numinput(title, prompt)
import turtle
radius = turtle.numinput('Input needed' , 'Enter the radius of a circle')
turtle.circle(radius)

# Three optional arguments for 'turtle.numinput' command
# variable = numinput('Title, prompt, default=x, minval= y, max val = z)
num = turtle.numinput('Input needed', 'Enter a value in the range 1-10' ,
default = 5, minval = 1, maxval = 10)

# String Input with 'turtle.textinput' command
# variable = turtle.textinput(title, prompt)
import turtle
name = turtle.textinput('Input needed' , 'Enter your name')
print(name)

# Constellation Example
# Named constants (to keep track of coordinates)
# Set graphics window to (500,600)
# Peusdocode
    # draw dots
    # display stars
    # display names
    # display lines

# LEFT_SHOULDER_X = -70 # Betelgeuse
# LEFT_SHOULDER_Y = 200 

# RIGHT_SHOULDER_X = 80 # Meissa
# RIGHT_SHOULDER_Y = 180

# LEFT_BELTSTAR_X = -40 # Alnitak
# LEFT_BELTSTAR_Y = 20

# MIDDLE_BELTSTAR_X = 0 # Alnilam
# MIDDLE_BELTSTAR_Y = 0

# RIGHTBELTSTAR_X = 40 # Mintaka
# RIGHTBELTSTAR_Y = 20

# LEFT_KNEE_X = -90 # Saiph
# LEFT_KNEE_Y = -180

# RIGHT_KNEE_X = 120 # Rigel
# RIGHT_KNEE_Y = -140

# This program draws the stars of the Orion Constellation,
# the names of the stars and the constellation lines.

import turtle
# set the window size.
turtle.setup(500,600)

# setup the turtle.
turtle.penup()
turtle.hideturtle()

# Create named constants for the star coordinates.
LEFT_SHOULDER_X = -70 # Betelgeuse
LEFT_SHOULDER_Y = 200 

RIGHT_SHOULDER_X = 80 # Meissa
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40 # Alnitak
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0 # Alnilam
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40 # Mintaka
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90 # Saiph
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120 # Rigel
RIGHT_KNEE_Y = -140

# Draw the stars.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()

# Display the star names.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('Betelgeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('Rigel')

# Draw the lines.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

turtle.done()

# End

# Checkpoint

# 2.42 What is the turtle's default heading when it first appears?
# A: 0 Degrees

# 2.43 How do you move the turtle forward?
# A: turtle.forward

# 2.44 How would you turn the turtle right by 45 degrees?
# A: turtle.right(45)

# 2.45 How would you move the turtle to a new location without 
# drawing a line?
# A: turtle.penup

# 2.46 What command would you use to display the turtle's current 
# heading?
# turtle.heading()

# 2.47 What command would you use to draw a circle with a radius of
# 100 pixels?
# A: turtle.circle(100)

# 2.48 What command would you use to change the turtle's pen size to 8
# pixels?
# A: turtle.pensize(8)

# 2.49 What command would you use to change the turtle's drawing color
# to blue?
# A: turtle.pencolor('blue')

# 2.50 What command would you use to change the background color
# of the turtle's graphic window to black?
# A: turtle.bgcolor('black')

# 2.51 What command would you use to change to set the size of the 
# turtle's graphics window to 500 pixels wide by 200 pixels high
# A: turtle.setup(500,200)

# 2.52 What command would you use to move the turtle to the location 
# turtle.goto(100,50)? 
# A: turtle.setposition

# 2.53 What command would you use to display the coordinates of the 
# turtle's current position?
# A: turtle.pos

# 2.54 Which of the following commands will make the animation speed 
# faster? turtle.speed(1) or turtle.speed(10)
# A: turtle.speed(10)

# 2.55 What command would you use to disable the turtle's animation?
# A: turtle.speed(0)

# 2.56 Describe how to draw a shaped that is filled with color.
# using turtle.begin_fill before drawing shape and then turtle.end_fill 
# after the shape is drawn.

# 2.58 Write a turtle graphics statement that displays a dialog box that
# gets a number from the user. The text Enter a Value should appear in 
# the dialog box's title bar. The dialog box should display the prompt 
# What is the radius of the circle?. The value that the users enter into 
# the dialog box should be assigned to a variable named radius.

import turtle
radius = turtle.numinput('Enter a Value' , 
'What is the radius of the circle? ')

# End