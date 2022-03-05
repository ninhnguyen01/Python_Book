# Using Loops to Process Files (Title)

# Reading

# This program prompts the user for sales amounts
# and writes those amounts to the sales.txt file.
# (with for loop)
def main():
    num_days = int(input('For how many days do '
     + 'you have sales? '))
    sales_file = open('sales.txt', 'w')
    for count in range (1, num_days + 1):
        sales = float(input(f'Enter the sales for day #{count}: ')) 
        sales_file.write(f'{sales}\n')
    sales_file.close()
    print('Data written to sales.txt.')

if __name__ == '__main__':
    main()

# Reading a File with a Loop and Detecting the End 
# of the File (section)

# psuedocode:
# 1) Open file
# 2) Use 'readline' to read the first line from the file
# 3) While value returned from 'readline' is not an empty
# string:
#   Process the item that was just read from the file.
#   Use 'readline' to read the next line from the file.
# Close the file.

# This program reads all of the values in the sales.txt
# file.
# with (while loop)
def main():
    sales_file = open('sales.txt', 'r')
    line = sales_file.readline()
    while line != '':
        amount = float(line)
        print(f'{amount:.2f}')
        line = sales_file.readline()
    sales_file.close()

if __name__ == '__main__':
    main()  

# Using Python's 'for' Loop to Read Lines
# General Format 'for' Loop:
#   for variable in file_object:
#       statement
#       statement
#       etc.

# This program uses the 'for' loop to read all of the 
# values in the sales.txt file.
def main():
    sales_file = open('sales.txt', 'r')
    for line in sales_file:
        amount = float(line)
        print(f'{amount:.2f}')
    sales_file.close()

if __name__ == '__main__':
    main()  

# pseudocode:
# 1) Get number of videos.
# 2) Open outputfile.
# 3) For each video in the project
#       Get video's running time 
#       Write running time to file
# 4) Close file.

# This program saves a sequence of video running times
# to the video_times.txt file.
def main():
    num_videos = int(input('How many videos are in the ' +
    'project? '))
    video_file = open('video_times.txt','w')
    print('Enter the running times for each video.')
    for count in range(1,num_videos + 1):
        run_time = float(input(f'Video #{count}: '))
        video_file.write(f'{run_time}\n')
    video_file.close()
    print('The times have been saved to video_times.txt.')

if __name__ == '__main__':
    main()  

# pseudocode:
# 1) Initialize an accumulator to 0.
# 2) Initialize a count variable to 0.
# 3) Open the input file.
# 3) For each line in the file.
#       Convert line to floating point (video runtime)
#       Add one to the count variable (keep video count)
#       Display video running time
#       Add runtime to accumulator
# 4) Close file.
# 5) Display content of accumulator as total runtime

# This program the values in the video_times.txt
def main():
    video_file = open('video_times.txt','r')
    total = 0.0
    count = 0
    print('Here are the running times for each video: ')
    
    for line in video_file:
        run_time = float(line)
        count += 1
        print('Video #', count, ': ', run_time, sep='')
        total += run_time
    video_file.close()
    print(f'The total running time is {total} seconds.')

if __name__ == '__main__':
    main()  

# End

# Checkpoint

# 6.12 Write a short program that uses a for loop to write the 
# numbers 1 through 10 to a file.
outfile = open('numbers.txt','w')
for num in range (1,11):
    outfile.write(str(num,)+'\n')
outfile.close()

# 6.13 What does it mean when the readline method returns an empty
# string?
# A. The readline method returns an empty string ('') when it has
# attempted to read beyond the end of a file.

# 6.14 Assume the file data.txt exists and contains several lines
# of text. Write a short program using the 'while' loop that displays
# each line in the file.
infile = open('numbers.txt','r')
line = infile.readline()
while line != '':
    print(line)
    line = infile.readline()
infile.close()

# 6.15 Revise the program that you wrote for checkpoint 6.14 to use 
# the 'for' loop instead of the 'while' loop.
infile = open('numbers.txt','r')
for line in infile:
    num = int(line)
    print(num)
infile.close()

# End