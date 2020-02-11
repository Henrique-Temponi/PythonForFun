"""
functions in python - part 4
"""

var = "value"


def func():
    print(var)


def func2(arg=None):
    # global var
    # var = "another value"
    # print(var)
    arg = arg.replace("v", "c")
    return arg


func()
func2()

var2 = func2("value")


def func3():
    # print(var)
    # var = "vae"
    # print(var)
    return 0


print(var)


