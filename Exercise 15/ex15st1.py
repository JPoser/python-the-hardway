# Learn Python The Hard Way. Exercise 15. Study Drill 1.
# Copied by JPoser

# Imports to add a feature to the python script the feature argv or "argument variable"
# argv holds arguments that you state when you run the script. In this case a txt file.
from sys import argv

# Sets the variable filename to whatever was specified as argv when the script was run
script, filename = argv

# Sets the variable to open the variable filename (this is the argv specified filename)
txt = open(filename)

# Prints a string with a formatter pointing to variable filename. (Will print the name of the 
# file specified by argv)
print "Here's your file %r:" % filename
# Prints the variable txt with the command read. This prints the contents of the file that was 
# opened on line 12
print txt.read()

# Prints a string which prompts the user to type the filename again
print "Type the filename again:"
# Sets the variable file_again to raw_input with the prompt "> ". 
file_again = raw_input ("> ")

# Sets the variable txt_again to open the variable file_again
txt_again = open(file_again)

# Prints the variable txt_again with the command read()
print txt_again.read()