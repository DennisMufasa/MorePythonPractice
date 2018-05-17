contacts = {'Jason': '555-4563',
            'Dre': '555-2365',
            'Evi': '555-9658'
            }

# referencing toa specific dictionary item
jason = contacts['Jason']
print('Dial {} to call Jason.'.format(jason))

# adding items in the dictionary through assignment
contacts['Tony'] = '555-8963'
print(contacts)
print(len(contacts))     # reports number of items in the dictionary

# deleting items
del contacts['Evi']
print(contacts)

# dictionary item with more than one value
students = {'name':['Dennis', 'Mufasa'], 'admNo':1452, }

for name in students['name']:
    print('Students name: {}'.format(name))

# looping through items

for contact in contacts:
    print('The number for {0} is {1}'.format(contact,contacts[contact]))


