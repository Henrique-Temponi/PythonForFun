"""
we have seen a while loop, now let's move on to for loops
they are quite the same but just a few diferences
for loop requires a interable object, meaning, what we could have a for in a string
list, arrays, anything that has a index or an idea of one you can loop it
"""

print()
# in using while we will use the function range, which returns a interable object so we can loop through it

for x in range(10):
    print(x)  # this is print 0 to 10

print()
for i in range(20, 10, -1):  # range kinda works like the string cutting, we can define where it begin and ends
    print(i)


"""
the range function can also have a few different param, 
the first is used to say where it starts, 
the second is used to say there it ends,
and the thrid  is used to say how it should step

if only a single param is passed, then it will use the default patterns,
the param given will act as where should the loop endn stepping 1 by 1

we also have the enumerete function, which creates a index, for the loop
"""
print()

x = "banana"
for i, p in enumerate(x):
    print(f"{i} = {x[i]}")
    # print(type(i))
    # print(type(p))
# we can also use it in the string itself

for c in x:
    print(f"the current letter is: {c}")  # this will get the current char of the string 

"""
so keep in mind that the type of the second part of the for defines 
what type the previous variable will have
"""