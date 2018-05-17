def getName():
    name = input('Enter your name.')
    return name


def sayName(name):
    print('Your name is {}'.format(name))


def getSayName():
    name = getName()
    sayName(name)


getSayName()
# help(getSayName)
