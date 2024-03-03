#ex - 1
import os
'''
print("Directories:", os.getcwd())

print("Files and all directories:", os.listdir())

print(os.path.abspath('builtin_functions.py'))
'''
#ex - 2
'''
def checking_file(file_path):
    if os.path.exists(file_path):
        print(f"{file_path} is exist")
    else:
        print("Is not exist")
    if os.access('file_path', os.W_OK):
        print(f"{file_path} is writable.")
    else:
        print("is not writable.")
    if os.access('file_path', os.R_OK):
        print(f"{file_path} is readable.")
    else: 
        print("is not readable.")
    if os.access('file_path', os.X_OK):
        print(f"{file_path} can be executed.")
    else:
        print("can not be executed.")
        
file_path = input()
checking_file(file_path)
'''
#ex - 3
'''
file_path = input()
if os.path.exists(file_path):
    name_of_file = os.path.basename(file_path)
    directory = os.path.dirname(file_path)
    print(name_of_file)
    print(directory)
else:
    print("File is not exist.")
'''

#ex - 4
'''
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total = len(lines)
        print(f"The number of lines: {total}")

file_path = input()
count_lines(file_path)
'''
#ex - 5
'''
list_of_items = ['I', 'Want', 'to', 'Pass', 'My', 'exams']
def write_list(file_path):
    with open(file_path, 'w') as file:
        for item in list_of_items:
            file.write("%s\n" % item)
file_path = input()
write_list(file_path)
'''
#ex - 6
'''
import string
for letter in string.ascii_uppercase:
    with open(letter + ".txt", 'w') as file:
        file.writelines(letter)
'''
#ex - 7
'''
import shutil
shutil.copyfile('first.txt', 'second.txt')
'''
#ex - 8
file_path = input()
if os.path.exists(file_path):
    if os.access('file_path', os.X_OK):
        os.remove(file_path)
        print(f"File {file_path} deleted")
else:
    print("File is not exist.")