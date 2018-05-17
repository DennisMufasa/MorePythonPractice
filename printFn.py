print(' (. )( .)')
print('  |   |')
print('  | . |   ')
print(' (  \/ )')
print('  \   /')

print('\n')

# cat
print(' /\_/\ ')
print('(o . o)')
print(' > ^ <')

print('\n')

while True:
    text = input('Enter any text.')
    textLength = len(text)

    if text == 'stop':
        break

    # speech bubble
    print('  {}'.format('_' * textLength))
    print('< {} >'.format(text))
    print('  {}'.format('-' * textLength))
