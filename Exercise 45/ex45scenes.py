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
		print "In the office"
		return "house"

class House(Section):
	"""Section for the blackmailers house"""
	def start(self):
		print "In the house"
		return "tail"

class Tail(Section):
	"""Section for tailing the perp"""
	def start(self):
		print "On the tail"
		return "crony"

class Crony(Section):
	"""Section for the first encounter with an armed Crony"""
	def start(self):
		print "Fighting the crony"
		return "interrogation"
		
class Interrogation(Section):
	"""Section where you interrogate the perp"""
	def start(self):
		print "Interrogating the crony"
		return "murderer"

class Murderer(Section):
	"""Final Section where you encounter the Murderer"""
	def start(self):
		print "Fighting the murderer"
		return "caseclosed"

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