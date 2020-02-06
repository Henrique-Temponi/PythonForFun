"""
functions in python
"""

# def func1(x, y, z, name=None, a):
#     print(x, y, z)


def func2(x, y, z, name=None, a='test'):
    print(x, y, z)


def func3(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


func3(1, 2, 3, 4, 5)


def func4(*args):
    args = list(args)
    args[0] = 20
    print(args)


func4(1, 2, 3, 4, 5)


def func5(*args, **kwargs):
    print(args)
    print(kwargs)

    print(kwargs['name'], kwargs['sur_name'])
    # print(kargs['age']) this will fail since there is no keyword 'age'
    # Risky


lis = [1, 2, 3, 4, 5]
func5(*lis, name="Smith", sur_name="Oku")
func5(lis, name="Smith", sur_name="Oku")  # Note the lis will be considered only one item


def func6(*args, **kwargs):
    print(args)

    # Safer
    name = kwargs.get('name')
    sur_name = kwargs.get('sur_name')
    age = kwargs.get('age')  # In this case this will only return a Nome

    if name and sur_name:
        print(f'Hello {name}')
    else:
        print('Not found')

    if name and sur_name and age:
        print(f'Hello {name}')
    else:
        print('Not found')


lis = [1, 2, 3, 4, 5]
func6(*lis, name='Smith', sur_name='Oku')
