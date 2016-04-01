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

class Trail(Section):
	"""Section for tailing the perp"""
	def start(self):
		pass

class Crony(Section):
	"""Section for the first encounter with an armed Crony"""
	def start(self):
		pass
		
class Interrogation(Section):
	"""Section where you interrogate the perp"""
	def start(self):
		pass

class Murderer(Section):
	"""Final Section where you encounter the Murderer"""
	def start(self):
		pass

class CaseClosed(Section):
	"""Win state"""
	def start(self):
		pass

class CaseCold(Section):
	"""Survival failure state"""
	def start(self):
		pass

class Dead(Section):
	"""Death failure state"""
	def start(self):
		pass

		