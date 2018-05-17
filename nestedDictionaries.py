employees = {
    'Melanie': {
        'phone number': '555-8523',
        'email': 'melanie@gmail.com'
    },
    'Sly': {
        'phone number': '555-9632',
        'email': 'sylvia@gmail.com'
    },
    'Anne': {
        'phone number': '555-7412',
        'email': 'annie@gmail.com'
    }
}

for employee in employees:
    print('{0}\'s phone number is {1} and her email is {2}'.format(employee,employees[employee]['phone number'],employees[employee]['email']))

print('\n')

# example II
students = {
    'Vanita': {
        'math': 90,
        'eng': 25,
        'kis': 15,
        'sci': 100,
        'hum': 75
    },

    'Zeituni': {
        'math': 80,
        'eng': 27,
        'kis': 100,
        'sci': 10,
        'hum': 78
    },
    'Marlon': {
        'math': 70,
        'eng': 45,
        'kis': 65,
        'sci': 90,
        'hum': 45
    }
}
print('Student Marks \n')
for student in students:
    print('{0}: \n'
          'Mathematics -{1} \n'
          'English     -{2} \n'
          'Kiswahili   -{3} \n'
          'Science     -{4} \n'
          'Humanities  -{5}\n'
        .format(student, students[student]['math'], students[student]['eng'], students[student]['kis'], students[student]['sci'], students[student]['hum']))

