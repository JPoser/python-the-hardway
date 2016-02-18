# Learn Python The Hard Way - Exercise 31: Study Drill
# Written by JPoser

print "You are at a forest: do you #1 walk up the fire road or #2 stand around scratching your arse"

forest = raw_input("> ")

if forest == "1":
	print "You come across a pond with a sign reading /'No Swimming!/'. Do you:"
	print "#1 jump in"
	print "#2 stare at it bemusededly (that is a word honest /'guv)"
	
	pond = raw_input("> ")
	
	if pond == "1":
		print "You jump and hit your face against the frozen pond knocking you out. Womp Womp."
	elif pond == "2":
		print "You freeze to death, womp womp"
	else:
		print "%s is not what I asked you for you fucking dolt" % pond
		
elif forest == "2":
	print "A wild dogger appears! Do you?"
	print "#1 smash him in the face with a small two toned spherical rock"
	print "#2 wonder why he is wearing a fox mask before shrugging your shoulders and walking away"
	
	dogger = raw_input("> ")
	
	if dogger == "1":
		print """You attempt to cave a strangers head in (albeit a sexually deviant stranger)\nbut it turns out to be a pokeball, this\nsummons a charizard who vapourizes your with fire breath. Womp womp"""
	elif dogger == "2":
		print "you leave, never to return."
	else:
		print "Erm, I don't think that's very appropriate do you?"
		
else:
	print "You suck"