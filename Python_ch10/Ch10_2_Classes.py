# Classes (Title)

# Class Definiton (section)

import random
class Coin:
    def __init__(self):
        self.sideup = 'Heads'
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup
        
def main():
    my_coin = Coin()
    print('This side is up:',my_coin.get_sideup())
    print('I am tossing the coin...')
    my_coin.toss()
    print('This side is up:',my_coin.get_sideup())

if __name__ == '__main__':
    main()

# Hiding Attributes (section)
import random
class Coin:
    def __init__(self):
        self.sideup = 'Heads'
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin()
    print('This side is up:',my_coin.get_sideup())
    print('I am tossing the coin...')
    my_coin.toss()
    my_coin.sideup = 'Heads'
    print('This side is up:',my_coin.get_sideup())

if __name__ == '__main__':
    main()

# coindemo3
import random
class Coin:
    def __init__(self):
        self.__sideup = 'Heads'
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    def get_sideup(self):
        return self.__sideup

def main():
    my_coin = Coin()
    print('This side is up:',my_coin.get_sideup())
    print('I am going to toss the coin ten times:')
    for count in range (10):
        my_coin.toss()
        print(my_coin.get_sideup())

if __name__ == '__main__':
    main()

# Storing Classes in Modules (section)

# check coin.py 
# check coin_demo4.py 


# The BankAccount Class (section)

# check bankaccount.py
# check account_test.py

# The __str__ Method (section)
# check bankaccount2.py
# check account_test2.py

# End

# Checkpoint

# 10.5 Does the blueprint represent a class, or does it
# represent an object?
# A. A class.

# 10.6 In this metaphor, are objects the cookie cutter, or
# the cookies?
# A. The cookies.

# 10.7 What is the purpose of the __init__ method? When does
# it execute? 
# A. To initialize an object's data attributes. It executes
# immediately after the object is created.

# 10.8 What is the purpose of the self parameter in a method?
# A. When a method executes, it must have a way of knowing
# which object's data attributes it is supposed to operate on.
# When a method is called, Python automatically makes it 'self'
# parameter reference the specific object that the method is 
# supposed to operate on.

# 10.9 In a Python class, how do you hide an attribute from
# code outside the class?
# A. By starting the attribute's name with two underscores.

# 10.10 What is the purpose of the __str__ method?
# A. It returns a string representation of the object.

# 10.11 How do you call the __str__ method?
# A. By passing the object to the built-in 'str' method.

# End