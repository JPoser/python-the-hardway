# Learn Python The Hard Way. Exercise 11. Study Drill 2.
# Copied by JPoser

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "What is your name?",
name = raw_input()

print "Ok %r, you are %r short, %r mug and %r fat." % (name, height, age, weight)