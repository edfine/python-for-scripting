# Python has a handful of built in utilities for working with files.
# Perhaps the most important ones are os and pathlib
import os
import pathlib

# NOTE: nowadays almost anything that could be done with the os module
# can be done with the newer (and preferred) pathlib module. However,
# legacy code will likely use the os module. We show both, but know that
# pathlib is preferred when it can be used.

# We can find the location of the currently executing file like this.
# note that __file__ is a special object that always refers to the file
# in which it appears. In this case the file 01-reading-and-writing-files.py
files_dir = os.path.dirname(__file__)
print(files_dir, "\n")

# We can also get the current working directory, which is the directory from
# which we executed the Python code.
cwd = os.getcwd() 
print(cwd, type(cwd), "\n")

# For a variety of reasons, the 'os' module (which treats paths as strings)
# is not preferred, especially if your code needs to run on multiple different
# operating systems. In python 3.6+ we can use the newer pathlib
cwd_path = pathlib.Path.cwd()
print(cwd_path, type(cwd_path), "\n")

# Lets make a new folder called output in the directory containing this file
output_dir = pathlib.Path(files_dir, 'output')
output_dir.mkdir(exist_ok=True)

# Path objects created by the pathlib library can be joined
# using the / operator (instead of the + operator which you'd use 
# for strings, from the os library)
new_file_path = output_dir / 'test_file.txt'
print(new_file_path, '\n')

# Python's "with" keyword does a few things, learn more: https://realpython.com/python-with-statement/
# But when used with files and the built-in open function, it ensures any open file also gets 
# closed properly.

# There are a few modes (see: https://docs.python.org/3/library/functions.html#open)
# but w here stands for "write." Write mode will always REPLACE ALL THE CONTENTS
# of a file.
with open(new_file_path, mode='w') as new_file:
    new_file.write("Hello World!")

# If you want to append to a file, use 'a' mode.
with open(new_file_path, mode='a') as new_file:
    new_file.write("\nOoooo a new line...")

# If you want to read a file, use r mode.
with open(new_file_path, mode='r') as new_file:
    file_text = new_file.read()
    print(file_text)

# Note, there are lots of methods for reading and writing text.
# As well as many "types" of file. You may want to explore them: 
# https://docs.python.org/3/library/io.html#module-io

# Pathlib also supplies it's own method for opening files
# Although it's not significantly different from the built-in function
with new_file_path.open(mode='r') as new_file:
    file_text = new_file.read()
    print(file_text)


# Micro-exercise: create another file in the output directory
# then write some data to it. Afterwards, open the file a second
# time and print the contents to the console.

