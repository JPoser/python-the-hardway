# Learn Python The Hard Way, Exercise 4 Study Drill 2. 
# Copied by JPoser.

# From book: "I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?"
# Answer: No, floating point numbers are useful when dividing as that is where fractions are created
# on running the program the values read similar save for on line 21 where the printed value is no longer a 
# floating point number

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."