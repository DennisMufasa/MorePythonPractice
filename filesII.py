# creating a file using pyhton and writing some data.
with open('file.txt', 'w') as file:   # the 'w' allows us to write in the file
    file.write('This text will appear in the file having being typed on pycharm.\n')
    file.write('Here\'s mmore text.')

with open('file.txt') as file:
    print(file.read())

try:
    contacts = open('file.txt').read()
except:
    contacts = ''


print(len(contacts))
