
# what it would look like without specification
print('{0} | {1}'.format('Fruit', 'Quantity'))
print('{0} | {1}'.format('Apple', 3))
print('{0} | {1}'.format('Oranges', 10))

print('\n')

# format specification
# the number following the colon makes value to format at least 8 characters in length
print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apple', 3))
print('{0:8} | {1:8}'.format('Oranges', 10))

print('\n')

# left aligning strings
print('{0:8} | {1:<8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:<8}'.format('Apple', 3))
print('{0:8} | {1:<8}'.format('Oranges', 10))

print('\n')

# center aligning strings
print('{0:8} | {1:^8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:^8}'.format('Apple', 3))
print('{0:8} | {1:^8}'.format('Oranges', 10))

print('\n')

# specifying dataTypes
# lets take a few bites from our apple
# the .3f specifies that the float value should be to 3 decimal places and the same applys for .2f
print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8.3f}'.format('Apple', 2.36987))
print('{0:8} | {1:8.2f}'.format('Oranges', 10))
