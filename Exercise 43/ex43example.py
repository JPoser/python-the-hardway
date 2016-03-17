import time

class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		print current_scene
		last_scene = self.scene_map.next_scene('finished')

		#current_scene.enter()

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
			print "not Dead"
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
				print "sucess"
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
			#time.sleep(1)
			print "'What goes Ha Ha Bonk?'"
			#time.sleep(1)
			print "The Gothon Commander retorts:"
			#time.sleep(1)
			print "'This is your plan, Ha Ha Ha'"
			#time.sleep(1)
			print "He raises his blaster"
			#time.sleep(1)
			print "Realising your mistake, you snap shoot him towards the cranial region"
			#time.sleep(1)
			print "..."
			#time.sleep(1)
			print "His head falls off"
			#time.sleep(1)
			print "..."
			#time.sleep(1)
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
		print "You must choose between escape pod A, B or C"
		action = raw_input("> ")
		# To do, santise action so string is always in caps aka CRUISE CONTROL FOR COOL!
		if action == "A":
			return 'finished'
		elif action == "B":
			return 'death'
		elif action == "C":
			return 'death'
		else:
			return 'death'

class Finished(Scene):
	def enter(self):
		print "Yay you win!"
		return 'finished'

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

