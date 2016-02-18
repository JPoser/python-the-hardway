# Learn Python The Hard Way - Exercise 33
# Copied by Joe Poser

i = 0
six = 6
numbers = []

def count(i):
	while i < six:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i +1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "
	
count(i)

for num in numbers:
	print num