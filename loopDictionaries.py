# Looping through items in a dictionary. This loop doesnt guarantee the order the items will be processed
contacts = {'Vicky': '555-9632',
            'Koi': '555-8523',
            'Viv': '555-7412'
            }
'''Loop begins'''
for contact in contacts:
    print('The number for {0} is {1}'.format(contact,contacts[contact]))
print('\n')
students = {
    'Julie': 140,
    'Sue': 210,
    'Leah': 350
}
print('Student Marks')
for student in students:
    print('{0}: {1}'.format(student,str(students[student])))

# looping with two variables.
# The first variable is the key and second variable is the value
for person, number in contacts.items():
    print('Call {0} on {1}.'.format(person,number))

print('\n')

# Students loop
for mwanafunzi, marks in students.items():
    print('{} scored {}.'.format(mwanafunzi,marks))

