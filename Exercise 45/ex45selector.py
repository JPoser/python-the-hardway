# Learn Python The Hard Way - Exercise 45
# Written by Joe Poser
# State Machine for State Setting
import ex45scenes

class SectionMap(object):
	sections = {
		"office" : ex45scenes.Office(),
		"house" : ex45scenes.House(),
		"tail" : ex45scenes.Tail(),
		"crony" : ex45scenes.Crony(),
		"interrogation" : ex45scenes.Interrogation(),
		"murderer" : ex45scenes.Murderer(),
		"case closed" : ex45scenes.CaseClosed(),
		"case cold" : ex45scenes.CaseCold(),
		"dead" : ex45scenes.Dead(),
	}

	def __init__ (self):
		self.first_stage("office")

	def next_stage(self, section_name):
		return self.sections.get(section_name)

	def first_stage(self, stage_name):
		return self.sections.get(stage_name)


class SceneSelector(object):
	
	def __init__ (self, section_map):
		self.map = section_map

	def run(self):
		
		begin = self.map.first_stage("office")
		next_one = self.map.next_stage(begin.start())
		end_states = []
		while True:
			and_again = self.map.next_stage(next_one.start())
		


new = SectionMap()
SELECTOR = SceneSelector(SectionMap())
SELECTOR.run()