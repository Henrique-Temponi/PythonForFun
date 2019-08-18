"""
lets talk string formatting

it can be done in two ways
the first is using f before the string
and the other is using .format() after the string
both methods have their advantages
"""

# before, to include a number value to a string you would need to convert it to string first
# but with formatting, just include the variable inside a {} and you are good to go
# and you can put many variables as you like
x = 10
print(f"this is a formatted string with a variable = {x}")

# the same can be done with .format
print("this is a formatted string with a variable = {}".format(x))

# note that you need to place a {} where you want your value to be displayed
# but .formatting has a few special tricks -
# if you pass more them one variable you can use the order as a index
y = 20
print("this is a formatted string with a variable = {0} and {1}".format(x, y))

# you can pass values with keywords such as
print("this is a formatted string with a variable = {a} and {b}".format(a=x, b=y))

# just remember that once you used a keyword everything after that needs a keyword as well
print("this is a formatted string with a variable = {} and {a} and another value {b}".format(x, a=y, b=2))


# and that x could be anything and it would still work
x = True
print(f"this is a formatted string with a variable = {x}")
x = 10.10
print(f"this is a formatted string with a variable = {x}")

# there is a few things we can also do with this formatting
# we can round numbers by using: {value:.xf}
# x = the number of digits after the dot
print(f"{x:.1f}")  # in this case we only want 1
