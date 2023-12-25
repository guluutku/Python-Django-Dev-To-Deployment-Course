# A Dictionary is a collection which is unordered, unchangeable and indexed. No duplicate members

# Simple Dic
person = {
    'first_name': 'Gün',
    'last_name': 'Uluutku',
    'age': 30
}

print(person)
print('---------------------')

# Using Constructor
# person = dict(first_name='Gün', last_name='Uluutku', age=30)

# Access Value
print(person['age'])
print(person.get('last_name'))
print('---------------------')

# Add key value
person['phone'] = '55-5555-555'
print(person)
print('---------------------')

# Get Keys
print(person.keys())
print('---------------------')

# Get Values
print(person.items())
print('---------------------')

# Make Copy
person2 = person.copy()
print(person2)
person2['city'] = 'boston'
print(person2)
print('---------------------')

# Remove Item
# del(person['age'])
print(person['age'])
print('---------------------')

# Clear Dic
person.clear()
print(person)
print('---------------------')

# Get length
print(len(person))
print('---------------------')

# List of dict
people = [
    {'name': 'Martha', 'age':40},
    {'name': 'Bob', 'age':20}
] 
print(people)
print(people[1]['name'])
print('---------------------')

