# Review Questions (Title) 

# Algorithm Workbench 

# 1
def times_ten():
    num = 10
    total = num * 10
    print(total)
    
times_ten()

# 2
def main():
    numb = 12
    show_value(numb)

def show_value(quantity):
    quantity = 12
    print(quantity)

main()

# 3
def main():
    my_function(3,2,1)

def my_function(a,b,c):
    print(a,b,c,)

main()

# 4 
def main():
    x = 1
    y = 3.4
    print(x,y)
    change_us(x,y)
    print(x,y)

def change_us(a,b):
    a = 0
    b = 0
    print(a,b)

main()

# 5
def main():
    my_function(2,4,6)


def my_function(a,b,c):
    d = (a+b)/c
    print(d)

main()

# 6
import random

rand = random.randrange(1,100)
print(rand)

# 7
def main():
    half()

def half():
    number = 6.0
    result = number / 2
    print(result)

main()

# 8
def main():
    num = 4
    result = cube(num)
    print(result)
    

def cube(num):
    return num * num * num
 
main()

# 9
def main():
    times_ten()
    total = times_ten() * 10
    print(total)

def times_ten():
    x = 4
    return x

main()

# 10
def get_first_name():
    f_name = input('Enter your first name: ')
    return f_name

get_first_name()

# End