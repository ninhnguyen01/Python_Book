# Introduction to Value-Returning Functions: Generating Random
# Numbers (Title)

# Reading

# Import Statement Example
import math

# Generating Random Numbers (section)
import random

# randit function
number = random.randint (1,100)

# This program displays a random number in the range 1 through 10
import random
def main():
    number = random.randint(1,10)
    print(f'The number is {number}.')

main()

import random
def main():
    for count in range (5):
        number = random.randint(1,10)
        print(number)

main()

print(random.randint(1,10))

import random
def main():
    for count in range (5):
        print(random.randint(1,10))

main()

# Calling Functions from an F String (section)
print(f'The number is {random.randint(1,100)}.')
print(f'{random.randint(0,1000):^10d}')

# This program the rolling of dice.
import random

MIN = 1
MAX = 6

def main():
    again = 'y'
    while again == 'y' or again == 'Y':
        print('Rolling the dice . . .')
        print('Their values are:')
        print(random.randint(MIN,MAX)) 
        print(random.randint(MIN,MAX)) 
        again = input('Roll them again? (y = yes): ')

main()

x = random.randint(1,10) * 2

# This program display 10 tosses of a coin.
import random

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')

main()

# The randrange, random, and uniform Functions (section)
number = random.randrange(10)
number = random.randrange(5,10)
number = random.randrange(0,101,10)

number = random.random()

number = random.uniform(1.0, 10.0)

# Random Number Seeds (section)
random.seed(10)

random.randint(1,100)
random.randint(1,100)
random.randint(1,100)
random.randint(1,100)

# End

# Checkpoint

# 5.21 How does a value-returning function differ from the void 
# functions?
# A: Returns a value back to the statement that called it.

# 5.22 What is a library function?
# A: A prewritten function that performs some commonly needed task.

# 5.23 Why are library functions like "black boxes"?
# A: You can't see the operations being performed.

# 5.24 What does the following statement do?
x = random.randint(1,100)
# A: It assigns a random integer in the range 1 and 100 to the variable
# x.

# 5.25 What does the following statement do?
print(random.randint(1,20))
# A: It prints a random integer in the range of 1 through 20.

# 5.26 What does the following statement do?
print(random.randrange(10,20))
# A: It prints a random integer in the range of 10 through 20.

# 5.27 What does the following statement do?
print(random.random())
# A: It prints a random floating-point number in the range of 0.0
# up to, but not including, 1.0.

# 5.28 What does the following statement do?
print(random.uniform(0.1, 0,5))
# A: It prints a random floating-point number in the range of 0.1
# through 0.5.

# 5.29 When the random module is imported, what does it use as
# a seed value for random number generation?
# A: It uses the system time, retrieved from the computer's internal
# clock.

# 5.30 What happens if the same seed value is always used for 
# generating random numbers? 
# A: The random number functions would always generate the same series
# of pseudorandom numbers.

# End