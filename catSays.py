while True:
    say = input('What would you like the cat to say?')
    # Determining speech Bubble length
    textLength = len(say)

    if say == 'stop':
        break

    print('          {}'.format('_' * textLength))
    print('         <{}>'.format(say))
    print('          {}'.format('-' * textLength))
    print('        /')
    print(' /\_/\ /')
    print('( o.o ) ')
    print(' > ^ < ')
