# Learn Python The Hard Way. Exercise 5.
# Copied by JPoser

# Assigns x to a string and inserts the int 10
x = "There are %d types of people." % 10
# Assigns variable to a string
binary = "binary"
# Assigns variable to a string
do_not = "don't"
# Assigns y to a string and inserts two previous variables which are also strings
y = "Those who know %s and those who %s." % (binary, do_not)

# prints variable
print x
# prints variable
print y

# prints string which includes formatter or nested string
print "I said: %r." % x
# prints string which includes formatter or nested string
print "I also said: '%s'." % y

# assigns variable to boolean value
hilarious = False
# assigns variable to string containing a formatter
joke_evaluation = "Isn't that joke so funny?! %r"

# prints variable joke evaluation with nested variable (boolean)
print joke_evaluation % hilarious

# Assigns variable to a string
w = "This is the left side of..."
# Assigns variable to a string
e = "a string with a right side."

# prints concatenation of two variables 
print w + e