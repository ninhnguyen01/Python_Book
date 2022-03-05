# Review Questions

# Algorithm Workbench

# 1. Write a program that opens an output file with the filename
# ...write name to file, close file.
outputfile = open('my_name.txt','w')
name = 'Ninh'
outputfile.write(name)
outputfile.close()

# 2. Write a program that opens the my_name.txt file,
# ...read name from file, displays name, closes file.
infile = open('my_name.txt','r')
file_content_name = infile.read()
infile.close()
print(file_content_name)

# 3. Write code that does the following: open outputfile
# with filename number_list.txt, uses a loop to write number 1
# through 100 to the file, closes file.
outputfile = open('number_list.txt','w')
for num in range (1,101):
    outputfile.write(str(num)+'\n')
outputfile.close()

# 4. Write code that does the following: opens number_list.txt file,
# from question 3, read numbers from file, displays them, 
# closes file.
infile = open('number_list.txt','r')
file_content_num = infile.read()
infile.close()
print(file_content_num)

# 5. Modify question 4 file to add all the numbers read from
# file and displays their total.
infile = open('number_list.txt','r')
file_content_num = infile.read()
total = 0
for num in range (1,101):
    total += num
infile.close()
print(f'The total is: {total}')

# 6. Write a code that opens an output file with the filename
# number_list.txt, but does not erase the file's contents if
# it already exists.
infile = open('number_list.txt','a')
file_content_num = infile.read()
infile.close()
print(file_content_num)

# 7. A file exists on the disk named students.txt. The file 
# contains several records, and each record contains 2 fields:
# (1) The student's name, and (2) the student's score for the
# final exam. Write code that deletes the record containing
# "John Perez" as the student name.

# Part 1: Create record
num_students = int(input('How many students ' +
    'do you want to add? '))
outputfile = open('students.txt','w')
for count in range(1,num_students+1):
    student_name = input('Enter student name: ')
    student_score_final = float(input('Enter student\'s final exam score: '))
    outputfile.write(f'Name: {student_name}\n')
    outputfile.write(f'Final Exam Score: {student_score_final}\n')
    print()
outputfile.close()

# Part 2: Display Record
infile = open('students.txt','r')
student_name = infile.readline()

while student_name != '':
    
    student_score_final = infile.readline()
    student_name.rstrip('\n')

    print(f'{student_name}')
    print(f'{student_score_final}')
    print()
    
    student_name = infile.readline()

infile.close()

# Part 3 Delete (error)
import os

found = False
search = input('Which student do you want to delete?:  ')
infile = open('students.txt','r')
temp_file = open('temp.txt','w')
student_name = infile.readline()
while student_name != '':
    student_score_final = infile.readline()
    student_name.rstrip('\n')

    if student_name == search:
        temp_file.write(f'{student_name}\n')
        temp_file.write(f'{student_score_final}\n')
    else:
        found = True

    student_name = infile.readline()
    
    infile.close()
    temp_file.close()

    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# 8 A file exists on the disk named students.txt. The file 
# contains several records, and each record contains 2 fields:
# (1) The student's name, and (2) the student's score for the
# final exam. Write code that changes Julia Milan's score to
# 100. 
# (in progress)

# 9. What will the following code display?
try: 
    x = float('abc123')
    print('The conversion is complete.')
except IOError:
    print('This code caused an IOError.')
except ValueError:
    print('This code caused a ValueError.')
print('The end.')
# A. ValueError

# 10. What will the following code display?
try:
    x = float('abc123')
    print(x)
except IOError:
    print('This code caused an IOError.')
except ZeroDivisionError:
    print('This code caused a ZeroDivisionError.')
except:
    print('An error happened.')
print('The end.')
# A. An error happened

# End