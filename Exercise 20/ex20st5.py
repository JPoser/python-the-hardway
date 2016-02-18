# Learn Python The Hard Way. Exercise 20.
# Copied by JPoser

# From package sys import script argv
from sys import argv

# sets variable input_file to the script argv
script, input_file = argv

# Creates function print_all using the variable f which is used for a file
def print_all(f):
# prints read file 
	print f.read()

# Creates a function called rewind
def rewind(f):
# sets the line of the file to line 0
	f.seek(0)
	
# Creates a function print_a_line using the variables file and line_count
def print_a_line(line_count, f):
# prints variables line count and a single file set by readline
	print line_count, f.readline()
	
# sets current_file to the input file	
current_file = open(input_file)

# prints string
print "First let's print the whole file:\n"

# runs script print all on variable current file
# this prints the all data in the file
print_all(current_file)

# prints string
print "Now let's rewind, kind of like a tape."

# "rewinds" the file moving it back to the beginning ready to be 
# read again 
rewind(current_file)

# prints string
print "Let's print three lines:"

# sets variable current_line to 1
current_line = 1
# runs script print a line using variable current line and the variable current_file
# this prints the first line
print_a_line(current_line, current_file)

# sets the variable current line to the sum of the previous value + 1 (2)
current_line += 1
# runs script print a line using variable current line and the variable current_file
# this prints the second line
print_a_line(current_line, current_file)

# sets the variable current line to the sum of the previous value + 1 (3)
current_line += 1
# runs script print a line using variable current line and the variable current_file
# this prints the third line
print_a_line(current_line, current_file)