fruit = "apple"
print(fruit)
student_name = 'Mufasa'
print(student_name)
first3letters = 'ABC'
print(first3letters)
sentence = 'She said, \"That\'s a great tasting apple"'
print(sentence)
sentence2 = "She said, \'That\'s a great tasting apple\'"
print(sentence2)
name = 'Mufasa'
firstChar = name[0]
print(firstChar)

num = 25
goldenRatio = float(num) * 1.618  # converting int num to float
print(goldenRatio)

print('\n')
"""The code below creates a file mufasa.txt and writes some text into it"""
with open('mufasa.txt', 'w') as file:
    file.write('Hello everyone.\nI\'m happy to be studying python.')

with open('mufasa.txt') as file1:
    for line in file1:
        print(line)

