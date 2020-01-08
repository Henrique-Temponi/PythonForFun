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
Lists in python can hold any type of value:
x =[1, 2, 3, True, False, 'f', 0.0]
so this list have a int, boolean, string and real values, anything goes in lists!
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

# you can add different lists with each other
z = x + y
print(z)

# just to clean up x we just reset it, to reset just do this
x = []
print(x)


print("=======================")
# we can also append the list
x.append(1)  # append would be something like, add after everything
x.append(True)
x.append("test")
print(x)

x = []

# extent is useful as well
x.extend(range(5))  # extend function, receives a iterable object and add it to the list
# and it can be configured with, start, ends, step
print(x)

# we can also insert at a specific index
x.insert(2, "X")  # will add a X at the second index
print(x)

# the index can be any valid index
x.insert(0, "python")
x.insert(3, True)
# x.insert(10, "erro") # this will cause an error

# we can also delete elements from the list using del
# del function works like string cutting ( we can chose a start, end and the stepping value )

x = []
x.extend(range(10))  # create a list with 10 elements
print(x)
del(x[::2])  # delete from start to end, and stepping 2
del(x[0:1])  # delete from start and stop ate index 1, meaning only the first element will get deleted
del(x[0])  # or you could just give the index value

# remember you can use the string cutting techniques

# let's suppose that you want to delete the last element in the list,
# we could do a del(x[-1]), but there is a build-in function for that
# which is the pop function,
x = [1, 2, 3, 4, 5, 6]
x.pop()
print(x)

# so now the last element will be deleted

# Max and Min functions, they are self explained by their names, but let's go over it
# max will return the  highest value
# min will return the lowest value
print(max(x))
print(min(x))

# but what if the values are not numeric, what if they are, strings? then the max will return in alphabetical order
print(max("Mike", "John", "Vicky"))
print(min("Mike", "John", "Vicky"))


# TODO: hangman
