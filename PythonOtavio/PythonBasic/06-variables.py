"""
Variables with python
well, this is quite an easy one, python has a dynamic typing
which means that, the actual variable type is defined as the program is on runtime
so we can just define a name for the variable, and the type will be chosen accordingly

about the name of the variable,
it can contain, letters, numbers, and _
it cannot start with a number

variables with python is case sensitive. meaning that a is different of A
"""

x = 10  # this will be used as a int at this point

print(x, type(x))

x = "text"  # the same variable can be used more the one time, and it can change type

print(x, type(x))

X = 10  # this is a different variable

# this is two different variables
print(x, type(x))
print(X, type(X))
