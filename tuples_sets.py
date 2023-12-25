# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
print(fruit_tuple)
print('---------------------')

# Using Constructor
#fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
print(fruit_tuple[1])
print('---------------------')

# Cannot change value
# fruit_tuple[1] = 'Grape' Gives Type Error

# Tuples with one value should have trailing coma
fruit_tuple_2 = ('Apple')
fruit_tuple_3 = ('Apple',)
print(fruit_tuple_2)
print(fruit_tuple_3)
print('---------------------')

# Get length
print(len(fruit_tuple))
print('---------------------')
print('')
print('')

print('-------SETS--------')

print('')

# A Set is a collection which is unordered and unindexed. No duplicate members

# Create Set
fruit_set = {'Apple', 'Orange', 'Mango'}
print(fruit_set)
print('---------------------')

# Check if in Set
print('Apple' in fruit_set)
print('Apples' in fruit_set)
print('---------------------')

# Add to set
fruit_set.add('Grape')
print(fruit_set)
print('---------------------')

# Remove from set
fruit_set.remove('Grape')
print(fruit_set)
print('---------------------')

# Clear the set
fruit_set.clear()
print(fruit_set)
print('---------------------')

# Delete Set
del fruit_set
print(fruit_set)
print('---------------------')
