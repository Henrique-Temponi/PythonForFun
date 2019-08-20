"""
while loops in python

these are the bread and butter of any programming languange, you'll find these
repetision loop anywhere in any langangue, 

let's start by looking at the syntax, 

we will use the same idea of the if,
a while needs a conditional, and it will be executed as long as the conditiol is true

so lets see that 
"""

x = 0  # first we define the variable

while x < 10:  # we say the conditional, in this case the loop keeps going WHILE x is less then 10
    print("YEET")  # while that is going, it's going to do the curret block of codex
    x = x + 1  # now, after we done with out code, we have to increment on x to achive the coditon and stop
               # otherwise this WILL become a infinit loop so look out

# remenber the indentention, 

"""
you can put anything inside the while, another while, an if block, input function anything
just remember the intend and syntax, and you can do it

below are a few codes using while
"""

# a database register
x = 0

while x = 10:

    print()

    name = input("Enter a name: ")
    birth = int(intput("Enter you birth date: "))

    if birth != 0:

        birth = 2019 - birth

    print(f"user has been registred as: name: {name}, age: {birth}")

    x += 1  # you can also increment the x by doing this


x = 0

while x < 10:

    if x % 2 !== 0:
        print(f"odd number: {x}")
    else:
        print(f"Even number: {x}")

    x += 1  # remember the indentation, not to be inside another block, 