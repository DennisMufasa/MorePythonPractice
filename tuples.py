# Taples are immutable lists that are ordered.
# Used when storing data that doesnt change
# Values are accessed by indices
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

fisrtDay = days[0]
print(fisrtDay)

print('\n')

for day in days:
    print(day)

print('\n')
weekends = ('Saturday','Sunday')
listWeekends = list(weekends)   # converts to list(array)
print(listWeekends)

students = ['Deniese', 'Lola', 'Daren']
girls = tuple(students)         # conerts to tuple
print(girls)

print('\n')
print(type(students))
print(type(weekends))

print('\n')

contact_info = ['555-74123', 'denny.muasa@gmail.com']
(phone, email) = contact_info
print(phone)
print(email)


