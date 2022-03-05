# The if Statement (Title)

# Reading

# Sequence Structure Example [Execute in the order in which they appear] (section)
name = input('What is your name? ')
age = int(input('What is your age? '))
print('Here is the date you enter: ')
print('Name: ', name)
print('Age: ', age)

# General format of if statement (section)
# if condition:
#       statement
#       statement
#       etc.

# Boolean Expressions and Relational Operators.
# Example Below
x = 1
y = 0
x > y 
y > x

# Putting It All together

# Example Decision Structure
sales = 5500.0
if sales > 5000.0:
    bonus = 500.0
    commission_rate = 0.12
    print('You met your sales quota!')

# This program gets three test scores and displays their average.
# It congratulates the user if the average is a high score.

# The HIGH_SCORE named constant holds the value that is considered a high
# score.
HIGH_SCORE = 95

# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score,
average = (test1 + test2 + test3) / 3

# Print the average.
print(f'The average score is {average}.')

# If the average is a high score, congratulate the user.

if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!') 

# End

# Checkpoint

# 3.1 What is a control structure?
# A: A logical design that controls the order in which a set
# of statements execute.

# 3.2 What is a decision structure?
# A: A program structure that can execute a set of statements only under
# certain circumstances.

# 3.3 What is a single alternative decision strcuture?
# A: A decision structure that provides a single alternative path for
# execution.

# 3.4 What is a Boolean Expression?
# A: An expression that can be evaluated as either true or false.

# 3.5 What types of relationships between values can you test with
# relational operators?
# A: Greater than (>), less than (<), greater than or equal to (>=),
# less than or equal to (<=), equal to (==), not equal to (!=).

# 3.6 Write an if statement that assigns 0 to x if y is equal to 20
y = 20
if y == 20:
    x = 0

# 3.7 Write an if statement that assigns 0.2 commissionRate if sales is
# greater than or equal to 10000.  
if sales >= 10000:
    commission_Rate = 0.2

# End