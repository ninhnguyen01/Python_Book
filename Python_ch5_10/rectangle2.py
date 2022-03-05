# Conditionally Executing the 'main' Function in a Module (5.10 program)

def area(width, length):
    return width * length
def perimeter(width, length):
    return 2 * (width + length)

def main():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print('The area is',area(width,length))
    print('The perimeter is',perimeter(width,length))
    # Call the 'main' function ONLY if the file is being run as
    # a standalone program.
if __name__ == '__main__':
    main()
