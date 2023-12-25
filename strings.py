
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
print("-----------------")

# String Methods
s = "heLlo thEre woRld"

# Capitalize First Letter
print(s.capitalize())
print("-----------------")

# Capitalize Every Letter
print(s.upper())
print("-----------------")

# Lower Case Every Letter
print(s.lower())
print("-----------------")

# Swap Case
print(s.swapcase())
print("-----------------")

# Get Length
print(len(s))
print("-----------------")

# Replace 
print(s.replace('woRld', 'everyone'))
print("-----------------")

# Count 
sub = "h"
print(s.count(sub))
print("-----------------")

# Starts With
print(s.startswith('h'))
print("-----------------")

# Ends With
print(s.endswith('ld'))
print("-----------------")

# Split into a List
print(s.split())
print("-----------------")

# Find Position
print(s.find('R'))
print("-----------------")

# Is all alphanumeric
print(s.isalnum())
print("-----------------")

# Is all alphabetic
print(s.isalpha())
print("-----------------")

# Is all numeric
print(s.isnumeric())
print("-----------------")
