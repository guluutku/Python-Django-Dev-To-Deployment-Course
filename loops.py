
# for loop
people = ['John', 'Will', 'Janet', 'Karen']

for person in people:
    print('Curren person: ', person)
print('-------------------------------------')

# break out
for person in people:
    print('Curren person: ', person)
    if person == 'Janet':
        break
print('-------------------------------------')

# Continue
for person in people:
    if person == 'Janet':
            continue
    print('Curren person: ', person)
print('-------------------------------------')

# Range
for i in range(len(people)):
     print('Current person: ', people[i])
print('-------------------------------------')

for i in range(1, 10):
     print('Current number: ', i)
print('-------------------------------------')   
print()
print()
print()

# While loop
count = 0
while count <= 10:
     print('COunt: ', count)
     count += 1
