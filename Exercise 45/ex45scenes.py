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
		print "she was wearing a red dress."
		print "The rain was lashing down like hot lead bouncing off concrete."
		print "I was looking busy flicking through old post, mostly unpaid bills, and had nearly run out of scotch."
		print "'What are you looking for?' I asked."
		print "'Someone to find out who's blackmailing me' she said."
		print "She looked like trouble and lots of it."
		print "I could have told her to get 'lost' now and buy another bottle\nor 'help' her and go after another scumbag despite hundreds of others ready to take his place."
		
		action = False
		
		while action == False:

			response = raw_input("\n> ")

			if "help" in response:

				print "I decided to help her on account of those unpaid bills."
				print "'My costs are fifteen dollars a day' I told her"
				print "She looked relieved 'Whatever you need, all I have to go on so far are the notes they've been sending me'"
				print "I took a good look at the notes and recognised the letter head they were sent on."
				print "It read 'Michael Finnagen, talent agent'. I knew him better as Micky Fin, hustler"
				print "'I know where these are coming from' I mumbled."
				print "'Your going to be making me work for my money tonight'"
				print "I headed east on 45th with the remainders of my scotch and a .38 on a hunch and a prayer"
				
				action = True

				return "murder"

			elif "lost" in response:

				print "'This isn't worth the heat it's going to draw me' I said not looking up from my papers."
				print "'In my experience it's always best to just pay whoevers turning the screw on you'"
				print "She didn't even try and argue, turned around and walked straight out of the door."
				print "Outside the rain stopped."

				action = True

				return "case cold"

			else:

				print "That's not what I happened I either 'help her' or tell her to 'get lost'"


class Murder(Section):
	"""Section for the blackmailers house"""
	def start(self):

		print "\n"
		print "I drove to the office block on the east side of the city."
		print "The rain lashed my overcoat and soaked me through."
		print "I stopped on the way to pick up another bottle of scotch and a pack of ciggerates."
		print "As I walked through the empyty lobby I heard the repetative dull thuds of  gunshots echoing through concrete."
		print "I ran to the elevator and thumped the button for the floor."
		print "As the doors opened I saw a door kicked off it's hinges."
		print "I cautiously walked into the room and found a body slouched over the desk."
		print "Blood was dripping off the desk onto the floor."
		print "Behind me I heard the quick thud of a man running down the hall and down the stairwell."
		print "I could have lingered to 'look' for clues but I had a hunch I'd learn more by giving 'chase'\nand catching whoever was fleeing the scene and persuading him to tell me what he knew."
		
		action = False
		
		while action == False:

			response = raw_input("\n> ")

			if "chase" in response:

				print "I gave chase down the stairwell. I could hear the perp up aheads footsteps get faster."
				print "At the bottom of the stairs I saw a man in a brown overcoat jump into a buick and drive away."
				print "I ran round the corner to my convertable and attempted to tail him."
				
				action = True

				return "tail"
			elif "look" in response:

				print "I decided that leaving a crime scene this fresh was a mistake."
				print "A name badge on the table read 'Michael Finnagen, talent agent'"
				print "But the man on the desk wasn't Micky."
				print "He'd been shot 3 times in the chest and was already past living."
				print "I had no idea who could have shot him but had a hunch that Micky didn't want to be found."
				print "I knew then that I'd never find him."

				action = True

				return "case cold"

			else:
				print "That won't help did I 'chase' after the perp or look for clues?"

class Tail(Section):
	"""Section for tailing the perp"""
	def start(self):

		print "\n"
		print "It was still raining as I drove away but I caught a glimpse of his taillights turning east towards Hollywood."
		print "The canvas roof of my convertable "
		print "I followed and sat two cars back until we arrived at 64th bullevard."
		print "He pulled over to the left hand lane and waited at the traffic lights."
		print "I could have 'pulled up' along side him, or follow him thinking he'd turn 'left'"
		
		action = False
		
		while action == False:
			response = raw_input("\n> ")
			if "pulled up" in response:
				print "I pulled alonside the buick and the driver glanced at me."
				print "Before I could react the driver sped off in a cloud of smoke."
				print "I was never going to catch him."
				action = True
				return "case cold"
			elif "left" in response:
				print "I stayed behind him waiting to see what he did."
				print "As he turned left I followed him."
				action = True
			else:

				"That's not what happened, I could have 'pulled up' next to him or waited behind him to see if he turned 'left'"

		print "As I followed the car up into the Hollywood hills I saw the driver turn around."
		print "He made a sudden wild turn cutting across traffic and into a road that I knew was a dead end."
		print "I had to stay on his tail but if I attempted the same manouvre I could have ended up causing a major pile up."
		print "I could either 'brake hard' and follow him or 'drive on' and turn around at the next set of of lights."
		
		action = False
		
		while action == False:

			response = raw_input("\n> ")

			if "brake hard" in response:

				print "I broke hard and cut across on coming traffic."
				print "I saw the buick parked in front of a derilict looking house further up the road."
				print "Getting out of the car I pulled out my gun and headed towards the house."
				return "crony"

			elif "dive on" in response:

				print "I couldn't cut across that much traffic without killing myself"
				print "and anyone who hit me."
				print "At the next set of lights I made a U turn" 
				print "but by the time I got to the street the buick was no-where to be seen."
				return "case cold"

			else:

				print "I didn't do that, I could have either 'brake hard' or 'drive on'"

class Crony(Section):
	"""Section for the first encounter with an armed Crony"""
	def start(self):

		print "\n"
		print "I crept around the back of the house and looked for an open window."
		print "All but one was borded up but the one that wasn't was wide open."
		print "I carefully climbed inside, gun in hand."
		print "The creep was in the next room sat on the sofa pointing a his pistol at the door."
		print "I had the drop on him and wanted to find out what he knew."
		print "The gun was in my hand so I could 'shoot' him right now,"
		print "attempt to 'talk' him down or sucker 'punch' him."
		
		action = False

		while action == False:

			response = raw_input("\n> ")

			if "shoot" in response:

				print "I aimed at his arm to try and make him drop his weapon."
				print "I squeezed the trigger."
				print "He yelled and the gun dropped to the floor."
				print "'Freeze punk!' I yelled."
				print "He scowled and dived for the gun."
				print "I shot him twice more."
				print "He didn't get up."
				print "Getting information out of him now would prove challenging."
				action = True
				return "case cold"

			elif "talk" in response:
				print "I calmly told him to 'drop the gun'."
				print "That wasn't what he did."
				print "He wheeled around a fired wildly."
				print "I shot in response but we were both done for."

				action = True

				return "dead"

			elif "punch" in response:

				print "I lept at him at hit him squarly in the jaw."
				print "He dropped the gun and I grabbed it."
				print "Wheeling around I pointed my .38 at him."
				print "'Start talking' I growled."
				action = True

				return "interrogation"
			else:
				print "That's not what happened."
		
class Interrogation(Section):
	"""Section where you interrogate the perp"""
	
	hitpoints = 3

	def start(self):

		print "\n"
		print "'Who are you and why did you shoot Micky?'."
		print "The creep coughed and spat at me 'Go to hell'."
		print "I was in two minds whether to 'hit' him to get him to talk, or 'ask' where Micky is."

		action = False

		while action == False or self.hitpoints != 1:
		
			response = raw_input("\n> ")

			if "hit" in response and self.hitpoints == 3:
				print "I hit him with the but of my pistol"
				print "He coughed reeled but still stared at me with eyes full of hate"
				self.assault()

			elif "hit" in response and self.hitpoints == 2:
				print "I hit him again."
				self.assault()

			elif "hit" in response and self.hitpoints == 1:
				print "He collapsed"
				self.assault()
				return "case cold"

			elif "ask" in response and self.hitpoints == 3:
				print "'Go to hell' was all he had to say to me"

			elif "ask" in response and self.hitpoints == 2:
				print "'Alright stop, I'll tell you' the murderer couged."
				print "'He's hiding out in south bay, he runs a warehouse over there."
				print "I cuffed him to a radiator, got in my car and set off for south bay."
				return "murderer"

			else:
				print "I wouldn't have done that. I could 'hit' him or 'ask' where Micky is."



	def assault(self):
		self.hitpoints -= 1

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