import cellphone

def main():
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))
    phone = cellphone.Cellphone(man,mod,retail)
    print('Here is the data that you entered:')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model Number: {phone.get_model()}')
    print(f'Retail Price: {phone.get_retail_price():,.2f}')

if __name__ == '__main__':
    main()

# End