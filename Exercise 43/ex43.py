# Learn Python The Hard Way - Exercise 43
# Modified by Joe Poser
# Object Oriented Design

# How selecting the next scene works. 

# There are two classes that control the flow of scenes. The Map defines which scene will be slected 
# next from a dictionary containing strings related to classes. It contains a hard coded variable for the dictionary, an init method 
# to define the opening scene, a method to get the opening scene from the dictionary and a method for getting the next scene from the dictionary.

# Next_scene() takes two arguments self because it's a class method and scene_name. scene_name gets run against the dictionary as a variable,
# this then returns the next scene class. Opening scene just calls next_scene with the argument start_scene to get the opening scene.

# The Engine provides the main loop to keep running scenes until it reaches scene finished defined by the variable last_scene which holds
# the class Finished(). current_scene is set to the opening_scene from the map and then a loop is defined which will keep getting the next scene
# and running it's method enter() until it reaches the last_scene which is finished.


import time

class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter()


class Death(Scene):

	def enter(self):
		print "You are dead, so it goes."
		return 'finished'

class CentralCorridor(Scene):

	def enter(self):
		print "You are in a corridor on a space craft."
		print "There is a Gothon in front of you."
		print "Gothons don't have a sense of humour and like to vapourise humans."
		print "You have a blaster and a laser map"
		print "what do you do?"
		action = raw_input("> ")
		if "joke" in action:
			return 'death'
		elif "fight" in action:
			return 'death'
		elif "hide" in action:
			print "The Gothon is blinded by your laser map."
			print "This gives you a 21 second window to escape."
			print "you duck a left into the Laz0r Armory.\n\n"
			return "laser_weapon_armory"
		else:
			return 'death'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "You are in the Laz0r Armory."
		print "There is a handy looking Neutron Bomb mounted on a wall rack."
		print "Access to it is protected by a keypad."
		print "The numbers 3, 7 and 2 are faded."
		print "There is a warning sign in Gothon that says if you get the wrong password\n3 times you will be ejected into space"
		attempts = 3
		while attempts != 0:
			attempt = raw_input("> ")
			if attempt == "732":
				break
			else:
				attempts -= 1
		if attempts == 0:
			return 'death'
		else:
			return 'the_bridge'

class TheBridge(Scene):

	def enter(self):
		print "You are on the Bridge"
		print "The Gothon Commander is by the command console."
		print "He does not look happy to see you"
		print "He grunts 'What are you doing here, and is that a neutron bomb!'"
		print "You have a choice: either throw the bomb at the Commander,\nshoot him with your blaster,\nor tell him the funniest joke in the world."
		action = raw_input("> ")
		if "joke" in action:
			print "You say:"
			time.sleep(1)
			print "'What goes Ha Ha Bonk?'"
			time.sleep(1)
			print "The Gothon Commander retorts:"
			time.sleep(1)
			print "'This is your plan, Ha Ha Ha'"
			time.sleep(1)
			print "He raises his blaster"
			time.sleep(1)
			print "Realising your mistake, you snap shoot him towards the cranial region"
			time.sleep(1)
			print "..."
			time.sleep(1)
			print "His head falls off"
			time.sleep(1)
			print "..."
			time.sleep(1)
			print "'A Gothon laughing his head off' you quip"
			print "You plant the Neutron bomb and dash towards the Escape Pods"
			return 'escape_pod'
		else:
			return 'death'

class EscapePod(Scene):

	def enter(self):
		print "When you arrive all but 1 of the ships escape pods are taken by fleeing Gothons"
		print "Before leaving the Gothons have sabotaged the indicators showing if a pod has been fired."
		print "This means if you get the wrong hatch you will be sucked out into space and pop like an overinflated baloon"
		button_selected = False
		while button_selected == False:
			print "You must choose between escape pod A, B or C"
			valid_actions = ["A", "B", "C"]
			action = raw_input("> ")
			cap_action = action.capitalize()
			if cap_action in valid_actions:
				button_selected = True
			else:
				button_selected = False
		if cap_action == "A":
			print "Congratulations you win"
			return 'finished'
		elif cap_action == "B":
			return 'death'
		elif cap_action == "C":
			return 'death'
		else:
			return 'death'

class Finished(Scene):
	def enter(self):
		print "The End"
		#return 'finished'

class Map(object):
	scenes = {
	'central_corridor' : CentralCorridor(),
	'laser_weapon_armory' : LaserWeaponArmory(),
	'the_bridge' : TheBridge(),
	'escape_pod' : EscapePod(),
	'death' : Death(),
	'finished' : Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
			val = self.scenes.get(scene_name)
			return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
# Debug code for Map() class
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

