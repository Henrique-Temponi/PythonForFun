"""
functions in python
"""


def func(var):
    print(var)


func('test')
var = func('test')
print(var)


if var:
    print(var)
else:
    print('nome')


def func1(var):
    return(var)


func('test')
var = func1('test')
print(var)


if var:
    print(var)
else:
    print('nome')


def div(x, y):
    return x / y


var = div(8, 2)

if var:
    print(var)
else:
    print('oh no, empty')


def div1(x, y):
    if y == 0:
        return

    return x / y


var = div1(8, 0)

if var:
    print(var)
else:
    print('oh no, empty')


def f(var):
    print(var)


def test():
    return f


var = test()('test')
var = test()
print(type(var))

var('now i can print')


def test2():
    return 'Oku', 'Smith'


var = test2()
print(var[0], type(var))
print(var[1], type(var))



