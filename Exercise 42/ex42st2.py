## Animal is-a object (yes, sort of confusing look at the extra credit)
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name of some kind
		self.name = name
	def bark(self):
		print "Woof"

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name of some kind
		self.name = name

	def meow(self):
		print "Meow"

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name of some kind
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
		## Employee inherits methods from Person?
		super(Employee, self).__init__(name)
		## Employee has-a salary of some kind
		self.salary = salary

	def slack_off(self):
		cost_to_employer = self.salary / 365 / 7
		print "This is costing the company $%d an hour" % cost_to_employer

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

rover.bark()

## satan is-a Cat
satan = Cat("Satan")

satan.meow()

## mary is-a Person
mary = Person("Mary")

## mary has-a pet Cat satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

frank.slack_off()

## frank has-a pet Dog rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()