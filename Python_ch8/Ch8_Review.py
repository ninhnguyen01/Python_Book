# Review Questions

# Algorithm Workbench

# 1. Assume Choices references a string. The following
# 'if' statement determines whether choices is equal to
# 'Y' or 'y':

# if choice == 'Y' or choice == 'y':

# Rewrite the statement so it only makes one comparison, 
# and does not use the 'or' operator.
choice = 'Y'

if choice.upper() == 'Y':
    print('Y is upper.')
else:
    print('y is not upper')

# 2. Write a loop that counts the number of space characters 
# that appear in the string referenced by 'mystring'.
mystring = ' '
total = 0
for s in mystring:
    if mystring == ' ':
        total += 1
        print(total)
       
# 3. Write a loop that counts the number of digits that
# appear in the string referenced by 'mystring'.
mystring = '12345'
digit = 0
for d in mystring:
    if mystring.isdigit():
        digit += 1
        print(digit)

# 4. Write a loop that counts the number of lowercase
# characters that appear in the string referenced 
# by 'mystring'.
mystring = 'mystring'
lower = 0
for l in mystring:
    if mystring.islower():
        lower += 1
        print(lower)
        
# 5. Write a function that accepts a string as an argument
# and returns true if the argument ends with the substring
# '.com'. Otherwise the function should return false.
def string():
    arg = 'string.com'
    if '.com' in arg:
        return True
    else:
        return False

string()

# 6. Write code that makes a copy of a string with all 
# occurrences of the lowercase 't' converted to uppercase. 
word = 'Titan'
if 't' in word:
    copy = word.upper()
    print(copy)

# 7. Write a function that accepts a string as an argument
# and displays the string backwards.
def backward():
    name = 'alucard'    
    print(name[-1],name[-2],name[-3],name[-4],name[-5],
name[-6],name[-7])

backward()

# 8. Assume 'mystring' references a string. Write a statement
# that uses a slicing expression and displays the first 3
# characters in the string.
mystring = 'alucard'
name = mystring[0:3]
print(name)

# 9. Assume 'mystring' references a string. Write a statement
# that uses a slicing expression and displays the last 3
# characters in the string.
mystring = 'alucard'
name = mystring[-3:]
print(name)

# 10. Look at the following statement
mystring = 'cookies>milk>fudge>cake>ice cream'
# Write a statement that splits this string, creating the
# following list:
# ['cookies','milk','fudge','cake','ice cream']
newstring = mystring.split('>')
print(newstring)

# End