def evenOdd(number):
    """Determining whether a number is odd or even"""
    number = int(number)
    if number % 2 == 0:
        print('{} is even'.format(number))
    else:
        print('{} is odd'.format(number))


# evenOdd(4)

def oddEven(number):
    """Determining whether a number is even or odd"""
    number = int(number)
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'


test = oddEven(71)
print(test)
