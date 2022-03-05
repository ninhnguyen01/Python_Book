# String Slicing (Title)

# Reading

# string slices (substrings)

# General Format:
# string[start : end]
full_name = 'Patty Lynn Smith'
middle_name = full_name[6:10]
print(middle_name)

full_name = 'Patty Lynn Smith'
middle_name = full_name[:5]
print(middle_name)

full_name = 'Patty Lynn Smith'
middle_name = full_name[11:]
print(middle_name)

full_name = 'Patty Lynn Smith'
my_string = full_name[:]
print(my_string)

# Equivalent 
my_string = full_name[0 : len(full_name)]
print(my_string)

# negative number
full_name = 'Patty Lynn Smith'
last_name = full_name[-5:]

# Login Program 
# Check login.py

# Generate Login Program
# Check generate_login.py

# End

# Checkpoint 

# 8.7 What will the following code display?
mystring = 'abcdefg'
print(mystring[2:5])
# A. cde

# 8.8 What will the following code display?
mystring = 'abcdefg'
print(mystring[3:])
# A. defg

# 8.9 What will the following code display?
mystring = 'abcdefg'
print(mystring[:3])
# A. abc

# 8.10 What will the following code display?
mystring = 'abcdefg'
print(mystring[:])
# A. abcdefg

# End