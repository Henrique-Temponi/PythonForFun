"""
if else elif in python
for this topic we will divide em 3 parts
first - syntax
second - math operators
third -  programming operators
"""

# first things first, lets look at the syntax
"""
syntax in python is quite easy to understand, so,

an if is defined like this:

if x:
    print("ok")
    
first, you say if to start a conditional block (the intend is to say that everything in that intend belongs to a block
of code)

where x = is the logical value,
remembering that 1 = true and 0 false.
a if only will be executed with the condition is true, keep that in mind

after you have placed the conditional, you need to put a : to say to python
that you are going to create a block of code

lets see that
"""

conditional = True  # first define the conditional
# (this can be any name that you want just remember to have a logical value)

if conditional:  # so if the conditional is true, the block of code below will be executed.
    print("the conditional is true")  # this code will be executed because our conditional is true

"""
good now, lets good at the else syntax

the else, will be used with an if code block,
when the condition is false, the if won't be executed, and this is when is else comes to play,
because the if code block wont be executed, so it will execute the else block instead
"""

conditional = False  # our conditional is now false

if conditional:
    print("the condition is true")
else:
    print("the condition is false")

"""
note that the else is not a part of the if block code, because its not intended 

now, the elif

the elif is used between if and else, it's supposed to be a middle term,
so if there is more conditions that you want to test, before ending with a else block,
you could use a elif 
"""

conditional = False
conditionalb = True

if conditional:
    print("conditional is true")
elif conditionalb:
    print("conditional is false but conditionalb is true")
else:
    print("both conditional are false")

"""
now, if python finds a true conditional, it will stop testing the rest of conditionals
and exit the code
"""

# all right so, we cleared the syntax, let move on to mathematical operations
# we can use the following operators: ==, >, <, >=, <= , !=

"""
we use them like like in math
    ==  - equals (10 == 10) = True
    >   - greater then (10 > 9) = True
    >=  - greater or equal then (10 >= 10) = True
    <   - less then - (9 < 10) = True
    <=  - less or equal then (10 <= 10) = True
    !=  - different then (9 != 10) = True
"""

conditional = 10 == 10  # change the value here, and see what happens with the code below

if conditional:
    print("This conditional is True")
else:
    print("This conditional is False")

"""
alright, now for the logical operators
we have the following:
    and - only true if both conditions are true
    or  - only true if one of the conditions are true
    not - negates a condition
    in  - true if there is the condition "in" a selected element
    
these are kinda different but really powerful
let's try them out below
"""

conditionala = True
conditionalb = not True

if conditionalb and conditionala:
    print("Both conditions are True")
elif conditionala or conditionalb:
    print("One of the conditions are true")
else:
    print("Neither of the conditions are true ")

# the in operator is a little different
text = "banana"

if "a" in text:  # one of the uses could look something like this
    print("There is a in banana")
