"""
there are a few type of primitive data in python, which are the following
    int - used for numbers - 1, 2, 3, 4, 5
    String - used for texts - "heelo" 'sup'
    float - used for real numbers - 1.0 , 20.34
    bool - logic value - True or false
"""

# so type of data, python uses those types, lets test a few of them
# there is a modifier called type in print, which prints out the type of given value

print(1, type(1))  # should print int, because 1 is a number
print("text", type("text"))  # should print str (short for string), because the value is inside a double or single quote
print(True, type(True))  # should print bool, because it's a bool value (a logical one)
print(1.30, type(1.30))  # should print float, because it's a real value, NOTE:the decimal part is separated with a dot

"""
talking about the logical values
there is a quick list of logical values
when a string is empty ("" or '') it has the logical value of False
when a int is 0 it has the the logical value of False

with that in mind let talk about casting or type casting, 
you can cast a type to another type
int(float) -> it becomes a int value!
to cast a cast a value just put the value you want in front of the value, and it should cast it to the desired
type

|- we want to convert the value inside the parenthesis to a bool value
bool("text")
       |- the value that is about to be converted
       
as we said before, a empty str (String) should give us a logical value of 0
but in this case we have something inside the string, so the logical value should be 1

you can convert almost anything!
you can convert:
    int
    float
    bool
    str
    
try it out below, convert a few types into others one, try to follow the examples below,
please if you have any question be sure to google it!

"""

print(type(1), type(bool(1)))  # should print int for the first and then bool for the other one
print(type(1.0), type(int(1.0)))  # should print real for the first and then int for the other one

