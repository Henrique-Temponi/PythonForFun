"""
ternary operator in python
"""

statement = True

# if statement:
#     thing = "yes!"
# else:
#     thing = "no :("

thing = 'Yes!' if statement else 'no :('

print(thing)

age = 21

# if age >= 21:
#     thing = 'OK'
# else:
#     thing = 'NOT OK'

check_age = (age >= 21)
thing = "OK" if check_age else 'NOT OK'

print(thing)

year = input()

if not year.isnumeric():
    print('only numbers please')
else:
    year = int(year)
    check_year = (year <= 2000)
    thing = "Y2K!!" if check_year else "loading..."

print(thing)
