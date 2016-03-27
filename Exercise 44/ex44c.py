# Learn Python The Hard Way - Exercise 44c
# Copied by Joe Poser
# SUPER and overriding

class Parent(object):
	
	def altered(self):
		print "Parent altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()