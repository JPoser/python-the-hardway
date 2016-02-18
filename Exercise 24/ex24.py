# Learn Python The Hard Way - Exercise 24
# Copied by JPoser

print "Let's practise everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern the \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# Sets variable to 10000
start_point = 10000
# Runs function secret_formula using the previously set variable (start_point) as its argument.
# Function does maths and returns 3 numbers which are then set to the 3 variables at the 
# start if the statement
beans, jars, crates = secret_formula(start_point)

print "With a starting point of %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Changes the value of start point and then runs the formula
start_point = start_point / 10

print "We can also do that this way:"
# Returns 3 values so this running the function in line works, Looks nicer uses less lines of code
# I prefer this way.
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)