students = {
    'Vanita': {
        'math': input('Enter Vanita Mathematics score'),
        'eng': input('Enter Vanita English score'),
        'kis': input('Enter Vanita Kiswahili score'),
        'sci': input('Enter Vanita Science score'),
        'hum': input('Enter Vanita Humanities score')
    },

    'Zeituni': {
        'math': input('Enter Zeituni Mathematics score'),
        'eng': input('Enter Zeituni  English score'),
        'kis': input('Enter Zeituni Kiswahili score'),
        'sci': input('Enter Zeituni Science score'),
        'hum': input('Enter Zeituni Humanities score')
    },
    'Marlon': {
        'math': input('Enter Marlon Mathematics score'),
        'eng': input('Enter Marlon  English score'),
        'kis': input('Enter Marlon Kiswahili score'),
        'sci': input('Enter Marlon Science score'),
        'hum': input('Enter Marlon Humanities score')
    }
}
print('Student Marks \n')
for student in students:
    print('{0}: \n'
          'Mathematics -    {1} \n'
          'English     -    {2} \n'
          'Kiswahili   -    {3} \n'
          'Science     -    {4} \n'
          'Humanities  -    {5}\n'
        .format(student, students[student]['math'], students[student]['eng'], students[student]['kis'], students[student]['sci'], students[student]['hum']))

