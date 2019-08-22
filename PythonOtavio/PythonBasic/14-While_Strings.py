"""
now we will talk about string with while,

a string is considered a interable object, meaning that you could run a repedicion through it,
so we could have a string like banana, and count how many a appear in that string,
what is the most used letter and so on,
we thing we cannot do in python is chance the said string, in python every string is a
immutable object, meaning that one declared we cannot change it.

let see some examples
first let's try to count the total number of letters
"""

x = "banana"
tam = len(x)  # this will get the total length of given string,
count = 0
c = 0

while c < tam:

    if x[c] != '':
        count += 1

    c += 1

print(f"The string have {count} letters")
