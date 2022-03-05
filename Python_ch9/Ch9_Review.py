# Review Questions

# Algorithm Workbench

# 1. Write a statement that creates a dictionary containing
# the following key-value pairs:
# 'a' : 1
# 'b' : 2
# 'c' : 3

letter = {'a':1,
            'b':2,
            'c':3}
print(letter)

# 2. Write a statement that creates an empty dictionary
letter = {}
print(letter)

# 3. Assume the variable dct references a dictionary. Write
# an 'if' statement that determines whether the key 'James'
# exists in the dictionary. If so, display the value that
# is associated with that key. If the key is not in the 
# dictionary, display a message indicating so.
dct = {'John': 101, 'James': 202}
if 'James' in dct:
    print(dct['James'])
else:
    print('James is not found.')

# 4. Assume the variable dct references a dictionary. Write
# an 'if' statement that determines whether the key 'Jim'
# exists in the dictionary. If so, delete 'Jim' and 
# its associated value.
dct = {'John': 101, 'James': 202,'Jim': 501}
print(dct)

if 'Jim' in dct:
    del dct['Jim']
    print(dct)

# 5. Write code to create a set with the following integers
# as members: 10,20,30,and 40.
num = ([10,20,30,40])
print(num)

# 6. Assume each of the variables set1 and set2 references
# a set. Write code that creates another set 
# containing all the elements of set1 and set2, and assigns
# the resulting set to the variable set3. 
set1 = set([1,2,3])
set2 = set([4,5,6])
set3 = set1 + set2 
print(set3)

# 7. Assume each of the variables set1 and set2 references
# a set. Write code that creates another set 
# containing only the elements that are found in both 
# set1 and set2, and assigns
# the resulting set to the variable set3. 
set1 = set([1,2,3,4])
set2 = set([4,5,6,7])
set3 = set1.intersection(set2)
print(set3)

# 8. Assume each of the variables set1 and set2 references
# a set. Write code that creates another set 
# containing elements that appear in set1 but not in set2 
# and assigns
# the resulting set to the variable set3. 
set1 = set([1,2,3,4])
set2 = set([4,5,6,7])
set3 = set1.difference(set2)
print(set3)


# 9. Assume each of the variables set1 and set2 references
# a set. Write code that creates another set 
# containing elements that appear in set2 but not in set1 
# and assigns
# the resulting set to the variable set3. 
set1 = set([1,2,3,4])
set2 = set([4,5,6,7])
set3 = set2.difference(set1)
print(set3)


# 10. Assume each of the variables set1 and set2 references
# a set. Write code that creates another set 
# containing elements that are not shared by set1 and set2 
# and assigns
# the resulting set to the variable set3. 
set1 = set([1,2,3,4])
set2 = set([4,5,6,7])
set3 = set1.symmetric_difference(set2)
print(set3)


# 11. Assume the following list exists:
numbers = [1,2,3,4,5]
# Write a statement that uses a dictonary comprehension to 
# create a dictionary in which each element contains a number
# from the numbers list as its key, and the product of that
# number times 10 as its value. In other words, the dictionary
# should contain the following elements:
# {1:10,2:20,3:30,4:40,5:50}
# (stuck)
numbers1 = {num*10 for num in numbers}
print(numbers)
print(numbers1)

# 12. Assume the following dictionary exists:
test_averages = {'Janelle':98,'Sam':87,'Jennifer':92,
'Thomas':74,'Sally':89,'Zeb':84}
# Write a statement that uses a dictonary comprehension to 
# create a second dictionary named high_scores. The high_scores
# dictionary should contain all the elements of the test_averages
# dictionary in which the value is 90 or greater.
# (stuck)
high_scores = {score for score in test_averages if test_averages 
>= 90 }
print(high_scores)

# 13. Assume the variable 'dct' references a dictionary. Write
# code that pickles the dictionary and saves it to a file
# named mydata.dat.
import pickle
dct = {'John': 10, 'Jane': 20, 'Jack': 30}
outputfile = open('mydata.dat','wb')
pickle.dump(dct,outputfile)
outputfile.close()

# 14. Write code that retrieves and unpickles the dictionary that
# you pickled in Algorithm Workbench 11.

# End