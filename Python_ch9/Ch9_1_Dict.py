# Dictionaries (section)

# Reading

# Creating a Dictionary (section)
# dictionary
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}

# Retrieving a Value from a Dictionary (section)
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
print(phonebook)

# Retrieve value from a dictiionary General Format:
# dictionary_name[key]
phonebook['Chris']

# if no key, KeyError exception
# string comparisons case sensitive

# Using the 'in' and 'not in' Operators to Test for a Value in
# a Dictionary.
# to prevent KeyError exception
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
if 'Chris' in phonebook:
    print(phonebook['Chris'])

phonebook = {'Chris':'555-1111','Katie':'555-2222'}
if 'Joanne' not in phonebook:
    print('Joanne is not found.')

# Adding Elements to an Existing Dictionary (section)
# dictionaries are mutable objects.

# General Format:
# dictionaty_name[key] = value
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
print(phonebook)

phonebook['Joe'] = '555-0123' 
phonebook['Chris'] = '555-4444'
print(phonebook)

# no duplicate keys in dictionary

# Deleting Elements (section)

# General Format:
# del dictionaty_name[key]
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
print(phonebook)

del phonebook['Chris']
print(phonebook)

# use 'in operator to prevent KeyError exception
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
print(phonebook)

if 'Chris' in phonebook:
    del phonebook['Chris']
print(phonebook)

# Getting the Number of Elements in a Dictionary (section)
phonebook = {'Chris':'555-1111','Katie':'555-2222'}
num_items = len(phonebook)
print(num_items)

# Mixing Data Types in a Dictionary (section)
employee = {'name': 'Kevin Smith','id':12345,'payrate': 25.75}
print(employee)
employee['name']

# Creating an Empty Dictionary
phonebook = {}
phonebook['Chris'] = '555-1111'
phonebook['Katie'] = '555-2222'
phonebook['Joanne'] = '555-3333'
print(phonebook)

# built-in dict method (alternative)
phonebook = dict()

# Using the 'for' Loop to Iterate over a Dictionary
# General Format:
# for var in dictionary:
#   statement 
#   statement 
#   etc.

phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
for key in phonebook:
    print(key)

for key in phonebook:
    print(key,phonebook[key])

# Some Dictionary Methods (section)

# clear
# get (value)
# items (return key and value as tuples)
# keys
# pop (return value from a key and remove key-value pair)
# popitem (return last key-value pair as tuples, remove from dict)
# values 

# dictionary.clear()
phonebook = {'Chris':'555-1111','Katie':'555-2222'}
print(phonebook)
phonebook.clear()
print(phonebook)

# dictionary.get(key,default)
phonebook = {'Chris':'555-1111','Katie':'555-2222'}
value = phonebook.get('Katie','entry not found')
print(value)
value = phonebook.get('Andy', 'Entry not found')
print(value)

# dictionary.items()
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
dct = phonebook.items()
print(dct)

# with 'for' loop
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
for key, value in phonebook.items():
    print(key,value)

# dictionary.keys()
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
dct = phonebook.keys()
print(dct)

# with for 'loop'
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
for key in phonebook.keys():
    print(key)

# dictionary.pop(key, default)
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
phone_num = phonebook.pop('Chris','Entry not found')
print(phone_num)
print(phonebook)
phone_num = phonebook.pop('Andy', 'Element not found')
print(phone_num)
print(phonebook)

# dictionary.popitem()
# k, v = dictionary.popitem()
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
print(phonebook)
key, value = phonebook.popitem()
print(key, value)
print(phonebook)

# popitem raises KeyError exception on empty dict

# dictionary.values()
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
value = phonebook.values()
print(value)

# with 'for' loop
phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
for val in phonebook.values():
    print(val)

# check card_dealer.py
# check birthdays.py

# Dictionary Comprehensions
# read input elements to produce a dict

numbers = [1,2,3,4]
squares = {item:item**2 for item in numbers}
print(numbers)
print(squares) 

phonebook = {'Chris':'555-1111','Katie':'555-2222',
'Joanne':'555-3333'}
print(phonebook)
phonebook_copy = {k:v for k,v in phonebook.items()}
print(phonebook_copy)

# Using if Clauses with Dictionary Comprehensions (section)
populations = {'New York': 8398748, 'Los Angeles': 3990456,
                'Chicago': 2705994,'Houston': 2325502,
                'Phoenix': 1660272,'Philadelphia': 1584138}

largest = {}
for k, v in populations.items():
    if v > 2000000:
        largest[k] = v
        print(largest)

# alternative (dict comprehension)
largest = {k:v for k,v in populations.items() if v > 2000000}

# General Format:
# {result_expression iteration_expression if_clause}

populations = {'New York': 8398748, 'Los Angeles': 3990456,
                'Chicago': 2705994,'Houston': 2325502,
                'Phoenix': 1660272,'Philadelphia': 1584138}
largest = {}
largest = {k:v for k,v in populations.items() if v > 2000000}
print(largest)

# End 

# Checkpoint

# 9.1 An element in a dictionary has 2 parts. What are they 
# called?
# A. Key and value.

# 9.2 Which part of a dictionary must be immutable?
# A. The key.

# 9.3 Suppose 'start' : 1472 is an element in a dictionary.
# What is the key? What is the value?
# A. Key is start. Value is 1472.

# 9.4 Suppose a dictionary named 'employee' has been created.
# What does the folowing statement do ?
employee ['id'] = 54321 
# A. It stores the key-value pair in the employee dictionary

# 9.5 What will the following code display?
stuff = {1 : 'aaa', 2: 'bbb', 3 : 'ccc'}
print(stuff[3])
# A. ccc

# 9.6 How can you determine whether a key-value pair exists
# in a dictionary?
# A. You can use the 'in' operator.

# 9.7 Suppose a dictionary named 'inventory' exists. What does the 
# following statement do?
# del inventory[654]
# A. It deletes the element that has the key 654.

# 9.8 What will the following code display?
stuff = {1 : 'aaa', 2: 'bbb', 3 : 'ccc'}
print(len(stuff))
# A. 3

# 9.9 What will the following code display?
stuff = {1 : 'aaa', 2: 'bbb', 3 : 'ccc'}
for k in stuff:
    print(k)
# A. 1
#    2
#    3

# 9.10 What is the difference between the dictionary methods
# pop and popitem?
# A. Pop accepts a key as an argument, returns the value 
# that is associated with that key, and removes that key-value
# pair from the dictionary. Popitem returns a randomly selected
# key-value pair, as a tuple, and removes that key-value pair
# from the dictionary.

# 9.11 What does the 'items' method return?
# A. All a dictionary's keys and their associated values
# as a sequence of tuples.

# 9.12 What does the 'keys' method return?
# A. All the keys in a dictionary
# as a sequence of tuples.

# 9.13 What does the 'values' method return?
# A. All the values in a dictionary
# as a sequence of tuples.

# 9.14 Assume the following list exists:
names = ['Chris', 'Katie', 'Joanne', 'Kurt']
# Write a statement that uses a dictionary comprehension to
# create a dictionary in which each element contains a name from
# the 'names' list as its key, and the length of that name as its
# value.
result = {item:len(item) for item in names}
print(result)
  
# 9.15 Assume the following dictionary exists: 
phonebook = {'Chris':'919-555-1111','Katie':'828-555-2222',
'Joanne':'704-555-3333','Kurt':'919-555-3333'}
# Write a statement that uses a dictionary comprehension to
# create a second dictionary containing the elements of 
# 'phonebook' that have a value starting with '919'.
phonebook_copy = {k:v for k,v in phonebook.items() if 
v.startswith('919')}
print(phonebook_copy)

# End