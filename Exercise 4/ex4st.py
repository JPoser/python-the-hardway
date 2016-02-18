# Learn Python The Hard Way, Exercise 4 Study Drill "Mistake". 
# Copied by JPoser.

# When I wrote this program the first time I had a mistake, and python told me about it like this:
# Traceback (most recent call last):
#      File "ex4.py", line 8, in <module>
#        average_passengers_per_car = car_pool_capacity / passenger
#    NameError: name 'car_pool_capacity' is not defined
# Explain this error in your own words. Make sure you use line numbers and explain why.

# Explanation by JPoser
# In this version line numbers will vary massively as there are lots of comments
# The original error relates to the order of the code, the error "NameError: name 'car_pool_capacity' is not defined"
# refers to the fact that the variable has not been assigned, in our version all the variables are calculated 
# in the correct order, so for line 25 both its variables have been defined in lines 20 and 23 when the program asks
# it to use those variables to calculate a new derivative of those variables. 

cars = 100
space_in_a_car = 4.0
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