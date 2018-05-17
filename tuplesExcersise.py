# using tuples to assign many variables values at once
students = ['Dennis', 'Mufasa', 'Yobra']
(form1, form2, form3) = students
print(form1 + '\n' + form2 + '\n' + form3)

# using tuple assignment in functions


def high_low(num):
    high = max(num)
    low = min(num)

    return high, low


lottery = [12, 5, 18, 7, 51, 6, 24, 37, 9]
# test = high_low(lottery)
# print(test)
(highest, lowest) = high_low(lottery)
print('Highest number: {}'.format(highest))
print('Lowest number: {}'.format(lowest))

# using tuples in a for loop
contacts = (['Denny', '555-87456'],['Mufasa', '555-32145'])

for (name, phone) in contacts:
    print('{}\'s phone number is {}.'.format(name,phone))




