while True:
    text = input('Enter your name')
    textLength = len(text)
    if text == 'stop':
        break
    print('  {}'.format('_' * textLength))
    print('< {} >'.format(text))
    print('  {}'.format('-' * textLength))


