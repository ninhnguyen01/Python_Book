# Finding Items in Lists with the 'in' Operator (section)

# Reading

# 'In' Operator General Format
# item in list

# This program demonstrate the 'in' operator used with a list.
def main():
    prod_nums = ['V475', 'F987', 'Q143', 'R688']
    search = input('Enter a product number: ')
    if search in prod_nums:
        print(f'{search} was found in the list.')
    else:
        print(f'{search} was not found in the list.')

# alternate
    if search not in prod_nums:
        print(f'{search} was not found in the list.')
    else:
        print(f'{search} was found in the list.')
        
if __name__ == '__main__':
    main()

# End

# Checkpoint

# 7.14 What will the following code display?

names = ['Jim','Jill','John','Jasmine']
if 'Jasmine' not in names: 
    print('Cannot find Jasmine.')
else:
    print("Jasmine's family: ")
    print(names)

# A. Jasmine's family: 
#    ['Jim', 'Jill', 'John', 'Jasmine']