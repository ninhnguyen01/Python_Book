# Review Questions

# Algorithm Workbench

# 1. Suppose 'my_car' is the name of a variable that references
# an object, and 'go' is the name of a method. Write a statement
# that uses the 'my_car' variable to call the 'go' method. 
# (stuck)

# 2 . Write a class definition named Book. The Book class
# should have data attributes for a book's title, the author's
# name, and the publisher's name. The class should also have
# the following:
# a. An __init___ method for the class. The method should 
# accept an argument for each of the data attributes.
# b. Accessor and mutator methods for each data attribute.
# c. An str_method that returns a string indicating the state
# of the object.

class Book:
    def __init__(self,title,author,publisher):
        self.title = title
        self.author = author
        self.publisher= publisher
    def set__title(self,title):
        self.title = title
    def set__author(self,author):
        self.author = author
    def set__publisher(self,publisher):
        self.publisher = publisher
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_publisher(self):
        return self.publisher
    def __str__(self):
        return f'{self.title}\n' + \
               f'{self.author}\n' + \
               f'{self.publisher}\n' 

# 3. Look at the following description of a problem domain:
# ....
# Assume that you are writing a program that will calculate
# the amount of interest earned for a bank account.
# a. identify the potential classes in this problem
# b. Refine the list to include only the necessary class or 
# classes for this problem.
# c. Identify the responsibilities of the class or classes.
# (in progress)
class Bank():
    def __init__(self,checking,saving,market):
        self.checking = checking
        self.saving = saving
        self.market = market
    def set__checking(self,checking):
        self.checking = checking
    def set__saving(self,saving):
        self.saving = saving
    def set__market(self,market):
        self.market = market
    def get_checking(self):
        return self.checking
    def get__saving(self):
        return self.saving 
    def get__market(self):
        return self.market

# End