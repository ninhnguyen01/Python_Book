# Global Variables and Global Constants (Title)

# Reading

# Create a Global Variable.
my_value = 10

def show_value():
    print(my_value)

show_value()

# Creat a Global Variable.
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.')

main() 

# Global Constants (section)
# The following is used as a global constant to represent 
# the contribution rate.

CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f'Contribution for gross pay ${contrib:,.2f}.')
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f'Contribution for bonuses ${contrib:,.2f}.')

main()

# End

# Checkpoint

# 5.18 What is the scope of a global variable?
# A: The entire program.

# 5.19 Give one good reason that you should not use global 
# variables in a program.
# A: Make debugging difficult, functions that use global variables become
# dependent on it, make a program hard to understand.
 
# 5.20 What is a global constant? Is it permissible to use  
# global constants in a program?
# A: A name that is available to every function in the program. It is 
# permissible. Value cannot be changed during execution.

# End