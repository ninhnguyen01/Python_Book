# Logical Operators (Title)

# Reading

# The 'and' Operator (section)
# if temperature < 20 and minutes > 12:
    # print('The temperature is in the danger zone.')

# The 'or' Operator (section)

# if temperature < 20 or temperature > 100:
    # print('The temperature is too extreme.')

# The 'not' Operator
# if not (temperature > 100):
    # print('This is below the maximum temperature.')

# Compound expression with 'and' Operator (section)
# This program determines whether a bank customer qualifies for 
# a loan.
MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on a job

# Get the customer's annaul salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
'years employed: '))

# Determine whther the customer qualifies.
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('You qualify for a loan.')
else:
    print('You do not qualify for a loan.')

# Compound Expression with 'or' Operator (section)
# This program determines whether a bank customer qualifies for 
# a loan.
MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on a job

# Get the customer's annaul salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
'years employed: '))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('You qualify for a loan.')
else:
    print('You do not qualify for a loan.')

# Checking Numeric Ranges with Logical Operators (section)
# if x >= 20 or x <= 40:
#     print('The value is in the acceptable range.')

# if x < 20 or x > 40:
#     print('The value is outside the acceptable range.')



# Checkpoint

# 3.14 What is a compound Boolean expression? 
# A: It is an expressions that is created by using a logical operators 
# to combine two Boolean subexpressions.

# 3.15 The following truth table shows various combinations of the values
# true and false connected by a logical operator. Complete the table by
# circling T or F to indicate whtether the result of such a combination
# is true or false.

# Answer below
# F
# T
# F
# F
# T
# T
# T
# F
# F
# T

# 3.16
# Answer Below
# T
# F
# T
# T
# T

# 3.17 Explain how short-circuit evaluations work with the 'and' and 'or'
# operators. 
# A: If an expression on the left side of the 'and' operator is false, the
# right side will not be checked. If an expression on the left side of the
# 'or' operator is true, the right side will not be checked.

# 3.18 Write an if statement that displays the message "The number is 
# valid" if the value referenced by speed is within the range 0 through
# 200

speed = 100
if speed >= 0 and speed <= 200:
    print('The number is valid')


# 3.18 Write an if statement that displays the message "The number is not 
# valid" if the value referenced by speed is outside the range 0 through
# 200.

speed = 225
if speed < 0 or speed > 200:
    print('The number is not valid')

# End