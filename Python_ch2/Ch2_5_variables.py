# Variables (Title)

# Reading 

# Variable = Expression
width = 10
length = 5

print(width)
print(length)

print('width')
print(width)

# This program demonstrates a variable.
room = 503 
print('I am staying in room number')
print(room)

# Create two variables: top_speed and distance.
top_speed = 160
distance = 300
 
# Display the values referenced by the variables.
print('The top speed is') 
print(top_speed)
print('The distance traveled is')
print(distance)

# Variable Naming Rules (section)

# 1 Python keywords (no)
# 2 Variable name (no spaces)
# 3 1st character only a to z, A to Z, or underscore (_)
# 4 AFTER FIRST CHARACTER a to z, A to Z, 0 to 9, or underscore (_)
# Uppercase and lowercase characters are distinct.

# Displaying Multiple Items with the print Function
# This program demonstrates a variable.
room = 503
print('I am staying in room number', room)

# Variable Reassignment (section)
# This program demonstrates program reassignment.
dollars = 2.75
print('I have', dollars, 'in my account.')
dollars = 99.95
print('But now I have', dollars, 'in my account!' )

# Numeric Data Types and Literals
type(1)
type(1.0)

# WARNING
# You can't write currency symbols, spaces or commas in numeric literals.
# Value = $4,567.99 Error!

# Store Strings with the str Data type 

# creat variables to reference two strings.
first_name = 'Kathyrn'
last_name = 'Marino'
print(first_name, last_name)

# Reassigning a Variable to a Different Type 
x = 99
print(x)
x = 'Take me to your leader'
print(x)

# End

# Checkpoint

# 2.10 What is a variable?
# A: A name that represents a value in the computer's memory.

# 2.11 Which of the following are illegal variable names in Python, 
# and why?
# x
# 99 bottles - illegal b/c it begins with a number
# july2009
# theSalesFigureForFiscalyear
# r&d - illegal b/c the character & is not allowed
# grade_report

# 2.12 Is the variable name 'Sales' the same as 'sales'? Why or why not?
# A: No b/c variable names are case-sensitive

# 2.13 Is the following statement valid or invalid? If it is invalid, why?
# 72 = amount
# A: Invalid because the variable 'amount' should be left of the operator

# 2.14 What will the following code display?
# val = 99
# print('The value is ', 'val')
# A: The values is val
val = 99
print('The values is', 'val') 

# 2.15 Look at the following assignment statements:
value1 = 99
value2 = 45.9
value3 = 7.0
value4 = 7
value5 = 'abc'

# int
# float
# float
# int
# str

# 2.16 What will be displayed by the following program?
my_value = 99
my_value = 0
print(my_value)
# A: 0

# End