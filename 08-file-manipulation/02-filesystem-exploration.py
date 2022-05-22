# Sometimes we want to navigate a filesystem, Python can do that too!
# We are only showing the pathlib way of doing things this time, but 
# there are similar features in the older os module which you may find
# used in legacy code.
import pathlib

# First, using pathlib to explore the hierarchy in "example folder"
files_dir = pathlib.Path(__file__).parent.absolute()

# We want to explore the "example_folder"
e_folder = files_dir / 'example_folder'

# Loop over the files in that folder
for child_path in e_folder.iterdir():
    print(child_path)

# If you want to search recursively, use rglob or glob methods.
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob
# https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
print()
for child_path in e_folder.rglob('*'):
    print(child_path)

# Perhaps you only care about text files, then you can use the pattern
# (* in the previous example) to indicate as much:
print()
for child_path in e_folder.rglob('*.txt'):
    print(child_path)

# Micro-exercise: Write some code that recursively searches through 
# the example_folder hierarchy and print the contents of files
# that contain the word "are" as well as the filepath to that file