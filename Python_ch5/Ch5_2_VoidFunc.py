# Defining and calling a Void Function (Title)

# Reading

# General Format of a Function Definiton:

# def function_name():
#     statement
#     statement
#     etc.

# This program demonstrates a function.
# First, defined a function named message.
def message():
    print('I am Arthur,')
    print('King of the Britons.')
# Call the message function
message()

# This program has two functions. 
# First we define the main function.
def main():
    print('I have a message for you.')
    message()
    print('Goodbye!')

# Next we define the message function.
def message():
    print('I am Arthur,')
    print('King of the Britons.')

# Call the main function.
main()

# End

# Checkpoint

# 5.6 A function definition has what two parts?
# A: A header and a block. The header indicates the starting point
# of the function, and the block is a list of statements that belong
# to the function.

# 5.7 What does the phrase calling a "function" mean?
# A: To call a function means to execute the function.

# 5.8 When a function is executing, what happens when the end of the
# function's block is reached?
# A: It returns back to the part of the program that called the 
# function, and the program resumes execution at that point. 

# 5.9 Why must you indent the statements in a block?
# A: Because the Python Interpreter uses the indentation
# to determine where a block begins and ends.

# End
