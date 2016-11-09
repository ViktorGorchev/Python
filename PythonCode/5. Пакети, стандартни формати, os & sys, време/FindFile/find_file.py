import sys
import os

#python find_file.py C:/Users/Admin/Desktop/PythonFiles/ me.jpg
def find_file(dir, filename):
    file_is_not_found = True

    for dir_path, dir_names, file_names in os.walk(dir):
        for name in file_names:
            if name == filename:
                print('File found.')
                print(dir_path + name)
                file_is_not_found = False

    if file_is_not_found:
            print('File not found!')

if len(sys.argv) < 3:
    print("Please provide at least 3 parameters")
else:
    find_file(dir=sys.argv[1], filename=sys.argv[2])