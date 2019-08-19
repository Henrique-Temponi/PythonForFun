"""
about values modifiers, there is a syntax to help you with that

using the format function or f'', inside the {} use the following commands to change the value

:s - for text (string)
:d - for numbers (int)
:f - for float (float)
:.(x)f - number of digits after the dot, where x is the number of digits
:(char)(< or > or ^)(quantity)(type - s, d, f)

> - left
< - right
^ - center

with this you can edit a lot of values that you want
"""
x = 10
print(f"{x:#>10}")  # will add 10 # at right of the number
print(f"{x:#<10}")  # will add 10 # at left of the number
print(f"{x:&^10}")  # will add 10 & at center of the number

y = 2.76
print(f"{y:.1f}")  # formats the float value to have a single digit after the dot (it rounds the number)
