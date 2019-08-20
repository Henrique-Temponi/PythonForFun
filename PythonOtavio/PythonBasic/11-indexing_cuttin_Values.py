"""
indexing and cutting strings in python

this one is quite usedful, sometimes we came across a few problems like
i need to takeout the last digit of the string, but i dont anything about it
well, python just so happens to have a tool in that

for example, a string have indexes, which start from 0 and goes all the way until the lenght - 1
**keep this in mind**

so lets try indexing this string = banana

012345
banana

so banana length is 6 but 5 positions
starting from 0

we can also use negative values to alter the string, lets use -1 and sse what happens
"""
x = "banana"

print(x[-1])  # using this, we get the letter a, which is the last letter in banana

"""
so knowing that we can tell that the indexing is something like this:

54321012345
ananabanana

so the first letter is always 0
and you can go either to the positive side or negative
"""

print(x[0], x[-1], x[-2], x[-3], x[-4], x[-5])  # this should print the whole word backwards

print(x[0:6:3])

# TODO: check if this is updated