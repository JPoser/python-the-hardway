# Learn Python The Hard Way - Exercise 30
# Copied by JPoser

# Sets the value of people to 30
people = 30
# Sets the value of cars to 40
cars = 40
# Sets the value of buses to 15
buses = 15

# Checks if cars are greater than people
if cars > people:
# If cars are greater than people prints this string
	print "We should take the cars."
# Checks if cars are less than people 
elif cars < people:
# If cars are less than people prints this string
	print "We should not take the cars."
# Checks if neither cases are true (cars equal people)
else:
# if so prints this line
	print "We can't decide."

# Checks if buses are greater than cars	
if buses > cars:
# if so prints this string
	print "That's too many buses."
# checks if buses are less than cars
elif buses < cars:
# if so prints this string
	print "Maybe we could take the buses."
# if neither (buses = cars)
else:
# prints this string
	print "We still can't decide."

# checks if people are greater than buses
if people > buses:
# if so prints this string
	print "Alright, let's just take the buses."
# checks if either people are less than buses or the same
else: 
# prints this string
	print "Fine, Let's stay home then."