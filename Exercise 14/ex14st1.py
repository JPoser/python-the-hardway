# Learn Python The Hard Way. Exercise 14.
# Copied by JPoser

from sys import argv

script, user_name = argv
prompt = 'Action: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Sounds awesome, how much RAM does it have?"
ram = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
Wow %r is alot of RAM!.
""" % (likes, lives, computer, ram)