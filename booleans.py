if 37 < 40:
    print('True')
else:
    print('False')

yob = input('Enter your Year of birth')
age = 2018 - int(yob)

if  age >= 35:
    print("You're old enough to be President!")
elif age >= 30:
    print("You're old enough to be a senetor!")
elif age >= 25:
    print("You're old enough to be an MCA!")
else:
    print("Not today!")
print("Have a nice day")
