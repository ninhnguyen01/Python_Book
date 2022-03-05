# Writing Your Own Value-Returning Functions (Title)

# Reading

# Value-returning function format 

# def function_name():
#   statement
#   statement
#   etc.
#   return expression

def sum(num1, num2):
    result = num1 + num2
    return result

# This program uses the return value of a function.
def main():
    first_age = int(input('Enter your age: '))
    second_age = int(input("Enter your best friends's age: "))
    total = sum(first_age, second_age)
    print(f'Together you are {total} years old.')

def sum(num1, num2):
    result = num1 + num2
    return result

main()

# Another option 
def sum(num1, num2):
    return num1 + num2

# How to Use Value-Returning Functions
# This program calculates a retail item's sale price.

DISCOUNT_PERCENTAGE = 0.20

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print(f'The sale price is ${sale_price:,.2f}.')

def get_regular_price():  
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()

# Using IPO Charts
# This program calculates a sales person's pay at Make Your 
# Own Music.
def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)

    pay = sales * comm_rate - advanced_pay
    print(f'The pay is ${pay:,.2f}.')

    if pay < 0:
        print('The salesperson must reimburse') 
        print('the company.')

def get_sales():
    monthly_sales = float(input('Enter the monthly sales: '))
    return monthly_sales

def get_advanced_pay():
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    advanced = float(input('Advanced pay: '))
    return advanced

main()

def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000.00 and sales <= 14999.99:
        rate = 0.12
    elif sales > 15000.00 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000.00 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18
    return rate 

# Returning Strings (section)
def get_name():
    name = input('Enter your name: ')
    return name

def dollar_format(value):
    return f'${value:,.2f}'

# Returning Boolean Values (section)
number = int(input('Enter a number: '))
if (number % 2 ) == 0:
    print('The number is even.')
else:
    print('The number is odd.')

# Revision
def is_even(number):
    if (number % 2) == 0:
        status = True
    else:
        status = False

number = int(input('Enter a number: '))
if is_even(number):
    print('The number is even.')
else:
    print('The number is odd.')

# Using Boolean Functions in Validation Code
model = int(input('Enter the model number: '))

while model != 100 and model != 200 and model != 300:
    print('The valid model numbers are 100, 200 and 300.')
    model = int(input('Enter a valid model number: '))

# Revision
def is_invalid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num!= 300:
        status = True
    else:
        status = False
    return status

while is_invalid(model):
    print('The valid model numbers are 100, 200 and 300.')
    model = int(input('Enter a valid model number: '))


# Returning Multiple Values (section)
# General format
# return expression1, expression2, etc.

def get_name():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    return first, last

first_name, last_name = get_name()

# Returning NONE from a function
def divide(num1, num2):
    if num2 == 0:
        result = None
    else:
        result = num1 /num2
    return result

# This program demonstrates the 'None' keyword.
def main():
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    quotient = divide(num1,num2)

    if quotient is None:
        print('Cannot divide by zero.')
    else:
        print(f'{num1} divided by {num2} is {quotient}.')

def divide(num1,num2):
    if num2 == 0:
        result = None
    else:
        result = num1 / num2
    return result

main()

# End

# Checkpoint

# 5.31 What is the purpose of the return statement in a function?
# A: It returns a value back to the part of the program that called 
# it. 

# 5.32 Look at the following function definition:

def do_something(number):
    return number * 2

# a What is the name of the function?
# A: do_something

# b. What does the function do?
# A: It returns a value that is twice the argument passed to it. 

# c. Given the function definition, what 
# will the following statement display?
print(do_something(10))
# A: 20

# 5.33 What is a Boolean function?
# A: A function that returns either True or False.

# End