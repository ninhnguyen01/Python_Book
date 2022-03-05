# Passing Arguments to Functions (Title)

# Reading

# This Program demonstrates an argument being passed to a function.
def main():
    value = 5
    show_double(value)

# The show_double function accepts an argument and displays double
# its value.
def show_double(number):
    result = number * 2
    print(result)

main()

show_double(50)

# Parameter Variable Scope (section)
# This program converts cups to fluid ounces
def main():
    intro()
    cups_needed = int(input('Enter the number of cups: '))
    cups_to_ounces(cups_needed)
def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces. For your')
    print('reference the formula is:')
    print(' 1 cup = 8 fluid ounces')
    print()
def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'That converts to {ounces} ounces.')

main()

# Passing Multiple Arguments (section)
# This program demonstrates a function that accepts two arguments.

def main():
    print('The sume of 12 and 45 is')
    show_sum(12,45)
def show_sum(num1,num2):
    result = num1 + num2
    print(result)

main()

# This program demonstrates passing two string arguments to a
# function.
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name,last_name)

def reverse_name (first, last):
    print(last, first)

main()

# Making Changes to Parameters (section)
def main():
    value = 99
    print(f' The value is {value}.')
    change_me(value)
    print(f' Back in main the value is {value}.')

def change_me(arg):
    print('I am changing the value.')
    arg = 0
    print(f'Now the value is {arg}.')

main()

# Keyword Arguments (section) 
# parameter_name = value
# This Program demonstrates keyword arguments.
def main():
    show_interest(rate=0.01, periods= 10, principal = 10000.0)
def show_interest (principal, rate, periods):
    interest = principal * rate * periods
    print(f'The simple interest will be ${interest:,.2f}.')

main()

# This program demonstrates passing two strings as keyword 
# arguments to a function.
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(last=last_name, first=first_name)

def reverse_name (first, last):
    print(last, first)

main()

# Mixing Keyword Arguments with Positional Arguments (section)
show_interest(10000.0, rate = 0.01, periods=10)

# This will cause an error!
# show_interest(1000.0, rate = 0.01, 10)

# End

# Checkpoint

# 5.13 What are the pieces of data that are passed into a function 
# called?
# A: Arguments.

# 5.14 What are the variables that receive pieces of data in a 
# function called?
# A: Parameters.

# 5.15 What is a parameter variable's scope?
# A: The entire function in which the parameter is declared.

# 5.16 When a parameter is changed, does this affect the argument
# that was passed into the parameter?
# No, it does not.

# 5.17 The following statements call a function named show_data.
# Which of the statements passes arguments by position, and which passes
# keyword arguments?

# a. show_data('name = Kathryn', age = 25)
# A: Passes by keyword argument

# b. show_data('Kathyrn', 25)
# A: Passed by position

# End