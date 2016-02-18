# Learn Python The Hard Way - Exercise 36 Homework
# Copied by Joe Poser

from sys import exit


def dungeon():
	print "Your quest is nearly at an end."
	print "In the dungeon is a bear."
	print "The bear can talk, it asks you a riddle:"
	print "\"If the answer is 42 what times 7 would give me the answer.\""

	action = raw_input("> ")
	
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	
	if action in numbers:
		int_action = int(action)
	else:
		print "Bear - \"That's not a number dumbass\""
		dungeon()

	if int_action * 7 == 42:
		print "You win!"
		exit(0)
	else:
		dead("Learn your times tables!")

def nord_keep():
	print "You are inside the keep and in front of you is an Imperial Legionaire"
	print "\nYou may; lunge, block or charge with your sword"

	action = raw_input("> ")

	if "lunge" in action:
		dead("Lunging at the Imperial Guard with a two handed blade wasn't smart.")
	elif "block" in action:
		print "You hold your sheild up deflecting a swing from the soldier\n"
		nord_keep()
	elif "charge" in action:
		print "You banzai charge at the Legionaire knocking him off his feet and from his sences."
		print "The door to the dungeon is now open.\n"
		dungeon()
	else:
		print "What is %s?" % (action)
		nord_keep()

def elf_keep():
	print "You are an elf inside a keep, ahead is an Imperial Legionary. His sword is drawn."
	print "\nDo you do a little dance, cast a little love or sneak down tonight?"
	print "You can also try and attack him but you are an elf, which is basically a fantasy hippy."

	action = raw_input("> ")

	elf_dead_actions = ["prance", "dance", "tickle", "hug", "attack"]
	elf_success_actions = ["cast", "sneak"]

	if action in elf_dead_actions:
		dead("You attempt to attack the soldier through the ancient Elf art of prancing.\n It's not very effictive and mostly involves dancing, tickling or hugging.\nThe soldier strikes you down and you become more powerful than he could possibly imagine.")
	elif action in elf_success_actions:
		dungeon()
	else:
		print "prompt again"
		elf()

def nord():
	print "The guard says \"So you are a Nord, you should no better than to \nchallenge the might of the Empi.....\""
	print "Before the guard could finish his taunt, a massive winged drake \ndescends from above disrupting the execution. In the confusion you escape"
	print "However on running for cover you encounter the dragon, standing \non it's hind legs between you and the door"
	print "\nDo you attack the massive lizard head on, try and cast a spell \nof dragon-cide or attempt to sneak past it?"

	action = raw_input("> ")
	
	if "attack" in action:
		print """You lunge at the dragon head on with your b****** sword held high!\nThe dragon somewhat fortuitously gets distracted by a passing peasent.\n You read a keep and quickly enter bolting the heavy wooden door behind you.\nBecasue we all know wood is the best defence against fire..."""
		nord_keep()
	elif "cast" in action:
		dead("""You wave your hand's around like a lion doing the Mick Jagger \nuntil your realise your a Nord and suck at magic.\nThe dragon swats you like a lion dancing the Mick Jagger.""")
	elif "sneak" in action:
		dead("You attempt to slyly creep past a dragon. You sissy. BBQ'd Nord is on the menu for the dragon's dinner")
	else:
		dead("You thought %s would save you from a fire breathing king of lizards? You deserve all that's coming to you, mostly fire.")

def elf():
	print "The guard says \"So you are an Elf, you should no better than to challenge the might of the Empi.....\""
	print "Before the guard could finish his taunt, a massive winged drake \ndescends from above disrupting the execution. In the confusion you escape"
	print "However on running for cover you encounter the dragon, standing \non it's hind legs between you and the door"
	print "\nDo you attack the massive lizard head on, try and cast a spell \nof dragon-cide or attempt to sneak past it?"

	action = raw_input("> ")

	elf_dead_actions = ["prance", "dance", "tickle", "hug", "attack"]
	elf_success_actions = ["cast", "sneak"]

	if action in elf_dead_actions:
		print dead("You died")
	elif action in elf_success_actions:
		elf_keep()
	else:
		print "prompt again"
		elf()

def dead(x):
	comment = x
	print "%s - So it goes." % (comment)

# This is the start of the adventure, there is an easter egg if the player types Dhovakiin!
def helgen():
	print "The guard asks if you are a Nord or an Elf under your hood?"

	player = raw_input("> ")

	if player == "Nord":
		nord()
	elif player == "Elf":
		elf()
	elif player == "Dhovakiin":
		dead("The guard says \"He's obviously mad, execute him!\"")
	else:
		print "The guard comments \"You don't look like a %s, be honest with me.\"" % (player)

		helgen()

print "You have been captured by the Imperial Legion."
print "You have been brought on a cart to Helgen."
print "You are thought to be a member of the Stormcloak rebellion,"
print "and you are to be executed..."

helgen()
