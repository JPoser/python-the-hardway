# Learn Python The Hardway - Exercise 37 Study Drill 1
# Written by JPoser

from sys import argv as fargv
import time

fun = fargv

class super_fun():

    if fun is fun:
        print "Woo-hoo! (is)"
    elif fun is not fun:
        print "boo"
    else:
        print "what?"

super_fun()

integer = 10

def number_fun():
    
    if integer < 5 and fun is fun:
        print "And I <3 < 5 %d" % (integer)
    elif integer == integer:
        print "I <3 %s" % ("Say what!")
    elif not (integer != integer):
        print "Blow me"
    else:
        print "I don't <3 %r" % (integer) 

    spanner = integer * 5
    print spanner
    return integer

number_fun()

listz = [1, 2, 3, 4, 5, 6, 7]

for thing in listz:
    print thing

if 4 or 3 in listz:
    print "or!"
else:
    print "or not!"

life = 40

while life != 42:
    print "That's not life %i" % (life)
    life = life + 1

print "Thats life! %u" % (life)

del(listz)

def none():
    pass

print none()

print "life"
while life > 29:
    life = life - 1
    print life
    time.sleep(.09)
        
    if life == 30:
        break

def globe_al():
    print "Thing is", thing
    global thing
    thing = 42

globe_al()
print "Thing is", thing

thing = 40

assert thing != 39 

print "Thing"

for num in range (2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        time.sleep(.05)
        continue
    print "Found a number", num
    time.sleep(.05)

# code bellow creates a number generator view - http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained for more info
def gen():
    mylist = range (3, 7)
    for i in mylist:
        yield i*i

mygen = gen()

print mygen

for i in mygen:
    print i

my_file = open('newfile.txt', 'w+')

with my_file:
    try:
        my_file.write("print 'hello world!'")
    except:
       y = lambda x: x**2 + 2*x - 5
       print y
    finally:
        my_file.read()

my_file.close()

exec_file = open('newfile.txt')

exec exec_file

if 9 != num:
    raise my_error, "OMG ERROR"

