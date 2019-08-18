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
