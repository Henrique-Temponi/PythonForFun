"""
or operator in python
"""
nome = input('type something')

if nome:
    print(nome)
else:
    print('please type something!!')

"""
or
"""

print(nome or 'please type something!')

print(nome or None or False or 0 or 'please type something' or 'otherthing')

