# Tuples (Title)

# Reading

# tuple
my_tuple = (1,2,3,4,5)
print(my_tuple)

# tuple with 'for' loop
names = ('Holly','Warren','Ashley')
for n in names:
    print(n)

#  Tuples Index
names = ('Holly','Warren','Ashley')
for i in range(len(names)):
    print(names[i])

# Tuples support:

# Subscripting index (retrieving element values only)
# Methods such as Index
# Built-in functions such as len, min, and max
# Slicing expressions
# The 'in' operator 
# The + and * operators

# DO NOT SUPPORT
# append, remove, insert, reverse, and sort.

# One Element Tuple
# my_tuple = (1,)

# Converting between Lists and Tuples 
number_tuple = (1,2,3)
number_list = list(number_tuple)
print(number_list)

str_list = ['one','two','three']
str_tuple = tuple(str_list)
print(str_tuple)

# End 

# Checkpoint

# 7.25 What is the primary difference between a list and a tuple?
# A. The primary difference between tuples and lists is that 
# tuples are immutable. That means that once a tuple is created,
# it cannot be changed.

# 7.26 Give two reasons why tuples exist.
# A. Three reasons.
# 1) Processing a tuple is faster than processing a list (good
# for big data that will not be modified).
# 2) Tuples are safe (no change content).
# 3) Certain ops requires the use of a tuple.

# 7.27 Assume my_list references a list. Write a statement that 
# converts it to a tuple.
# A. my_tuple = tuple(my_list)

# 7.28 Assume my_tuple references a tuple. Write a statement that 
# converts it to a list.
# A. my_list = list(my_tuple)

# End