import time
import sys
show = dir(time)
print(show)

for path in sys.path:
    print(path)

print('\n')
# using sys.exit to close a program incase of an error
try:
    with open('file.txt') as file:
        for line in file:
            print(line)
except:

    print('Couldn\'t find file')
    sys.exit(1)