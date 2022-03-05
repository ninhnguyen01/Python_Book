# More About the print Function (Title)

# Reading

# Suppressing the Print Function's Ending Newline
print('one')
print('two')
print('three')

# To print space instead of newline character (new line of output)
print('one', end=' ')
print('two', end=' ')
print('three')

# To print nothing at the end of its output
print('one', end='')
print('two', end='')
print('three', end='')

# Specifiying an Item Separator (section)
print('One', 'Two', 'Three')

# Use sep='' if you want no space printed between items
print('One' , 'Two', 'Three', sep='')

# Special argument to separate multiple items (similar to above)
print('One', 'Two', 'Three', sep='*')

# Additional example
print('One', 'Two', 'Three', sep='~~~')

# Escape Characters (sections)

# Escape Character \n
print('One/nTwo/nThree')

# Escape Character \t
print('Mon\tTues\tWed')
print('Thur\tFri\tSat')

# Escape Character \' and \" to display quotation marks
print("Your assignment is to read \"Hamlet\" by tomorrow.")
print('I\'m ready to being.') 

# Escape Character \\ to display a backslash
print('The path is C:\\temp\\data.')

# End

# Checkpoint 

# 2.25 How do you supress the print function's ending newline?
# A: Pass special argument end = ' ' to the function

# 2.26 How can you change the character that is automatically 
# displayed between multiple items that are passed to the print function?
# A: Pass the argument sep = ' ' to the print function

# 2.27 What is the '/n' escape character?
# A: Newline escape character

# End