# Learn Python The Hard Way - Exercise 33 study drill 2
# Copied by Joe Poser

i = 2
max = 10
numbers = []
increase = 2

def count(i):
	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increase
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "
	
count(i)

for num in numbers:
	print num