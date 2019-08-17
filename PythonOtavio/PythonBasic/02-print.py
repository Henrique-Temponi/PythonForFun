"""
So we will learn about the print function, we will just go over a few details
What we will learn:
    -a little more about print
    -separators
    -end line modifiers
"""

# print can be used in pretty much a lot of places, you can print a single string
print("Hello")

# or you can print more then one string in a single print
# NOTE: when you print multiple string with a single print the ',' will automatically add a space for you.
print("Hello", "World")

# it can be used with a single quote or a double quote, both works wonders
print("Hi", 'my name is smith')

# and a print can be used on it's own and it will add a blank line
print()

"""
say, what if you wanted to print a lot of names on a single print?
but you don't want them all cramp up together nor with spaces, we can use a few modifiers
to help us out, we will go over the sep (separator) modifier
in this case i want a few names with '|' between them
"""
print("smith", "mark", "Robertinho", "john", sep="|")

# With the sep, we can change the behaviour of ',' instead of it adding spaces, we can add what we want

# mess around with the sep modifier a little bit, se what else you can achieve

"""
Now let's talk about the end modifier
it's just like sep, but instead of in between the word, it changes at the end
"""
print("132", end="Kappa")
print()

# now when ever this print above ends it will add kappa to it. top notch

"""
test time!
try to make a single line print that prints five names speared with - and ending with .
the answer is down below, but don't look
"""


# print("mark", "smith", "sam", "negan", "robertinho", sep='-', end='.')
