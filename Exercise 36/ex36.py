# Learn Python The Hard Way - Exercise 35
# Copied by Joe Poser

from sys import exit

how_much = 0

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input("> ")
	if "0" in next or "1" in next or "2" in next or "3" in next or "4" in next or "5" in next or "6" in next or "7" in next or "8" in next or "9" in next:
		global how_much 
		how_much = int(next)
		gold_int()
	else:
		dead("Man, learn to type a number.")
def gold_int():	
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
			
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def end_times():
	print "You have established a cult that worships the great and evil Cthulu."
	print "Your organisation's influence stretches accross the world."
	print "You have obtained a terrible and ancient artifact."
	print "Do you use the artifact to; sacrifice many lambs, hypnotize the population of the world into becoming Cthulu-Chow (tm) for you evil master or sit in a corner and cry?"

	next = raw_input("> ")

	if "sacrifice" and "lamb" in next:
		dead("Cthulu is angered by your petty worship!")
	elif "hynotize" in next:
		dead("The people of the world become sheeple.")
	elif "cry" in next:
		print "You win!"
		exit(0)
	else:
		dead("You are a terrible cult leader, where are the mass suicide plans?")

def cthulu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life, eat your head or worship the great lord Cthulu?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	elif "worship" in next:
		end_times()
	else:
		cthulu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")

start()
