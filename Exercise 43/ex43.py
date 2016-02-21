class Scene(object):

	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		game_map = scene_map
		game_map.opening_scene()

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
		print "You have a blaster and a Map"
		print "What do you do?"
		action = raw_input("> ")
		if "joke" in action:
			print "Dead"
		elif "fight" in action:
			print "Dead"
		elif "hide" in action:
			print "not Dead"
		else:
			print "Dead"

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Map(object):

	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		corridor = CentralCorridor()
		corridor.enter()
		

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()