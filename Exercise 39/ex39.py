# Learn Python The Hard Way - Exercise 39
# Copied by Joe Poser
# Fun with Dictionaries!

# creates line of '-'s
line = '-' * 10


# creates a mapping of state to abbreviation
states = {
	'Oregan': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# creates a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print line
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviations is: ", states ['Florida']

# do it by using the state then cities dict
print line
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print line
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print line
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print line
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print line
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
print state
if not state:
	print "Sorry, no Texas."
	
# get a city with a defalt value
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % city
