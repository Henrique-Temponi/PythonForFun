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

"""
you can use teh cutting function like this
first the string you want to cut,
the open the brackes
at this point it should look something like this
x[],
now 
so we can add a few operators
x[y,z,p]
where y = the start of the cutting
      z = the end of the cutting
      p = the steps

the steps mean that how it's going to walk in the string
"""
print(x[0:6:3])  # take this exemple for instance, it will start at 0, going all the say to 6, stepping 3 by 3

# we can use one, two, or all three flags to say what we want,
# just leave it empty, it should look something like this

print(x[::2])  # here we are saying that we want the default start and end, but stepping two by two 

# TODO: check if this is updated