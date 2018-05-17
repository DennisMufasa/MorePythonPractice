log = open('/etc/hosts')     # using the open fn to open a file hosts contained in folder etc in my computer
content = log.read()        # the read fn looks at the content of the file
print(content)      # output contents of the file

print('\n')
# opening another file
py = open('//home/mufasa/Documents/python.txt')     #windows o.s uses backward slashes
look = py.read()
print(look)

print('\n')
# changing current position to offset

file = open('/etc/hosts')
print('Current position: {}'.format(file.tell()))  # returns the current position before reading the file i.e 0
print(file.read())
print('Current position: {}'.format(file.tell()))  # returns the current position after reading the file i.e the final byte
file.seek(0)
print('Current position: {}'.format(file.tell()))  # returns the current position atfer offsetting no bytes i.e at beginning of the file

print(file.read(3))     # reads the first 3 bytes
print(file.tell())

# closing a file
file.close()
py.close()
print('\n')
# automatically closing a file once code is completed
print('Opened the file')
with open('/etc/hosts') as hosts:
    print('File Closed? {}'.format(hosts.closed))
    print(hosts.read())
print('File closed')
print('File Closed? {}'.format(hosts.closed))


with open('/etc/hosts') as the_file:
    for line in the_file:
        print(line)
