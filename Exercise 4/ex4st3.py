# Learn Python The Hard Way, Exercise 4 Study Drill 3. 
# Copied by JPoser.

# Assigns variable "cars" to the integer (in future written as int) 100
cars = 100
# Assigns variable "space_in_a_car" to the floating number 4.0
space_in_a_car = 4.0
# Assigns the variable "drivers" to int 30
drivers = 30
# Assigns the variable "passengers" to the int 90
passengers = 90
# Assigns the variable "cars_not_driven" to the subtraction of the variables "cars" and "drivers"
cars_not_driven = cars - drivers
# Assigns the variable "cars_driven" to the variable "drivers"
cars_driven = drivers
# Assigns the variable "carpool_capacity" to multiplication of the variables "cars_driven" and "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car
# Assigns the variable "average_passengers_per_car" to the division of the variables "passengers" and "cars_driven"
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."