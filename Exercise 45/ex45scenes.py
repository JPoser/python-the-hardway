# Learn Python The Hard Way - Exercise 45
# Written by Joe Poser
# Classes for sections

class Section(object):
	"""Section is the base class for each section of the adventure, 
	it only contains the base function start which will be
	overriden in each section"""
	def start(self):
		pass

class Office(Section):
	"""Section for your office and start of the adventure"""
	def start(self):
		print "I was sat in my office when she walked in,"
		print "the rain was lashing down like lead in a shoot out."
		print "I was looking busy flicking through old post, mostly unpaid bills, and had nearly run out of scotch."
		print "'What are you looking for?' I asked."
		print "'Someone to find out who's blackmailing me' she said."
		print "She looked like trouble and lots of it."
		print "I could tell her to get lost now and buy another bottle or take her money."
		action = False
		while action == False:
			response = raw_input("> ")
			if "help" in response:
				print "I decided to help her on account of those unpaid bills."
				print "'My costs are fifteen dollars a day' I told her"
				print "She looked relieved 'Whatever you need, all I have to go on so far are the notes they've been sending me'"
				print "I took a good look at the notes and recognised the letter head they were sent on."
				print "'I have an idea where these are coming from' I mumbled thinking aloud"
				print "'Your going to be making me work for my money tonight'"
				print "I headed east on 45th with the remainders of my scotch and a .38 on a hunch and a prayer"
				action = True
				return "house"
			elif "lost" in response:
				print "'This isn't worth the heat it's going to draw me' I said not looking up from my papers."
				print "'In my experience it's always best to just pay whoevers turning the screw on you'"
				print "She didn't even try and argue, turned around and walked straight out of the door."
				print "Outside the rain stopped."
				action = True
				return "case cold"
			else:
				print "I need to decide if i'm going to 'help her' or tell her to 'get lost'"
				action = False

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
		return "case closed"

class CaseClosed(Section):
	"""Win state"""
	def start(self):
		print "Case Closed..."
		exit(1)

class CaseCold(Section):
	"""Survival failure state"""
	def start(self):
		print "The trail went cold"
		exit(1)

class Dead(Section):
	"""Death failure state"""
	def start(self):
		print "you died"
		exit(1)