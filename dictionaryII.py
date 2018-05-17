contacts = {
    'Jason': ['555-89654', '555-65412'],
    'Carl': '555-74521',
    'Mufasa': '555-45872'
}

for contact in contacts:
    print('To call {0} dial {1}.'.format(contact, contacts[contact]))

# checking whether a value exists in a dictionary
if 'Mufasa' in contacts.keys():
    number = contacts['Mufasa']
    print('Mufasa\'s phone Number: {}'.format(number))

# Checking for key that contains a list
if 'Jason' in contacts.keys():
    '''Printing Jasons second phone number'''
    Jnumber = contacts['Jason'][1]
    print('Jason phone number: {}'.format(Jnumber))

# Checking for a key that isnt in the dictionary
# this code is not executed because 'Tony' is not a key

try:
    if 'Tony' in contacts.keys():
        print('Tony phone number :' + contacts['Tony'])
except:
    print('That key is not in the dictionary')


# Returns whether a value exists in a list
print('555-45872' in contacts.values())

    


