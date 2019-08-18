"""
today we will learn a little more about string
"""

"""
so in a nutshell String is everything between '' or "", treat it as a text,
so keep in mind that while working with string that it should be text to text
e.g: "hello" + 1
that we are saying there is do the operation + with a string and a number,
and it won't work because string works with text + text
a solution would be 
"hello" + "1"
this is ok
"""
print("text")  # this is a string

# what about the quotes?, we can use both ' and ", but if you start with ' but you will need to close it with '
# same goes for "
print('Hello')
print("World")

# if you want to use the quote inside a string, it gets tricky, in python if you start wih " or '
# you can still use the opposite quote
print("this is a 'test'")

# see? i used a double quote inside a single quote, you can do the reverse as well
print('this is a "test"')

# if you really wanted to use a single quote for everyone you could you a escape method
# to use the escape method just add a \ before the quotes and you are good to go!
print("this is another \"test\"")

# FYI:print support "flags" that will change the way it prints things, if you use the r before
# the string it will print the raw string
print(r"this is another another \"test\"")

# with the r "flag" it should print the string like we are seeing it
