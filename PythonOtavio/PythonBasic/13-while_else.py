"""
now, we will talk more about the while else code of block
the while block we have seen it before, now let's combo that with a else

"""
x = 0

while x < 10:
    print(f"Current value is: {x}")
    x = x + 1 
else:
    print("finished with no erros")

"""
So here we have the basic syntax, first , we define the while loop, then
after all while block we add a else, 
but this else block will only show up if the while compleated with no breaks.

let check some a way to do that 
"""

x = 0

while x < 10:
    
    if x == 5:
        break

    x += 1
else:
    print("This shouldn't print")

"""
now, accumulators:
accumulators are like a total sum of given number
let's try to accumulate 10
"""

x = 0
acuu = 0

while x < 10:
    
    acuu = acuu + x  #  this will get the total sum of 10
    
    x += 1
else:
    print(f"The total sum was : {acuu}")