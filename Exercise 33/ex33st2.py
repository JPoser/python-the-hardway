# Learn Python The Hard Way - Exercise 33 study drill 2
# Copied by Joe Poser

# sets value of int to 2
i = 2
# sets value of max to int 10
max = 10
# sets the value of numbers to a blank list
numbers = []

# creates function count to be run on i
def count(i):
	# runs a while loop while statement i < max is true
	while i < max:
		# while above statement is true prints string
		print "At the top i is %d" % i
		# adds value of i to the list numbers
		numbers.append(i)
		
		# adds 1 to the previous value of i
		i = i + 1
		# prints a string
		print "Numbers now: ", numbers
		# prints another string
		print "At the bottom i is %d" % i
	# prints yet another string 
	print "The numbers: "

# runs function count on variable i	
count(i)

# runs a for loop on list numbers 
for num in numbers:
# prints list numbers
	print num