# Learn Python The Hard Way - Exercise 31
# Copied by JPoser

# Prints a line 
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

# creates a variable door and sets its value to user input with the prompt "> "
door = raw_input("> ")

# checks to see if the variable door has been set to the string "1"
if door == "1":
# if above is True prints a line
	print "There's a giant bear here eating cheese cake. What do you do?"
	# prints a line
	print "1. Take the cake."
	# prints a line
	print "2. Scream at the bear."
	
	# creates a variable bear and sets its value to user input with the prompt "> "
	bear = raw_input("> ")
	
	# checks if variable bear has been set to the string "1" 
	if bear == "1":
	# if above is True then prints a line
		print "The bear eats your face off. Good job!."
	# checks to see if the variable bear has been set to the string "2"
	elif bear == "2":
	# if above is True then prints a line
		print "The bear eats your legs off. Good job!."
	# if neither is true runs the code below
	else:
	# prints a line
		print "Well doing %s is probably better. Bear runs away." % bear
		
# checks if the variable door has been set to the string "2"
elif door == "2":
# if above is True then prints lines below
	print "You stare into the endless abyss at Cthulu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	# creates the variable insanity and asks for user input 
	insanity = raw_input("> ")
	
	# checks if the variable is set to either "1" or "2", if either is True then runs code below
	if insanity == "1" or insanity == "2":
	# if above is True then prints the line below
		print "Your body survives powered by a mind of jello. Good job!"
	# if neither is True (insanity is set to any string but "1" or "2") runs code indented below	
	else:
	# prints a line if above is true
		print "The insanity rots your eyes into a pool of muck. Good job!"
# if door is set to anything but "1" or "2" runs code below		
else :
# if above is True prints a line
	print "You stumble around and fall on a knife and die. Good job!"