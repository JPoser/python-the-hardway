# Learn Python The Hard Way. Exercise 16. Study Drill 2
# Copied by JPoser

print "Please enter the file name:"
file_name = raw_input("> ")

txt = open(file_name, 'r')

print "File contents:"
print txt.read()

txt.close()