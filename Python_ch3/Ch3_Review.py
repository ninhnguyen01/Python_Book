# Review Questions (Title)

# Algorithm Workbench

# 1
x = 99

if x > 100:
    y = 20
    z = 40
    print(y)
    print(z)

# 2
a = 9
if a < 10:
    b = 0
    c = 1
    print(b)
    print(c)

# 3
a = 11

if a < 10:
    b = 0
else:
    b = 99
    print(b)

# 4 

# if score >= A_score:
#     print('Your grade is A.')
#     else:
#         if score >= B_score:
#             print('Your grade is B.')
#             else:
#                 if score >= C_Score:
#                     print('Your grade is C.')
#                     else:
#                         if score >= D_score:
#                             print('Your grade is D.')
#                             else:
#                                 print('Your grade is F.')

# 5
amount1 = 11
amount2 = 66        # Execute order 66! (Star Wars Reference)

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1)
    else:
        print(amount2)

# 6
speed = 45
if speed >= 24 and speed <= 56:
    print('Speed is normal')
else:
    print('Speed is abnormal')

# 7
points = 45
if points <= 9 or points >= 51:
    print("Invalid points.")
else:
    print("Valid points.")

# 8
import turtle

turtle.showturtle()
turtle.setheading(40)
turtle.isdown()

if turtle.heading() >= 0 and turtle.heading() <= 45:
    turtle.penup()

turtle.isdown()

# 9
import turtle

turtle.showturtle()
turtle.pencolor('red')

if turtle.pencolor() == 'red' or 'blue':
    turtle.pensize(5)

# 10 
import turtle
turtle.showturtle()