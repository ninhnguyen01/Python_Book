# List Comprehensions (Title)

# Reading

# list comprehension
list1 = [1,2,3,4]
list2 = [item for item in list1]

# General Format Simple List Comprehension
# [result_expression iteration_expression]

# Square of all numbers in a first list
list1 = [1,2,3,4]
list2 = []

for item in list1:
    list2.append(item**2)

# List comprehension
list1 = [1,2,3,4]
list2 = [item**2 for item in list1]

# List of strings and length in first list
str_list = ['Winken', 'Blinken', 'Nod']
len_list = []
for s in str_list:
    len_list.append(len(s))

# List comprehension
str_list = ['Winken', 'Blinken', 'Nod']
len_list = [len(s) for s in str_list]

# Using if Clauses with List Comprehension (section)
list1 = [1,12,2,20,3,15,4]
list2 = []

for n in list1:
    if n < 10:
        list2.append(n)

# General Format if Clause to a List Comprehension:
# [result_expression iteration_expression if_clause]
list1 = [1,12,2,20,3,15,4]
list2 = [item for item in list1 if item < 10]

last_name = ['Jackson', 'Smith', 'Hildebrandt', 'Jones']
short_names = [name for name in last_name if len(name) < 6]

# End

# Checkpoint

# 7.19 Look at the folowing list comprehension:
# [x for x in my_list]
# What is the result expression? 
# What is the iteration expression?
# A. The result expression is: x. The iteration expression is: 
# for x in my_list.

# 7.20 After this code executes, what value will the list2 list
# hold?
list1 = [1,12,2,20,3,15,4]
list2 = [n*2 for n in list1]
# A. [2,24,4,40,6,30,8]

# 7.21 After this code executes, what value will the list2 list
# hold?
list1 = [1,12,2,20,3,15,4]
list2 = [n for n in list1 if n > 10]
# A. [12,20,15]

# End.