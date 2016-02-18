from sys import exit

def dungeon():
	print "blah blah blah"
	print "If the answer is 42 what times 7 would give me the answer."

	action = raw_input("> ")
	
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	
	if action in numbers:
		int_action = int(action)
	else:
		print "Not a number dumbass"
		dungeon()

	if int_action * 7 == 42:
		print "win"
		exit(0)
	else:
		print "you suck"
print "Dungeon function test"

dungeon()
