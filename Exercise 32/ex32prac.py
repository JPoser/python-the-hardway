# Learn Python The Hard Way - Exercise 32 Practise
# Copied by Joe Poser

fishes = ['perch', 'trout', 'haddock', 'cod', 'halibut']
primes = [2, 3, 5, 7, 11]

for fish in fishes:
	print "%s is a type of fish" % fish
	
for values in primes:
	print "%d is a prime" % values
	
print " "

print "What is the meaning of life?"

life = raw_input("> ")

while life != "42":
	print "No it's 42 try again." 
	life = raw_input("> ")
	
print "But what is the question?"