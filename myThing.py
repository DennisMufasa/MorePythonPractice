while True:
    name = input('Enter your name')
    nameLength = len(name)

    if name == 'stop':
        break

    print('  {}'.format('_' * nameLength))
    print('< {} >'.format(name))
    print('  {}'.format('-' * nameLength))
