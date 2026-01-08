name = input('Enter your name: ')
location = input('Enter your location: ')
age = input('Enter your age: ')

print('Your name is:', name)
print('and it has\t', len(name), '\tcharacters')

print('Length of location:', len(location), '| Type:', type(location))
print('Length of age:', len(age), '| Type:', type(age))

person = name + " - " + location + " - " + age
print('Concatenated person info:', person)
