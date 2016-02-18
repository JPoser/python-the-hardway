# Learn Python The Hard Way. Exercise 19. Study Drill 1.
# Copied by JPoser

# sets function cheese_and_crackers to the arguments cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# Prints string with formatter linked to variable cheese_count
	print "You have %d cheeses!" % cheese_count
	# prints string with variable linked to boxes of crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# prints a string
	print "Man that's enough for a party!"
	# prints a banterous string
	print "Get a blanket. \n"

# prints a string explaining what happens in the function to the user
print "We can just give the function numbers directly:"
# calls function cheese and cracker and sets the arguments to 20 and 30
cheese_and_crackers(20, 30)

# prints a string explaining what happens in the function to the user
print "OR, we can use variables from our script:"
# sets variable amount_of_cheese to the integer 10
amount_of_cheese = 10
# sets the variable amount_of_crackers to the integer 50
amount_of_crackers = 50

# calls function cheese and cracker and sets the arguments to the variables
# amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a string explaining what happens in the function to the user
print "We can even do math inside too:"
# calls function cheese and cracker and sets the arguments to 
# the sum of (10 & 20) and (5 & 6)
cheese_and_crackers(10 + 20, 5 + 6)

# prints a string explaining what happens in the function to the user
print "And we can combine the two, variables and math:"
# calls function cheese and cracker and sets the arguments a combination
# of variables and integers with maths
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)