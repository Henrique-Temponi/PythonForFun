"""
about lists in python,

so a list is kinda like a string, but except here we can use plenty of data types
for a example, we can make a list with int, it would look like something like this

[0,1,2,3,4,5]

now, that is a list, and a list have a index, which is the position of a data,
just like a position in a string.

putting the index into the list we get:

 0 1 2 3 4 5
[0,1,2,3,4,5]
-6 5 4 3 2 1

this index is just like the string index, now how we define it:
"""

x = [0, 1, 2, 3, 4, 5]  # just like this, now x is a list of integers (int)

# we can add lists with other lists
z = [6, 7, 8, 9]

print(x)
print(z)

print("=======================")

print(x + z)


print("=======================")
# we can cut it as well
print(x)

y = x[:3]  # here we said that, we want y to have the first 3 values of x
print(y)   # Should print [0, 1, 2]

y = x[3:5]  # now starting from the third data from x, get everyone until the index 5
print(y)    # Should print [3, 4]

# note that the the last index it wont be added, if you want it to be added, increase the final value by one
# like so
y = x[3:6]
print(y)

# we can also use the steps as well
y = x[::2]
print(y)

print("=======================")
# we can also append the list
x.append(1)  # append would be something like, add after everything
print(x)

# just to clean up x we just reset it, to reset just do this
x = []

# extent is useful as well
x.extend(range(10))  # extend function, receives a iterable object and add it to the list
# and it can be configured with, start, ends, step
print(x)

# we can also insert at a specific index
x.insert(2, "X")  # will add a X at the second index
print(x)

# also, we have a list with whatever type we want in a single list

# TODO: pop, push, del, max, min, print by index, create by iterable, hangman
