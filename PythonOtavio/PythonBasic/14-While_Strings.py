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

x = "bananaa"
tam = len(x)  # this will get the total length of given string,
count = 0
c = 0

while c < tam:

    if x[c] != '':  # the useage of [] in this case is to get index of a string, 
                    # remembering that a string have a index, so we can access that by using a []
        count += 1

    c += 1

print(f"The string have {count} letters")


"""
let's try something different, 
now we want to check what is most used letter
in a given string
"""
c = 0
letter_most_used = ""
number_times = 0

while c < tam:
    
    current_letter = x[c]

    current_number = x.count(x[c])

    if current_number > number_times:

        letter_most_used = x[c]
        number_times = current_number

    # print(x[c])
    c += 1
    

print(f"The letter most used was: '{letter_most_used}' it appeared {number_times} times")
