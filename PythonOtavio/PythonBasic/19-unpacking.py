"""
unpacking in python
"""

x = ['axell', 'Robert', 'cassandra']

x1, x2, x3 = x

print(x1, x2, x3,sep="\n")


"""
x = ['axell', 'Robert', 'cassandra']

x1, x2 = x

ERRO
"""

y = ['yeet', 'max', 'smith',1, 3, 4, 6, 7, 8, 123]

x1, x2, *_ = y

print(x1, x2)

*_, x1, x2 = y

print(x1, x2)

x1, *_, x2 = y

print(x1, x2)
