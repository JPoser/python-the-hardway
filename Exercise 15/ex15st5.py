# Learn Python The Hard Way. Exercise 15. Study Drill 5
# Copied by JPoser

print "Type your filename:"
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()