"""
    Split       - this will split a string with the chosen separator, ( default is whitespace )
    Join        - this will join multiple elements (eg. in a list or a string)
    enumerate   - this will create a index for a iterable object (eg. list, string, dictionary, etc)

    these function covers a lot of ground when it comes to manipulate an object,
    simple and effective these will help you out along the way
"""

# the first we'll cover is the split function, using a string, we will split the whitespaces
x = "Built purse maids cease her ham new seven among"

list1 = x.split()

# so what we've done is, when python founds a whitespace it will cut and return what was before the cut as a new object
# you can see that was printed was a list with the cut elements

print(list1)

# now that we have separated the string, we can join it back, with join, how to use it it's quite simple as well
# first the define what the separator will be
separator = " "  # in this case we'll use the whitespace

# after that, we say that we want to use that separator to join our list

y = separator.join(list1)  # and finally we give the iterable object to join

# so in plain english this would mean, i want to use the separator( whitespace ) to join a iterable list

# now, the enumerate function, this can be used to enumerate a list or a string
# let's say that you have a list and you want to get the index of each name, you could add another variable
# or you could use enumerate

z = ['Banana', "Mango", "Apple"]

# let's put an index in each of them

for index, food in enumerate(z):
    print(index, food)

# this will give us a index right of the bat, while saving a few extras variables, quite handy
# you may notice that we used 2 variables in the for, we'll get to that later, but for now, just know that
# you can have two variables in for, this can give a flexible for.
