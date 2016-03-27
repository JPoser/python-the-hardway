# Learn Python The Hard Way - Exercise 44d
# Copied by Joe Poser
# All the inheritance

# Creates a class Parent() inheriting from base class object()
class Parent(object):

	# Creates a method override that takes one arguement self
	def override(self):
		# Prints "PARENT override()" to stdout
		print "PARENT override()"

	# Creates a method implicit that takes one arguement self
	def implicit(self):
		# Prints "PARENT implicit()" to stdout
		print "PARENT implicit()"

	# Creates class altered that takes one arguement self
	def altered(self):
		# Prints "PARENT altered()" to stdout
		print "PARENT altered()"

# Creates a class Child that inherits from Parent()
class Child(Parent):

	# Creates a method override, overrides the one from class Parent()
	def override(self):
		# Prints "CHILD override" to stdout
		print "CHILD override()"

	# Creates method altered, overrides altered from Parent()
	def altered(self):
		# Prints "CHILD, BEFORE PARENT altered()" to stdout
		print "CHILD, BEFORE PARENT altered()"
		# Calls method altered() from parent class Parent()
		super(Child, self).altered()
		# Prints "CHILD, AFTER PARENT altered()" to stdout
		print "CHILD, AFTER PARENT altered()"

# Create an instance of class Parent() called dad
dad = Parent()
# Create an instance of class Child() called son
son = Child()

# Call method implicit() from class Parent()
dad.implicit()
# Call inherited method implicit() from class Parent()
son.implicit()

# Call method override() from class Parent()
dad.override()
# Call overrided method override() from class Child()
son.override()

# Call method altered() from class Parent()
dad.altered()
# Call overriding method altered() from class Child(), but method also
# calls parents version of altered() by means of a super() function
son.altered()