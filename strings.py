
name = 'Gün'
age1 = 26
age2 = 26

# Concatenate
print('Hello I am ' + name + ' age ' + str(age1))

print("-----------------")

# Arguments by positions
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

print("-----------------")

# Arguments by name
print('My name is {name} and I am {age2} years old.'.format(name=name, age2=age2))

print("-----------------")

# F-Strings (only 3.6+)
print(f'My name is {name} and I am {age2} years old.')
