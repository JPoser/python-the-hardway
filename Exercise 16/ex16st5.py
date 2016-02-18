# Learn Python The Hard Way. Exercise 16.
# Copied by JPoser

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN,"

raw_input("?")

# No need to truncate file as write mode will do this if it encounters 
# a file of the same name
print "Opening the file..."
target = open(filename, 'w')

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s" % (line1, line2, line3))

print "And finally, we close it."
target.close()