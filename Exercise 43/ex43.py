import time

class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		game_map = scene_map
		game_map.opening_scene()
		game_map.next_scene()

	def play(self):
		pass

class Death(Scene):

	def enter(self):
		print "You are dead, so it goes."

class CentralCorridor(Scene):

	def enter(self):
		print "You are in a corridor on a space craft."
		print "There is a Gothon in front of you."
		print "Gothons don't have a sense of humour and like to vapourise humans."
		print "You have a blaster and a laser map"
		print "what do you do?"
		action = raw_input("> ")
		if "joke" in action:
			print "Dead1"
		elif "fight" in action:
			print "dead2"
		elif "hide" in action:
			print "not Dead"
			self.hidden()
		else:
			print "Dead3"
	
	def hidden(self):
		print "The Gothon is blinded by your laser map."
		print "This gives you a 21 second window to escape."
		print "you duck a left into the Laz0r Armory.\n\n"
		return "laser_weapon_armory"

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
			print "DEBUG: Dead"
		else:
			print "NEXT LEVEL"
			next_level = TheBridge()
			next_level.enter()

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
			next_level = EscapePod()
			next_level.enter()
		else:
			print "debugbridge: DEAD"

class EscapePod(Scene):

	def enter(self):
		print "When you arrive all but 1 of the ships escape pods are taken by fleeing Gothons"
		print "Before leaving the Gothons have sabotaged the indicators showing if a pod has been fired."
		print "This means if you get the wrong hatch you will be sucked out into space and pop like an overinflated baloon"
		print "You must choose between escape pod A, B or C"
		action = raw_input("> ")
		# To do, santise action so string is always in caps aka CRUISE CONTROL FOR COOL!
		if action == "A":
			print "Success"
		elif action == "B":
			print "Death by vaccum"
		elif action == "C":
			print "Death by vaccum"
		else:
			print "Death by Neutron radiation"

class Map(object):

	def __init__(self, start_scene):
		start = start_scene

	def next_scene(self, scene_name):
			scene_map = {
			'central_corridor' : CentralCorridor(),
			'laser_weapon_armory' : LaserWeaponArmory(),
			'the_bridge' : TheBridge(),
			'escape_pod' : EscapePod(),
			}
			next_level = scene_map[scene_name]
			next_level.enter()

	def opening_scene(self):
		self.next_scene('central_corridor')
		
		

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()