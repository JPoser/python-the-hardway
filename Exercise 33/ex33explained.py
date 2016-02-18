# Learn Python The Hard Way - Exercise 33
# Copied by Joe Poser

# sets the variable i to int 0
i = 0
# creates variable numbers with a blank list attached
numbers = []

# runs a code indented below while statement 'i < 6' is True
while i < 6:
	# while above is true prints string
	print "At the top i is %d" % i
	# adds variable i to the list numbers
	numbers.append(i)
	
	# adds 1 to previous value of i
	i = i + 1
	# prints list in its current state
	print "Numbers now: ", numbers
	# prints the value of i after the it has had 1 added to it on line 17
	print "At the bottom i is %d" % i

# prints variable i
print "\nThe final value of i is: %d\n" % i
	
# prints string
print "The numbers: "

# runs a for loop until values in the list numbers end
for num in numbers:
	# prints the loop results
	print num