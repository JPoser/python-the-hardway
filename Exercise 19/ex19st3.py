# Learn Python The Hard Way. Exercise 19. Study Drill 3.
# Copied by JPoser

def scampy_claw(adorable, painful):
	print "The sum of cuteness %d and 10 is %d" % (adorable, adorable + 10)
	print "This is tempered with %d pain" % (painful)
	print "Such is the way of things"
	print "Awwwwwwwwwww... OUCH!\n"

print "Claws and floats:"
scampy_claw(10.5, 11.756)

print "Claws and fixed variables:"
cuteness_level = 9001
claw_length = 16

scampy_claw(cuteness_level, claw_length)

print "And this is gonna be some fancy shizzle, type numbers at the prompt innit:"
cuteness_amount = raw_input("> ")
claw_sharpness = raw_input("> ")

# There may be a way of doing this easier but these two
# convert their strings to integers
cute_int = int(cuteness_amount)
claw_int = int(claw_sharpness)

scampy_claw(cute_int, claw_int)

print "see my maths"

scampy_claw(10 * 5, 6 % 1)

print "I am bored"
scampy_claw(1, 1)
