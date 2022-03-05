# The while Loop: A Condition-Controlled Loop (Title)

# Reading

#  General format of the 'while loop'(section)

# while condition:
#   statement
#   statement
#   etc.

# This program calculates sales commissons.

# Creating a variable to control the loop.

keep_going = 'y'

# Calculate a series of commissions.

while keep_going == 'y':
    # Get a saleperson's sales and commisson rate.
    
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commissionn rate: '))
    
    # Calculate the commission.
    
    commission = sales * comm_rate
    
    # Display the commission.
    
    print(f'The commisson is ${commission:,.2f}.')
    
    # See if the user wants to do another one.
    
    keep_going = input('Do you want to calculate another' +
    'commission(Enter y for yes): ')

# This program assist a technician in the process of checking a
# substance's temperature.
# Named constant to represent the maximum temperature.

MAX_TEMP = 102.5

# Get the substance's temperature.

temperature = float(input("Enter the substance's Celsius temperature: ")) 

# As long as necessary, instruct the user to adjust the thermostat.

while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temprature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

# Remind the user to check the temperature again in 15 minutes.

print('The temperature is acceptable.')
print('Check it again in 15 minutes.')

# End

# Checkpoint 

# 4.4 What is a loop iteration?
# A: An execution of the statements in the body of loop.

# 4.5 Does the 'while' loop test its condition before or after it
# performs an iteration?
# A: Before.

# 4.6 How many times will 'Hello World' be printed in the following
# program.

count = 10
while count < 1:
    print('Hello World')
# 0

# 4.7 What is an infinite loop?
# A: A loop that continues to repeat until it is interrupted.

# End
