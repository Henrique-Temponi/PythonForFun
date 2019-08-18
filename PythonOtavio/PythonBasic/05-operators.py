"""
we have a few operators in python:
+, -, *, **, /, //, %, ()
"""

# Both + - are quite simple, the first adds, the second subtracts
print(1 + 1)
print(1 - 1)

# note with +, you add strings together
print("bana" + "na")

# * = multiples
print(2*2)

# NOTE: you can multiply strings, with you copy x number of times a string
print("bana" * 20)

# ** = power to
print(2**10)  # 1025 (2^10)

# / = division with rest
print(5 / 2)  # will return a real value, since 5 is even

# // = division without rest
print(5 // 2)  # returns a int value, only getting the numbers after the dot

# % = rest return
print(5 % 2)  # return the rest of the division

# () = tells to the computer which operation to do first
print(10 * (2 + 1))  # returns 30, without the parentheses it returns 21
