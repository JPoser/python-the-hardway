# Learn Python The Hard Way - Exercise 45
# Written by Joe Poser
# Classes for scenes

class Section(object):
	"""Section is the base class for each section of the adventure, 
	it only contains the base function start which will be
	overriden in each section"""
	def start(self):
		pass

class Office(Section):
	"""Section for your office and start of the adventure"""
	def start(self):
		pass

class House(Section):
	"""Section for the blackmailers house"""
	def start(self):
		pass


		