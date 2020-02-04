"""
switching values in python
"""

x = 10
y = 'string'

print(x, y)

x, y = y, x

print(x, y)

x = 20
y = 'banana'
z = True

print(x, y, z)

x, y, z = z, x, y

print(x, y, z)


