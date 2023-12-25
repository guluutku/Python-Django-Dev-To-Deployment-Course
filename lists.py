
# Create List
numbers = [1, 2, 3, 4, 5]
print(numbers)
print('---------------------')

# Using Constructor
# numbers = list((1, 2, 3, 4, 5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get Specific value
print(fruits[1])
print('---------------------')

# Get Length
print(len(fruits))
print('---------------------')

# Append to list
fruits.append('Mangos')
print(fruits)
print('---------------------')

# Remove from list
fruits.remove('Grapes')
print(fruits)
print('---------------------')

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)
print('---------------------')

# Remove from position
fruits.pop(3)
print(fruits)
print('---------------------')

# Reverse List
fruits.reverse()
print(fruits)
print('---------------------')

# Sort List
fruits.sort()
print(fruits)
print('---------------------')

# Reverse Sort
fruits.sort(reverse=True)
print(fruits)
print('---------------------')
