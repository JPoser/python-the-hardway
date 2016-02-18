# Learn Python The Hard Way. Exercise 10. Study Drill 4.
# Copied by JPoser

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a \a line with %s sausages." % 6
backslash_cat = "I'm \\ a \\ cat."
formatter_cat = "I'm a \\ %r \\ \'escape\' look at all my crazy \"count'em\" %s escapes." % ("crazy", 10)

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print formatter_cat