# Review Questions (Title) 

# Algorithm Workbench 

# 1
product = int(input('Enter a number: '))
product *= 10
while product < 100:
    print(product)

# 2
response = 'Y'

while response == 'Y':
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a second number: '))
    sum = num1 + num2
    print(sum)
    response = input("Do you want to continue? If yes, enter 'Y'. Enter 'n' for no: ") 

# 3
for x in range (0,1001,10):
    print(x)

# 4
max = 10
total = 0

for num in range(max):
    num = int(input('Enter a number: '))
    total += num
    print(total)

# 5 



# 6
 
# a. x += 1
# b. x *= 2
# c. x /= 10
# d. x -= 100

# 7
for row in range (10):
    for col in range(15):
        print("#", end= '')
    print()

# 8
num = int(input('Enter a positive nonzero number: '))

while num == 0 or num < 0:
    print('Error! Please enter a positive nonzero number: ')
    num = int(input('Enter a positive nonzero number: '))

# 9
num_range = int(input('Enter a number in the range of 1 through 100: '))

while num_range < 1 or num_range > 100:
    print('Error! Enter a number in the range of 1 through 100: ')
    num_range = int(input('Enter a number in the range of 1 through 100: '))

# End