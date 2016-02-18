# Learn Python The Hard Way. Exercise 15. Study Drill 4
# Copied by JPoser

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()