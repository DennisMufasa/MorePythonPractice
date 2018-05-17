names = ['dennis', 'mufasa', 'evi']
print(names[0])
print(names[1])
print(names[2])
# replaces list items at specified position
names[0] = 'Sue'
print(names[0])
# lists the lists in reverse
print(names[-1])
print(names[-2])
print(names[-3])

# adding list items
names.append('Viv')
print(names[-1])    # prints last list item

# adding multiple list items
names.extend(['Koi', 'Divina'])
print(names)

more_names = ['Ephra', 'Walt']
names.extend(more_names)
print(names)

# inserting list items at specified positions
names.insert(0, 'Sam')
names.insert(2, 'Weirdo')
print(names)

print(names[0:3])
# when slicing lists include one more number to the required slice size
first_three = names[0:3]
print('Some students: {}'.format(first_three))

last_two = names[-2:]
print('Last two students: {}'.format(last_two))

print(names[-1])

# String slices
partOfHorse = 'horse'[1:3]
print(partOfHorse)

Sue = names.index('Sue')
print(Sue)

# joining two arrays
animals = ['cow', 'goat', 'sheep']
more_animals = ['donkey', 'cat', 'dog']
farm = animals + more_animals
print(farm)
# sorting list items in alphabetical order
farm.sort()
print(farm)


names.sort()
print(names)




