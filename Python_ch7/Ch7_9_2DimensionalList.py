# Two_Dimensional Lists (Title)

# Reading
students = [['Joe','Kim'],['Sam','Sue'],['Kelly','Chris']]
print(students)
print(students[0])
print(students[1])
print(students[2])

# This program demonstrates a two-dimensional list (nested list)
def main():
    values = [[1,2,3],
              [10,20,30],
              [100,200,300]]
    for row in values:
        for element in row:
            print(element)

if __name__ == '__main__':
    main()

# This program assigns random numbers to a 
# two-dimensional list.
# assign value to element with index
import random

ROWS = 3
COLS = 4

def main():
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1,100)
    print(values)

if __name__ == '__main__':
    main()

# End

# Checkpoint

# 7.22 Look at the following interactive session, in which
# a two-dimensional list is created. How many rows and how many
# columns are in the list?
# numbers = [[1,2],[10,20],[100,200],
# [1000,2000]]
# A. The list contains 4 rows and 2 columns.

# 7.23 Write a statement that creates a two-dimensional list
# with 3 rows and 4 columns. Each element should be assigned
# the value 0.
# A. mylist = [[0,0,0,0],[0,0,0,0],
#              [0,0,0,0]]

# 7.24 Write a set of nested loops that display the contents
# of the 'numbers' listed shown in Checkpoint question 7.22.
# A. for r in range (4):
#        for c in range (2):
#           print (numbers[r][c])

# End