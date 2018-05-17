# the value in the format() method is placed where there are curly braces

print('I {} Python.' .format('love'))  # formatting strings using strings

print('{} {} {}'.format('I', 'love', 'Python.'))
print('{0} {1} {2}. {2} {1}s {3}'.format('I', 'love', 'Jay', 'me'))  # formatting strings using indices
first = 'I'
sec = 'love'
third = 'coding'
print('{} {} {}'.format(first, sec, third))  # formatting strings using variables

version = 3
print('I love Pyhton {}.'.format(version))

print('\n')
# format specification
# The number before the colon is the index of the value in the lists of the format method.
# the number following the colon makes value to format at least 8 characters in length
print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apple', 3))
print('{0:8} | {1:8}'.format('Oranges', 10))
