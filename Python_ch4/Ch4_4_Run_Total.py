# Calculating a Running Total (Title)

# Reading

# This program calculates the sum of a series of numbers entered by
# the user.

MAX = 5

# Intialized an accumulator variable.

total = 0.0

# Explain what we are doing.

print('This program calculates the sum of ', end = '')
print('f{MAX} numbers you will enter.')

# Get the numbers and accumulate them.

for counter in range(MAX): 
    number = int(input('Enter a number: '))
    total = total + number 

# Display the total of the numbers.

print(f'The total is {total}.')

# The Augmented Assignment Operators (section)
#  Example +=

# End

# Checkpoint

# 4.13 What is an accumulator?
# A: A variable that is used to accumulate the total 
# of a series of numbers. 

# 4.14 Should an accumulator be initialized to any specific value?
# Why or why not?
# A: The accumulator should be initialized to a 0 or else it will
# not contain the correct total of numbers when the loop ends.

# 4.15 What will the following code display?

total = 0
for count in range (1,6):
    total = total + count
print(total)

# A: 15

# 4.16 What will the following code display?

number1 = 10
number2 = 5
number1 = number1 + number2
print(number1)
print(number2)

# A: 15, 5

# 4.17 Rewrite the following statements using augmented assignment 
# operators:

# a. quantity += 1
# b. days_left -= 5
# c. price *= 10
# d. price /= 2

# End
