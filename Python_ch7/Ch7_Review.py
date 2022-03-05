# Review Questions

# Algorithm Workbench

# 1. Write a statement that creates a list with the following
# strings: 'Einstein','Newton','Copernicus', and 'Kepler'.
names = ['Einstein','Newton','Copernicus','Kepler']
print(names)

# 2. Assume names references a list. Write a for loop
# that displays each element of the list.
names = ['Einstein','Newton','Copernicus','Kepler']
for name in names:
    print(name)

# 3. Assume the list 'numbers1' has 100 elements, and
# 'numbers2' is an empty list. Write code that copies
# the values in 'numbers1' to 'numbers2'.
numbers1 = [1,2,3,4,5,6,7,8,9,10]
numbers2 = []
numbers2 = numbers1
print(numbers2)

# 4. Draw a Flowchart (skip)


# 5. Write a function that accepts a list as an argument
# (assume the list contains integers) and returns the total
# of the values in the list.
# (stuck)
def list():
    list1 = [10,20,30,40,50]
    total = 0
    

list()

# 6. Assume the 'names' variable references a list of strings.
# Wrtie code that determines whether 'Ruby' is in the names
# list. If it is, display the message 'Hello Ruby'. Otherwise,
# display the message 'No Ruby'.
names = ['Ninh','Andrew','Ruby']
if 'Ruby' in names:
    print('Hello Ruby')
else:
    print('No Ruby')

# 7. What will the following code print?
list1 = [40,50,60]
list2 = [10,20,30]
list3 = list1 + list2
print(list3)
# A. [40,50,60,10,20,30]

# 8. Assume 'list1' is a list of integers. Write a statement
# that uses a list comprehension to create a second list
# containing the squares of the elements of 'list1'.
list1 = [2,3,4,5,6]
list2 = [item**2 for item in list1]
print(list2)

# 9. Assume 'list1' is a list of integers. Write a statement
# that uses a list comprehension to create a second list
# containing the elements of 'list1' that are greater than 100.
list1 = [60,90,100,112,212]
list2 = [item for item in list1 if item > 100]
print(list2)

# 10. Assume 'list1' is a list of integers. Write a statement
# that uses a list comprehension to create a second list
# containing the elements of 'list1' that are even numbers.
# (stuck)
list1 = [60,90,100,112,212]
list2 = [item for item in list1 if list1]
print(list2)
 
# 11. Write a statement that creates a two-dimensional list
# with 5 rows and 3 columns. Then write nested loops that get
# an integer value from the user for each element in the list.
# (stuck)
list1 = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,12,13],
         [14,15,16]]
for list in list1:
    for element in list:
        print(element)

# End