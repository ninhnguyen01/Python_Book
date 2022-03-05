# List Slicing (section)

# Reading
# slices - selecting subsections of a sequence 
#  
# List Slice general format
# list_name [start : end]

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
'Thursday', 'Friday', 'Saturday']

mid_days = days[2:5]
print(mid_days)

numbers = [1,2,3,4,5]
print(numbers)
print(numbers[1:3])

# no 'start' index, Python uses 0
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[:3])

# no 'end' index, Python uses length of list
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[2:])

# no 'start' or 'end' index, get a copy of the entire list
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[:])

# with step value
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[1:8:2])

# negative numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[-5:])

# End

# Checkpoint

# 7.9 What will the following code display?
numbers = [1,2,3,4,5]
my_list = numbers[1:3]
print(my_list)
# A. [2,3]

# 7.10 What will the following code display?
numbers = [1,2,3,4,5]
my_list = numbers[1:]
print(my_list)
# A. [2,3,4,5]

# 7.11 What will the following code display?
numbers = [1,2,3,4,5]
my_list = numbers[:1]
print(my_list)
# A. [1]

# 7.12 What will the following code display?
numbers = [1,2,3,4,5]
my_list = numbers[:]
print(my_list)
# A. [1,2,3,4,5]

# 7.13 What will the following code display?
numbers = [1,2,3,4,5]
my_list = numbers[-3:]
print(my_list)
# A. [3,4,5]

# End