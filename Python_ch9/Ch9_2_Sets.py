# Sets (Title)

# Reading

# set - an object that stores a collection of data
# all elements must be unique
# sets are unordered
# elements can be different data types.

# Creating a Set (section)
# 1 argument (list,tuple,string)
myself = set()
myself = set(['a','b','c'])
myself = set('abc')
myself = set(['one','two','three'])

# Getting the Number of Elements in a Set (section)
myset = set([1,2,3,4,5])
len(myset)

# Adding and Removing Elements (section)
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# update method
myset = set([1,2,3])
myset.update([4,5,6])
print(myset)

set1 = set([1,2,3])
set2 = set([8,9,10])
set1.update(set2)
print(set1)
print(set2)

myset = set([1,2,3])
myset.update('abc')
print(myset)

# remove method (raise KeyError exception)
myset = set([1,2,3,4,5])
print(myset)
myset.remove(1)
print(myset)

# discard method (no exception)
myset.discard(5)
print(myset)
myset.discard(99)
myset.remove(99)

# clear method 
myset = set([1,2,3,4,5])
print(myset)
myset.clear()
print(myset)

# Using the 'for' Loop to Iterate over a Set (section)
# General Format:
#   for var in set:
#       statement
#       statement
#       etc.

myself = set(['a','b','c'])
for val in myset:
    print(val)

# Using the 'in' and 'not in' Operators to Test for a Value
# in a Set (section)
myset = set([1,2,3])
if 1 in myset:
    print('The value 1 is in the set.')

myset = set([1,2,3])
if 99 not in myset:
    print('The value 99 is not in the set.')

# Finding the Union of Sets (section)

# General Format:
# set1.union(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.union(set2)
print(set3)

# alternative
# General Format:
# set1 | set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 | set2
print(set3)

# Finding the Intersection of Sets (section)

# General Format:
# set1.intersection(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.intersection(set2)
print(set3)

# alternative
# General Format:
# set1 & set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 & set2
print(set3)

# Finding the Difference of Sets (section)

# General Format:
# set1.difference(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.difference(set2)
print(set3)

# alternative
# General Format:
# set1 - set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 - set2
print(set3)

# Finding the Symmetric Difference of Sets (section)

# General Format:
# set1.symmetric_difference(set2)
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1.symmetric_difference(set2)
print(set3)

# alternative
# General Format:
# set1 ^ set2
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
set3 = set1 ^ set2
print(set3)

# Finding Subsets and Supersets (section)
set1 = set([1,2,3,4])
set2 = set([2,3])
set2.issubset(set1)
set1.issuperset(set2)

# alternative
set1 = set([1,2,3,4])
set2 = set([2,3])
set2 <= set1
set1 >= set2
set1 <= set2

# This program demonstrates various set operations.
baseball = set(['Jodi','Carmen','Aida','Alicia'])
basketball = set(['Eva','Carmen','Alicia','Sarah'])
print('The following students are on the baseball team:')
for name in baseball:
    print(name)

print()
print('The following students are on the basketball team:')
for name in basketball:
    print(name)

print()
print('The following students play both baseball and basketball:')
for name in baseball.intersection(basketball):
    print(name)

print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)

print()
print('The following students play baseball, but not basketball:')
for name in baseball.difference(basketball):
    print(name)

print()
print('The following students play basketball, but not baseball:')
for name in basketball.difference(baseball):
    print(name)

print()
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)

# Set Comprehensions (sections)
# an expression that reads a sequence of input elements to
# produce a set.

# List
set1 = set([1,2,3,4,5])
# Set
set2 = {item for item in set1}

# List
set1 = set([1,2,3,4,5])
# Set
set2 = {item**2 for item in set1}

# List
set1 = set([1,20,2,40,3,50])
# Set (if)
set2 = {item for item in set1 if item < 10}

# End

# Checkpoint

# 9.16 Are the elements of a set ordered or unordered?
# A. unordered.

# 9.17 Does a set allow you to store duplicate elements?
# A. No.

# 9.18 How do you create an empty set?
# A. You call the built-in set function.

# 9.19 After the following statement executes, what elements
# will be stored in the myset set?
# myset = set('Jupiter')
# A. ('J','u','p','i','t','e','r') in no particular order.

# 9.20 After the following statement executes, what elements will
# be stored in the 'myset' set?
# myset = set(25) 
# A. 25

# 9.21 After the following statement executes, what elements will
# be stored in the 'myset' set?
# myset = set('www xxx yyy zzz')
# A. ('w','x','y','z') in no particular order.

# 9.22 After the following statement executes, what elements will
# be stored in the 'myset' set?
# myset = set([1,2,2,3,4,4,4])
# A. ('1','2','3','4') in no particular order.

# 9.23 After the following statement executes, what elements will
# be stored in the 'myset' set?
# myset = set(['www' ,'xxx', 'yyy', 'zzz'])
# A. ('w','x','y','z') in no particular order.

# 9.24 How do you determine the number of elements in a set?
# A. You pass the set as an argument to the len function.

# 9.25 After the following statement executes, what elements will
# be stored in the 'myset' set?
# myset = set([10,9,8])
#  myset.update([1,2,3])
# A. ('10','9','8','1','2','3') in no particular order.

# 9.26 After the following statement executes, what elements will
# be stored in the 'myset' set?
# myset = set([10,9.8])
#  myset.update('abc')
# A. ('10','9','8','a','b','c') in no particular order.
 
# 9.27 What is the difference between the remove 
# and discard method?
# A. If the specified element to delete is not in the set,
# the 'remove' method raises a KeyError exception, but the 
# 'discard' method does not raise an exception.

# 9.28 How can you determine whether a specific element exists
# in a set?
# A. You can use the 'in' operator to test for the element.

# 9.29 After the following code executes, what elements will
# be members of set3?
# set1 = set([10,20,30])
# set2 = set([100,200,300])
# set3 = set1.union(set2)
# A. {10,20,30,100,200,300}
 
# 9.30 After the following code executes, what elements will
# be members of set3?
# set1 = set([1,2,3,4])
# set2 = set([3,4,5,6])
# set3 = set1.intersection(set2)
# A. {3,4}

# 9.31 After the following code executes, what elements will
# be members of set3?
# set1 = set([1,2,3,4])
# set2 = set([3,4,5,6])
# set3 = set1.difference(set2)
# A. {1,2}

# 9.32 After the following code executes, what elements will
# be members of set3?
# set1 = set([1,2,3,4])
# set2 = set([3,4,5,6])
# set3 = set2.difference(set1)
# A. {5,6}

# 9.33 After the following code executes, what elements will
# be members of set3?
# set1 = set(['a','b','c'])
# set2 = set(['b','c','d'])
# set3 = set1.symmetric_difference(set2)
# A. {'a','d'}

# 9.34 Look at the following code:
# set1 = set([1,2,3,4])
# set2 = set([2,3])
# set3 = set1.difference(set2)
# Which of the sets is a subset of the other?
# Which of the sets is a superset of the other? 
# A. Set2 is a subset of set1, and set1 is a superset of set2.

# End