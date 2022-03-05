# The math Module (Title)

# Reading

# This program demonstrates the sqrt function. (section)
import math

def main():
    number = float(input('Enter a number: '))
    square_root = math.sqrt(number)
    print(f'The square root of {number} is {square_root}.')

main()

# This program calculates the length of a right triangle's
# hypotenuse. (section)
import math

def main():
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))
    c = math.hypot(a, b)

    print(f'The length of the hypotenuse is {c}.')

main()

# The math.pi and math.e Values

# area = math.pi * radius**2

# End

# Checkpoint

# 5.34 What import statement do you need to write in a program that
# uses the math module?
# A: import math

# 5.35 Write a statement that uses a math module function to get
# the square root of 100 and assigns it to a variable.
# A: square_root = math.sqrt(100)

# 5.36 Wrtie a statement that uses a math module function to 
# convert 45 degrees to radians and assigns the value to a
# variable.
# A: angle = math.radians(45)

# End