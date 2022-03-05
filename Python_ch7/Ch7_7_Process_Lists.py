# Processing List (Title)

# Reading

# This program calculates the gross pay for each of Megan's baristas.
NUM_EMPLOYEES = 6

def main():
    hours = [0] * NUM_EMPLOYEES
    for index in range(NUM_EMPLOYEES):
        hours[index] = float(input(f'Hours worked by employee {index + 1}: '))
    pay_rate = float(input('Hourly pay rate: '))
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f'Gross pay for employee {index + 1}: ${gross_pay:,.2f}')

if __name__ == '__main__':
    main()

# Totaling the Values in a list (section)
# This program calculates the total of the values in a list.
def main():
    numbers = [2,4,6,8,10]
    total = 0
    for value in numbers:
        total += value 
    print(f'The total of the elements of is {total}.')

if __name__ == '__main__':
    main()

# Averaging the values in a list (section)
# This program calculates the average of the values in a list.
def main():
    scores = [2.5,7.3,6.5,4.0,5.2]
    total = 0.0
    for value in scores:
        total += value
    average = total / len(scores)
    print(f'The average of the elements is {average}.')

if __name__ == '__main__':
    main()

# Passing a List as an Argument to a Function (section)
# This program uses a function to calculate the total of the values
# in a list.
def main():
    numbers = [2,4,6,8,10]
    print(f'The total is {get_total(numbers)}.')
def get_total(value_list):
    total = 0
    for num in value_list:
        total += num
    return total

if __name__ == '__main__':
    main()

# Returning a List from a Function (section)
# This program uses a function to create a list.
# The function returns a reference to the list.
def main():
    numbers = get_values()
    print('The numbers in the list are:')
    print(numbers)

def get_values():
    values = []
    again = 'y'
    while again == 'y':
        num = int(input('Enter a number: '))
        values.append(num)
        print('Do you want to add another number?')
        again = input('y = yes, anything else = no: ')
        print()
    return values 

if __name__ == "__main__":
    main()

# This program get a series of test scores and calculates
# the average of the scores with the lowest score dropped.
# pseudocode
# 1) student test score
# 2) total of scores
# 3) find lowest score
# 4) subtract low score from total
# 5) divide adjusted total by 1 less than the number of test scores
# this is the average.
# 6) display the average

def main():
    scores = get_scores()
    total = get_total(scores)
    lowest = min(scores)
    total -= lowest
    average = total / (len(scores) - 1) 
    print(f'Average with lowest score dropped: {average}')

def get_scores():
    test_scores = []
    again = 'y'
    while again == 'y':
        value = float(input('Enter a test score: '))
        test_scores.append(value)
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()
    return test_scores

def get_total(value_list):
    total = 0.0
    for num in value_list:
        total += num
    return total
    
if __name__ == "__main__":
    main()

# Randomly Selecting List Elements (section)
import random 
names = ['Jenny','Kelley','Chloe','Aubrey']
winner = random.choice(names)
print(winner)

# k = 'n' (n is number of elements you want)
import random
numbers = [1,2,3,4,5,6,7,8,9,10]
selected = random.choices(numbers, k=3)
print(selected)

# sample function -> unique elements (no duplicates)
import random
numbers = [1,2,3,4,5,6,7,8,9,10]
selected = random.sample(numbers,k=3)
print(selected)

# Working with Lists and Files (section)
# This program uses the writelines method to save a list
# of strings to a file.
def main():
    cities = ['New York','Boston','Atlanta','Dallas']
    outfile = open('cities.txt','w')
    outfile.writelines(cities)
    outfile.close()

if __name__ == "__main__":
    main()

# This program saves a list of strings to a file.
# (with 'for' loop) 
# newline
def main():
    cities = ['New York','Boston','Atlanta','Dallas']
    outfile = open('cities.txt','w')
    for item in cities:
        outfile.write(item + '\n')
    outfile.close()

if __name__ == "__main__":
    main()

# This program reads a file's contents into a list.
# (with 'for' loop) 
# strip

def main():
    infile = open('cities.txt','r')
    cities = infile.readlines()
    infile.close()
    for index in range(len(cities)):
        cities[index] = cities[index].rstrip('\n')
    print(cities)

if __name__ == "__main__":
    main()

# This program saves a list of numbers to a file.
def main():
    numbers = [1,2,3,4,5,6,7]
    outfile = open('numberlist.txt', 'w')
    for items in numbers:
        outfile.write(str(items)+'\n')
    outfile.close()
  
if __name__ == "__main__":
    main()  

# This program reads numbers from a file into a list.
def main():
    infile = open('numberlist.txt', 'r')
    numbers = infile.readlines()
    infile.close()
    for index in range (len(numbers)):
        numbers[index] = int(numbers[index])
    print(numbers)

if __name__ == "__main__":
    main()  

# End