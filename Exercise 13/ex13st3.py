# Learn Python The Hard Way. Exercise 13.
# Copied by JPoser

from sys import argv

script, first, second, third, bitchin = argv
user = raw_input("Type some shit: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "And for my final trick here is your shit - %s:" % user, bitchin