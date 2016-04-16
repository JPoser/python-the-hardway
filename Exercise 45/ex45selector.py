# Learn Python The Hard Way - Exercise 45
# Written by Joe Poser
# State Machine for State Setting
import ex45scenes

class SectionMap(object):
	sections = {
		"office" : ex45scenes.Office()
		"house" : ex45scenes.House()
		"tail" : ex45scenes.Tail()
		"crony" : ex45scenes.Crony()
		"interrogation" : ex45scenes.Interrogation()
		"murderer" : ex45scenes.Murderer()
		"case closed" : ex45scenes.CaseClosed()
		"case cold" : ex45scenes.CaseCold()
		"dead" : ex45scenes.Dead()
	}

	def __init__ (self):
		pass

	def next_stage(self, section_name):
		pass

	def first_stage(self, opening_stage):
		pass


class SceneSelector(object):
	pass