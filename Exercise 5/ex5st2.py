# Learning Python The Hard Way. Exercise 5. Study Drill 2
# Copied by JPoser

name = 'Zed A. Shaw'
age = 35.5 # not a lie
height = 74
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually he's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)